#!/bin/python3

# This is the main script that patches custom resources into the main game.

import subprocess
import os
import glob
from distutils.dir_util import copy_tree
import json
from pprint import pprint
import traceback
import shutil
import re
import textwrap

platform = os.name

if platform == "nt":
    gamedir_root = "C:/Program Files (x86)/Steam/steamapps/common/Homestuck Pesterquest"
    executable = "pesterquest.exe"
elif platform == "posix":
    # If you're on linux, change this path to your steam install directory.
    gamedir_root = os.environ["HOME"] + "/Library/Application Support" + "/Steam/steamapps/common/Homestuck Pesterquest"
    executable = "pesterquest"
else:
    raise Exception("Unknown platform " + platform)

gamedir = os.path.normpath(os.path.join(gamedir_root, "game"))

with open("subtable.json", "r") as fp:
    rpy_sub_table = json.load(fp)


dummy_package = {
    "package_id": "pid",
    "volumes": [
        {
            "volume_id": "vid",
            "title": "title",
            "subtitle": "pull quote",
            "author": "author"
        }
    ]
}

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


def subtableReplace(textdata, fstrings=dummy_package, subtable=rpy_sub_table):
    for rtype, pattern, repl in subtable:
        if rtype == "R":
            textdata = re.sub(pattern, repl, textdata, flags=re.MULTILINE)
        elif rtype == "S":
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
        rpy_data = subtableReplace(rpy_data, metadata)
        with open(dst, 'w') as fp:
            fp.write(rpy_data)
        if not quiet:
            print("{} --> {}".format(src, dst))
    except Exception:
        if not quiet:
            print("{} -x> {}".format(src, dst))
        raise


def processPackages(only_volumes=[], quiet=False):
    all_volumes = []
    warn = False

    filtering_volumes = (only_volumes != [])
    only_volumes.append("sys")

    os.makedirs(os.path.join("../custom_volumes"), exist_ok=True)
    os.makedirs(os.path.join("../custom_volumes_other"), exist_ok=True)

    sysdir = os.path.join(".", "sys/")
    for subdir in [sysdir] + glob.glob(os.path.join("../custom_volumes", "*/")):
        print()
        # Load metadata from json file
        try:
            # Load raw json from file
            meta_filepath = os.path.join(subdir, "meta.json")
            with open(meta_filepath, "r") as fp:
                meta = json.load(fp)

            # Grab metadata id
            package_id = meta["package_id"]
            if filtering_volumes and package_id not in only_volumes:
                continue

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

        # custom_rpa_dir = os.path.join(gamedir, "custom_archives")
        # os.makedirs(custom_rpa_dir, exist_ok=True)
        for rpa in glob.glob(os.path.join(subdir, "*.rpa")):
            __, filename = os.path.split(rpa)
            destfile = os.path.join(gamedir, (f"ycustom_{package_id}_{filename}"))
            # destfile = os.path.join(gamedir, (f"{os.path.splitext(filename)[0]}_custom_.rpa" if (subdir == sysdir) else f"ycustom_{package_id}_{filename}"))
            copy2(rpa, destfile, quiet=quiet)

        # Parse and copy rpy files
        custom_scripts_dir = os.path.join(gamedir, "custom_scripts")
        os.makedirs(custom_scripts_dir, exist_ok=True)
        for rpy in glob.glob(os.path.join(subdir, "*.rpy")):
            __, filename = os.path.split(rpy)
            destfile = os.path.join(custom_scripts_dir, (f"{os.path.splitext(filename)[0]}_custom_.rpy" if (subdir == sysdir) else f"zcustom_{package_id}_{filename}"))
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
    return {
        k: v.replace('"', '\\"')
        for k, v in
        table1.items()
    }


