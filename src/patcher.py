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
import collections

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


CUSTOM_SCRIPTS_DIR = os.path.join(gamedir, "custom_scripts")
SYSDIR = os.path.join(".", "sys/")
COMMON_ASSETS_DIR = os.path.join(gamedir, f"custom_assets")


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


def dict_merge(dct, merge_dct):
    for k, v in merge_dct.items():
        if k in dct: 
            if isinstance(dct[k], dict) and isinstance(merge_dct[k], collections.Mapping):
                dict_merge(dct[k], merge_dct[k])
            elif isinstance(dct[k], list) and isinstance(merge_dct[k], list):
                dct[k] = list(set(dct[k]).union(merge_dct[k]))
        else:
            dct[k] = merge_dct[k]


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
    from pqms_mod import Package

    all_packages = []
    warn = False

    filtering_volumes = (only_volumes != [])
    only_volumes.append("sys")

    for subdir in [SYSDIR] + glob.glob(os.path.join("../custom_volumes", "*/")):
        try:
            package = Package(subdir)

            if filtering_volumes and package.id not in only_volumes:
                continue

            all_packages.append(package)

        except FileNotFoundError as e:
            print(f"[ERROR]\tMissing configuration file {e}, required!")
            warn = True
            continue

    for package in all_packages:
        print(f"Detected package {package.id} at {package.root}")

        # Copy precompiled RPA archives
        for rpa in package.getArchiveFiles():
            __, filename = os.path.split(rpa)
            destfile = os.path.join(gamedir, (f"ycustom_{package.id}_{filename}"))
            copy2(rpa, destfile, quiet=quiet)

        # Parse and copy rpy files
        for rpy in package.getScriptFiles():
            __, filename = os.path.split(rpy)
            destfile = os.path.join(CUSTOM_SCRIPTS_DIR, (f"{os.path.splitext(filename)[0]}_custom_.rpy" if (subdir == SYSDIR) else f"zcustom_{package.id}_{filename}"))
            copyAndSubRpy(rpy, destfile, package.metadata, quiet=quiet)

        # Copy namespaced assets
        if os.path.isdir(package.assets_dir):
            destdir = os.path.join(gamedir, f"custom_assets_{package.id}")
            os.makedirs(destdir, exist_ok=True)
            mergeDirIntoDir(package.assets_dir, destdir, quiet=quiet)

        # Copy common assets
        if os.path.isdir(package.assets_common_dir):
            mergeDirIntoDir(package.assets_common_dir, COMMON_ASSETS_DIR, quiet=quiet)

    return (all_packages, warn,)


def reEscapeString(str_):
    return str_.replace('"', '\\"')


def jsonReEscape(table1):
    return {
        k: (reEscapeString(v) if type(v) is str else v)
        for k, v in
        table1.items()
    }


def patchCreditsTemplate(all_packages, quiet=False):
    # Credits
    with open(os.path.join("templates", "credits_custom_template.rpy"), "r") as fp:
        template_data = fp.read()

    with open(os.path.join("templates", "credits_header_custom_template.rpy"), "r") as fp:
        template_data_header = fp.read()

    with open(os.path.join("templates", "credits_listitem_custom_template.rpy"), "r") as fp:
        template_data_listitem = fp.read()

    with open(os.path.join("templates", "credits_keyitem_custom_template.rpy"), "r") as fp:
        template_data_keyitem = fp.read()

    with open(os.path.join("templates", "credits_postscript_custom_template.rpy"), "r") as fp:
        template_data_postscript = fp.read()

    all_credits = {}

    for package in all_packages:
        if package.credits:
            dict_merge(all_credits, package.credits)

    # pprint(all_credits)

    for role, list_ in all_credits.get("LIST", {}).items():
        template_data = template_data.replace(
            "{{credits}}",
            textwrap.indent(
                template_data_header.format(name=reEscapeString(role)),
                "    " * 3
            ) + "\n{{credits}}")
        for name in list_:
            template_data = template_data.replace(
                "{{credits}}",
                textwrap.indent(
                    template_data_listitem.format(name=reEscapeString(name)),
                    "    " * 3
                ) + "\n{{credits}}")

    for role, person_credits in all_credits.get("DICT", {}).items():
        template_data = template_data.replace(
            "{{credits}}",
            textwrap.indent(
                template_data_header.format(name=reEscapeString(role)),
                "    " * 3
            ) + "\n{{credits}}")
        for name, list_ in person_credits.items():
            template_data = template_data.replace(
                "{{credits}}",
                textwrap.indent(
                    template_data_keyitem.format(
                        name=reEscapeString(name), 
                        credits=reEscapeString(", ".join(list_))
                    ),
                    "    " * 3
                ) + "\n{{credits}}")

    for text in all_credits.get("POSTSCRIPT", []):
        template_data = template_data.replace(
            "{{postscript}}",
            textwrap.indent(
                template_data_postscript.format(text=reEscapeString(text)),
                "    " * 3
            ) + "\n{{postscript}}")

    with open(os.path.join(gamedir, "custom_credits.rpy"), 'w', encoding="utf-8") as fp:
        fp.write(template_data.replace("{{credits}}", "").replace("{{postscript}}", ""))


def patchVolSelectTemplate(all_packages, quiet=False):
    # Volume select screen

    all_volumes = sum((p.volumes for p in all_packages), [])

    with open(os.path.join("templates", "vol_select_custom_template.rpy"), "r") as fp:
        template_data = fp.read()
        template_data = template_data.replace("{{num_custom_volumes}}", str(len(all_volumes)))

    volumes_by_author = sorted(all_volumes, key=lambda v: v["author"])
    for volume in volumes_by_author:
        if not quiet:
            pprint(volume)
        volume["entrypoint"] = subtableReplace("{{package_entrypoint}}_", volume) + volume["volume_id"]

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
    print(f"Starting {executable}")
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

        print("Initializing")
        os.makedirs(os.path.join("../custom_volumes"), exist_ok=True)
        os.makedirs(os.path.join("../custom_volumes_other"), exist_ok=True)
        os.makedirs(CUSTOM_SCRIPTS_DIR, exist_ok=True)

        print("\nCopying user scripts")
        (all_packages, warn,) = processPackages(only_volumes=args.packages, quiet=args.quiet)

        print("\nPatching volume select template")
        patchVolSelectTemplate(all_packages, quiet=args.quiet)
        print("\nPatching credits template")
        patchCreditsTemplate(all_packages, quiet=args.quiet)

        if warn:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!! Errors occured!")

        if warn or args.pause:
            print("Please review this window and then press enter to launch the game OR press Ctrl+C to abort.")
            input()

        if not args.nolaunch:
            runGame()
    except Exception:
        traceback.print_exc()
        raise


if __name__ == "__main__":
    main()
