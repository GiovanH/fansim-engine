#!/bin/python3

from sys import version_info

try:
    assert version_info.major >= 3
    assert version_info.minor >= 6
except (AssertionError, AttributeError):
    print("This script requires Python 3.6 or newer.")
    print("Press enter to exit.")
    input()
    exit()


import subprocess
import os
import glob
from distutils.dir_util import copy_tree
import json
from pprint import pprint
import traceback

gamedir_root = "C:/Program Files (x86)/Steam/steamapps/common/Homestuck Pesterquest"
executable = "pesterquest.exe"
outdir = "./pesterquest"
rpatool = "./rpatool/rpatool"

gamedir = os.path.normpath(os.path.join(gamedir_root, "game"))

with open("subtable.json", "r") as fp:
    rpy_sub_table = json.load(fp)


def print_tree(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


def mergeDirIntoDir(src, dst, quiet=False):
    if not quiet:
        print_tree(src)
    try:
        copy_tree(src, dst, update=True)
        if not quiet:
            print("{} --> {}".format(src, dst))
    except Exception:
        if not quiet:
            print("{} -x> {}".format(src, dst))
        raise


def subtableReplace(subtable, textdata, fstrings):
    for pattern, repl in subtable:
        try:
            if pattern in textdata:
                textdata = textdata.replace(pattern, repl.format(**fstrings))
        except KeyError:
            print("Availible keys:", fstrings.keys())
            raise
    return textdata


def copyAndSubRpy(src, dst, metadata, quiet=False):
    assert os.path.isfile(src)
    assert not os.path.isfile(dst)

    with open(src, "r") as fp:
        rpy_data = fp.read()

    try:
        rpy_data = subtableReplace(rpy_sub_table, rpy_data, metadata)
        with open(dst, 'w') as fp:
            fp.write(rpy_data)
        if not quiet:
            print("{} --> {}".format(src, dst))
    except Exception:
        if not quiet:
            print("{} -x> {}".format(src, dst))
        raise


def processPackages(quiet=False):
    all_volumes = []
    warn = False
    sysdir = os.path.join(".", "sys/")
    for subdir in [sysdir] + glob.glob(os.path.join("custom_volumes", "*/")):
        print()
        # Load metadata from json file
        try:
            # Load raw json from file
            meta_filepath = os.path.join(subdir, "meta.json")
            with open(meta_filepath, "r") as fp:
                meta = json.load(fp)

            # Grab metadata id
            package_id = meta["package_id"]

            dirname = os.path.split(os.path.dirname(subdir))[-1]
            if not package_id == dirname:
                print(f"[WARNING]\tPackage {package_id} is in incorrectly named folder {dirname}")

            # Backreference containing package and add to volume list
            for volume in meta["volumes"]:
                volume["package_id"] = meta["package_id"]
                all_volumes.append(volume)

        except FileNotFoundError:
            print(f"[ERROR]\tMissing configuration file {meta_filepath}, required!")
            warn = True
            continue
        except KeyError as e:
            print(f"[ERROR]\t{meta_filepath} missing required key '{e.args[0]}'!")
            warn = True
            continue

        # Identify system vs volume packages.
        prefix = ("" if (subdir == sysdir) else "_vol")

        print(f"Detected package {package_id} at {subdir}")

        # Parse and copy rpy files
        for rpy in glob.glob(os.path.join(subdir, "*.rpy")):
            __, filename = os.path.split(rpy)
            destfile = os.path.join(gamedir, f"custom{prefix}_{package_id}_{filename}")
            copyAndSubRpy(rpy, destfile, meta, quiet=quiet)

        # Copy namespaced assets
        assets_dir = os.path.join(subdir, "assets")
        if os.path.isdir(assets_dir):
            destdir = os.path.join(gamedir, f"custom_assets_{package_id}")
            mergeDirIntoDir(assets_dir, destdir, quiet=quiet)

        # Copy common assets
        assets_common_dir = os.path.join(subdir, "assets_common")
        if os.path.isdir(assets_common_dir):
            destdir = os.path.join(gamedir, f"custom_assets")
            mergeDirIntoDir(assets_common_dir, destdir, quiet=quiet)

    return (all_volumes, warn,)


def jsonReEscape(table1):
    table2 = {
        k: v.replace('"', '\\"')
        for k, v in
        table1.items()
    }
    return table2


def processVolumes(all_volumes, quiet=False):
    with open("vol_select_custom_template.rpy", "r") as fp:
        template_data = fp.read()

    for volume in all_volumes:
        pprint(volume)
        volume_id = volume["volume_id"]
        volume["entrypoint"] = subtableReplace(rpy_sub_table, "{{package_entrypoint}}_", volume) + volume["volume_id"]

        required_files = [
            os.path.join(gamedir, "custom_assets", f"volumeselect_{volume_id}.png"),
            os.path.join(gamedir, "custom_assets", f"volumeselect_{volume_id}_small.png")
        ]
        for expected_file in required_files:
            if not os.path.isfile(expected_file):
                raise FileNotFoundError(expected_file)

        print("Inserting at", volume["entrypoint"])

        with open("vol_select_entry_template.rpy", "r") as fp:
            new_entry = fp.read().format(**jsonReEscape(volume))

        template_data = template_data.replace("{{}}", new_entry + "\n{{}}")

    template_data = template_data.replace("{{}}", "")
    with open(os.path.join(gamedir, "custom_volumeselect.rpy"), 'w') as fp:
        fp.write(template_data)


def runGame():
    subprocess.run(os.path.join(gamedir_root, executable))


if __name__ == "__main__":

    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--nolaunch", action="store_true",
        help="Don't launch the game.")
    ap.add_argument(
        "--quiet", action="store_true",
        help="Print less output about successful operations")
    ap.add_argument(
        "--pause", action="store_true",
        help="Pause before launching the game OR pause when script is complete.")
    args = ap.parse_args()

    from snip.stream import std_redirected
    with std_redirected("latest.log", tee=True):
        try:

            print("\nClearing old scripts")

            for rpy in glob.glob(os.path.join(gamedir, "custom*.rpy*")):
                if not args.quiet:
                    print(f"{rpy} --> [X]")
                os.unlink(rpy)

            print("\nCopying user scripts")
            (all_volumes, warn,) = processPackages(quiet=args.quiet)

            print("\nCompiling volumes")
            processVolumes(all_volumes, quiet=args.quiet)

            if warn:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!! Errors occured!")

            if warn or args.pause:
                print("Please review this window and then press enter to launch the game OR press Ctrl+C to abort.")
                input()

            print(f"Starting {executable}")

            if not args.nolaunch:
                runGame()
        except Exception:
            traceback.print_exc()
            raise
