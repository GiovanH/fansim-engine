#!/bin/python3

# This is the main script that patches custom resources into the main game.

import subprocess
import os
import glob
from distutils.dir_util import copy_tree
import json
import shutil
import re
import collections
import _logging
import environment
import fse_mod

logger = _logging.getLogger(__name__)

platform = os.name

logger.debug("Running on platfom " + platform)

gamedir_root = environment.getGamedirRoot()
executable = environment.getExecutableName()

gamedir = os.path.normpath(os.path.join(gamedir_root, "game"))

with open("subtable.json", "r") as fp:
    rpy_sub_table = json.load(fp)


dummy_package = fse_mod.DummyPackage()

# Properties, dependent on the current gamedir


def getCustomScriptsDir():
    return os.path.join(gamedir, "custom_scripts")


def getCommonAssetsDir():
    return os.path.join(gamedir, "custom_assets")


def print_tree(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        logger.info('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            logger.info('{}{}'.format(subindent, f))


def copy2(src, dst, verbose=False):
    printer = logger.info if verbose else logger.debug
    try:
        shutil.copy2(src, dst)
        printer("{} --> {}".format(src, dst))
    except Exception:
        printer("{} -x> {}".format(src, dst))
        raise


def mergeDirIntoDir(src, dst, verbose=False):
    printer = logger.info if verbose else logger.debug
    try:
        copy_tree(src, dst, update=True, verbose=verbose)
        printer("{} --> {}".format(src, dst))
        # if verbose:
        #     print_tree(src)
    except Exception:
        printer("{} -x> {}".format(src, dst))
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
                logger.error("Availible keys:", fstrings.keys(), exc_info=True)
                raise
    return textdata


def copyAndSubRpy(src, dst, metadata, verbose=False):
    printer = logger.info if verbose else logger.debug

    if not os.path.isfile(src):
        raise FileNotFoundError(src)
    # if os.path.isfile(dst):
    #     raise FileExistsError(dst)

    with open(src, "r", encoding="utf-8") as fp:
        rpy_data = fp.read()

    try:
        rpy_data = subtableReplace(rpy_data, metadata)
        with open(dst, 'w', encoding="utf-8") as fp:
            fp.write(rpy_data)
        printer("{} --> {}".format(src, dst))
    except Exception:
        printer("{} -x> {}".format(src, dst))
        raise


def processPackages(only_volumes=[], verbose=False):
    all_packages, warn = fse_mod.getAllPackages("..", only_volumes)
    for package in all_packages:
        logger.info(f"Patching {package.id}")

        # Copy precompiled RPA archives
        for rpa in package.getArchiveFiles():
            __, filename = os.path.split(rpa)
            destfile = os.path.join(gamedir, (f"ycustom_{package.id}_{filename}"))
            copy2(rpa, destfile, verbose=verbose)

        # Parse and copy rpy files
        for rpy in package.getScriptFiles():
            __, filename = os.path.split(rpy)
            destfile = os.path.join(getCustomScriptsDir(), f"{package.id}_{filename}")
            copyAndSubRpy(rpy, destfile, package.metadata, verbose=verbose)

        # Copy namespaced assets
        if os.path.isdir(package.assets_dir):
            destdir = os.path.join(gamedir, f"custom_assets_{package.id}")
            # os.makedirs(destdir, exist_ok=True)
            mergeDirIntoDir(package.assets_dir, destdir, verbose=verbose)

        # Copy common assets
        if os.path.isdir(package.assets_common_dir):
            mergeDirIntoDir(package.assets_common_dir, getCommonAssetsDir(), verbose=verbose)

    return (all_packages, warn,)


def patchCreditsData(all_packages, verbose=False):
    # Credits
    all_credits = {}

    for package in all_packages:
        if package.credits:
            dict_merge(all_credits, package.credits)

    # pprint(all_credits)

    with open(os.path.join(getCustomScriptsDir(), "custom_credits.rpy"), 'w', encoding="utf-8") as fp:
        fp.write("init offset = 1\n\n")
        fp.write("define dlc_credits_data = ")
        fp.write(json.dumps(all_credits, indent=4))


def patchVolumeData(all_packages, verbose=False):
    # Volume select screen

    all_volumes = sum((p.volumes for p in all_packages), [])

    with open(os.path.join(getCustomScriptsDir(), "custom_volumes_data.rpy"), 'w', encoding="utf-8") as fp:
        fp.write("init offset = 1\n\n")
        fp.write("define dlc_volumes_data = ")
        fp.write(json.dumps(all_volumes, indent=4))


def patchWarningData(all_packages, verbose=False):
    # Volume select screen

    all_volumes = sum((p.volumes for p in all_packages), [])
    all_warnings = {v["title"]: v["warnings"] for v in all_volumes if v.get("warnings")}

    with open(os.path.join(getCustomScriptsDir(), "custom_warning_data.rpy"), 'w', encoding="utf-8") as fp:
        fp.write("init offset = 1\n\n")
        fp.write("define dlc_warning_data = ")
        fp.write(json.dumps(all_warnings, indent=4))


def patchAchievementsData(all_packages, verbose=False):
    # Volume select screen

    all_achievements = sum((p.achievements for p in all_packages), [])

    with open(os.path.join(getCustomScriptsDir(), "custom_achievement_data.rpy"), 'w', encoding="utf-8") as fp:
        fp.write("init offset = 1\n\n")
        fp.write("define dlc_achievements_data = ")
        fp.write(json.dumps(all_achievements, indent=4))


def runGame():
    logger.info(f"Starting {executable}")
    subprocess.run(os.path.join(gamedir_root, executable))


def makeArgParser():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--nolaunch", action="store_true",
        help="Don't launch the game, only patch the assets. Useful during development for real-time reloading.")
    ap.add_argument(
        "--verbose", action="store_true",
        help="Print more output about successful operations.")
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
    logger.debug(argstr)
    logger.debug(args)

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

    verbosePrinter = logger.info if args.verbose else logger.debug

    try:

        logger.info("Clearing old scripts")
        try:
            shutil.rmtree(getCustomScriptsDir())
        except FileNotFoundError:
            pass

        # Legacy:
        for rpy in glob.glob(os.path.join(gamedir, "*custom_*.rpy*")):
            verbosePrinter(f"{rpy} --> [X]")
            os.unlink(rpy)

        if args.clean:
            logger.info("Cleaning out old assets")
            for assets_dir in glob.glob(os.path.join(gamedir, "custom_assets_*/")):
                shutil.rmtree(assets_dir)

        logger.info("Initializing")
        os.makedirs(os.path.join("../custom_volumes"), exist_ok=True)
        os.makedirs(os.path.join("../custom_volumes_other"), exist_ok=True)
        os.makedirs(getCustomScriptsDir(), exist_ok=True)

        logger.info("Copying user scripts")
        (all_packages, warn,) = processPackages(only_volumes=args.packages, verbose=args.verbose)

        logger.info("Patching volume select data")
        patchVolumeData(all_packages, verbose=args.verbose)
        logger.info("Patching credits data")
        patchCreditsData(all_packages, verbose=args.verbose)
        logger.info("Patching warning data")
        patchWarningData(all_packages, verbose=args.verbose)
        logger.info("Patching achievements data")
        patchAchievementsData(all_packages, verbose=args.verbose)

        if warn:
            logger.warn("!!!!!!!!!!!!!!!!!!!!!!!!! Errors occured! Please review the log above for [WARN] or [ERROR] messages.")
            logger.warn("A full logfile should be availible at 'latest_debug.log'")

        if warn or args.pause:
            logger.warn("Please review this window and then press enter to launch the game OR press Ctrl+C to abort.")
            input()

        if not args.nolaunch:
            runGame()
    except Exception:
        logger.error("Root exception", exc_info=True)
        logger.warn("A full logfile should be availible at 'latest_debug.log'")
        logger.warn("Please review this window and then press enter to launch the game OR press Ctrl+C to abort.")
        input()
        return


if __name__ == "__main__":
    main()