def processVolumes(all_volumes, quiet=False):
    with open(os.path.join("templates", "vol_select_custom_template.rpy"), "r") as fp:
        template_data = fp.read()

    template_data = template_data.replace("{{num_custom_volumes}}", str(len(all_volumes)))

    for volume in sorted(all_volumes, key=lambda v: v["author"]):
        if not quiet:
            pprint(volume)
        volume["entrypoint"] = subtableReplace("{{package_entrypoint}}_", volume) + volume["volume_id"]

        # Doesn't work with rpa archives.

        # volume_id = volume["volume_id"]
        # required_files = [
        #     os.path.join(gamedir, f"custom_assets_{volume['package_id']}", f"volumeselect_{volume_id}.png"),
        #     os.path.join(gamedir, f"custom_assets_{volume['package_id']}", f"volumeselect_{volume_id}.png")
        # ]
        # for expected_file in required_files:
        #     if not os.path.isfile(expected_file):
        #         raise FileNotFoundError(expected_file)

        print("Inserting at", volume["entrypoint"])

        with open(os.path.join("templates", "vol_select_entry_template.rpy"), "r") as fp:
            new_entry = fp.read().format(**jsonReEscape(volume))

        template_data = template_data.replace(
            "{{volumes}}", 
            textwrap.indent(new_entry, "    " * 5) + "\n{{volumes}}")

    template_data = template_data.replace("{{volumes}}", "")
    with open(os.path.join(gamedir, "custom_volumeselect.rpy"), 'w') as fp:
        fp.write(template_data)


def runGame():
    subprocess.run(os.path.join(gamedir_root, executable))


def makeArgParser():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--nolaunch", action="store_true",
        help="Don't launch the game, only patch the assets. Useful during development for real-time reloading.")
    ap.add_argument(
        "--quiet", action="store_true",
        help="Print less output about successful operations.")
    ap.add_argument(
        "--pause", action="store_true",
        help="Pause before launching the game OR pause when script is complete.")
    ap.add_argument(
        "--clean", action="store_true",
        help="Delete old custom assets, including any old mods. Skipped by default for performance.")
    ap.add_argument(
        "--patchdir",
        help="Patch files to this directory. Defaults to your system's equivalent of steamapps/common/Homestuck Pesterquest'")
    ap.add_argument(
        "--lite", action="store_true",
        help="Lite mode: Installs a working version of PQLite, if it doesn't exist, and sets --patchdir to it. Much faster on subsequent runs.")
    ap.add_argument(
        "--liteskins", nargs="+", default=["default"],
        help="If using lite, use these distribution skins. NOT RECOMMENDED: Always test your mod without skins before distribution!")
    ap.add_argument(
        '--packages', nargs="+", default=[],
        help="If set, only look at custom packages with these IDs. By default, all mods in 'custom_volumes' are included, but if this option is set, the patcher only includes the packages specified."
    )
    return ap


def main(argstr=None):

    ap = makeArgParser()

    args = (ap.parse_args(argstr) if argstr else ap.parse_args())

    if args.lite:
        litedir = os.path.join("..", "litedist")
        from dist_standalone import copyLiteWithSkins
        copyLiteWithSkins(litedir, args.liteskins)
        args.patchdir = os.path.normpath(litedir)

    if args.patchdir:
        global gamedir_root
        global gamedir
        gamedir_root = args.patchdir
        gamedir = os.path.normpath(os.path.join(gamedir_root, "game"))
        os.makedirs(gamedir, exist_ok=True)

    if args.packages:
        args.clean = True

    try:
        print("\nClearing old scripts")
        for rpy in glob.glob(os.path.join(gamedir, "*custom_*.rpy*")):
            if not args.quiet:
                print(f"{rpy} --> [X]")
            os.unlink(rpy)
        if args.clean:

            print("\nCleaning out old assets")
            for cfile in glob.glob(os.path.join(gamedir, "custom_*/")) + glob.glob(os.path.join(gamedir, "*custom_*")):
                if not args.quiet:
                    print(f"{cfile} --> [X]")
                if os.path.isdir(cfile):
                    shutil.rmtree(cfile)

        print("\nCopying user scripts")
        (all_volumes, warn,) = processPackages(only_volumes=args.packages, quiet=args.quiet)

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


if __name__ == "__main__":
    main()
