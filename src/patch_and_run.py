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
import shutil


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


def copy2(src, dst, quiet=False):
    try:
        shutil.copy2(src, dst)
        if not quiet:
            print("{} --> {}".format(src, dst))
    except Exception:
        if not quiet:
            print("{} -x> {}".format(src, dst))
        raise


def mergeDirIntoDir(src, dst, quiet=False):
    try:
        copy_tree(src, dst, update=True)
        if not quiet:
            print("{} --> {}".format(src, dst))
        if not quiet:
            print_tree(src)
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
    if not os.path.isfile(src):
        raise FileNotFoundError(src)
    # if os.path.isfile(dst):
    #     raise FileExistsError(dst)

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

        print(f"Detected package {package_id} at {subdir}")

        for rpa in glob.glob(os.path.join(subdir, "*.rpa")):
            __, filename = os.path.split(rpa)
            destfile = os.path.join(gamedir, (f"{os.path.splitext(filename)[0]}_custom_.rpa" if (subdir == sysdir) else f"ycustom_{package_id}_{filename}"))
            copy2(rpa, destfile, quiet=quiet)

        # Parse and copy rpy files
        for rpy in glob.glob(os.path.join(subdir, "*.rpy")):
            __, filename = os.path.split(rpy)
            destfile = os.path.join(gamedir, (f"{os.path.splitext(filename)[0]}_custom_.rpy" if (subdir == sysdir) else f"zcustom_{package_id}_{filename}"))
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

        # required_files = [
        #     os.path.join(gamedir, f"custom_assets_{volume['package_id']}", f"volumeselect_{volume_id}.png"),
        #     os.path.join(gamedir, f"custom_assets_{volume['package_id']}", f"volumeselect_{volume_id}.png")
        # ]
        # for expected_file in required_files:
        #     if not os.path.isfile(expected_file):
        #         raise FileNotFoundError(expected_file)

        print("Inserting at", volume["entrypoint"])

        with open("vol_select_entry_template.rpy", "r") as fp:
            new_entry = fp.read().format(**jsonReEscape(volume))

        template_data = template_data.replace("{{volumes}}", new_entry + "\n{{volumes}}")

    template_data = template_data.replace("{{volumes}}", "")
    with open(os.path.join(gamedir, "xcustom_volumeselect.rpy"), 'w') as fp:
        fp.write(template_data)


def runGame():
    subprocess.run(os.path.join(gamedir_root, executable))


@contextmanager
def std_redirected(outfile, errfile=None, tee=False):
    """Summary

    Args:
        outfile (TYPE): Description
        errfile (None, optional): Description

    Yields:
        TYPE: Description
    """
    import sys  # Must import basename for naming to bind globally
    if errfile is None:
        errfile = outfile

    # Save file handle
    _stdout = sys.stdout
    _stderr = sys.stderr

    sys.stdout = open(outfile, 'w')
    sys.stderr = open(errfile, 'w') if outfile != errfile else sys.stdout

    if tee:
        sys.stdout = stream_tee(sys.stdout, _stdout)
        sys.stderr = stream_tee(sys.stderr, _stderr)

    try:
        yield None
    finally:
        sys.stdout.close()
        sys.stderr.close()  # Safe to use even if stdout == stderr
        sys.stdout = _stdout
        sys.stderr = _stderr


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
    ap.add_argument(
        "--clean", action="store_true",
        help="Delete old custom assets")
    args = ap.parse_args()

    with std_redirected("latest.log", tee=True):
        try:

            if args.clean:
                print("\nCleaning out old assets")
                for rpy in glob.glob(os.path.join(gamedir, "custom_*/")):
                    if not args.quiet:
                        print(f"{rpy} --> [X]")
                    shutil.rmtree(rpy)

                print("\nClearing old scripts")

                for rpy in glob.glob(os.path.join(gamedir, "*custom_*.rpy*")):
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

            if not args.nolaunch:
                print(f"Starting {executable}")
                runGame()
        except Exception:
            traceback.print_exc()
            raise
