from distutils.dir_util import copy_tree
# import sys
import os
# import subprocess
import argparse
import zipfile
import zlib


litedir = "lite"
litearch = "lite.zip"
distdir = "../dist"
skinbase = "liteskins"


def crcFile(fileName):
    prev = 0
    for eachLine in open(fileName, "rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X" % (prev & 0xFFFFFFFF)


def copyLiteWithSkins(destdir, skins=["default"]):
    print("Copying PQ lite")

    needs_extract = True
    zipcrc_path = os.path.join(destdir, ".zipcrc")
    real_crc = crcFile(litearch)
    if os.path.isfile(zipcrc_path):
        with open(zipcrc_path, "r") as fp:
            cache_crc = fp.read()
        if real_crc == cache_crc:
            needs_extract = False
            print("Skipping extraction: CRC match")
    else:
        print("No CRC cache")

    if needs_extract:
        print("Extracting...")
        with zipfile.ZipFile(litearch, "r") as z:
            z.extractall(destdir)
        with open(zipcrc_path, "w") as fp:
            fp.write(real_crc)

    copy_tree(litedir, destdir, update=True)

    print("Patching skin")
    for skin in ["default"] + skins:
        skindir = os.path.join(skinbase, skin)
        if not os.path.isdir(skindir):
            print("Skin not found:", skin)
            print("Should be located at", skindir)
            raise FileNotFoundError(skindir)
        copy_tree(skindir, destdir, update=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--skins", nargs="+", default=["default"],
        help="Pack the mod with these skins, in order. The default skin is always included. For example, '--skins hiveswap befriendus' will use the hiveswap skin, but replace any assets that conflict with the befriendus skin with the befriendus version.")
    ap.add_argument(
        '--volumes', nargs="+", default=[],
        help="If set, only package thecustom volumes with these IDs. For example, '--volumes openbound mymod' will package both the openbound and mymod packages, allowing mymod to use assets openbound provides. Order is not sensitive."
    )
    args = ap.parse_args()

    print("READ THIS:")
    print()
    print("Distributing your PQMS mod standalone is generally not recommended.")
    print("Please only use this feature for large projects where standalone distribution is required.")
    print()
    print("Further, if you do use this feature, always distribute a mod-only version as an option,")
    print("  so people aren't forced to use the standalone version. For more details, see the readme.")
    print("By using this tool, you agree that you have read and understand this, and will not distribute")
    print("  a standalone version of the game without providing the option to download the mod by itself.")
    print()
    input("Press enter if you agree. Otherwise, press Ctrl+C or close this window.\n")

    copyLiteWithSkins(distdir, args.skins)

    print("Patching mods")
    run_patcher(args.volumes)


def run_patcher(volumes=[]):
    from patcher import main as patch
    if volumes != []:
        patch(["--patchdir", distdir, "--clean", "--nolaunch", "--volumes", *volumes])
    else:
        patch(["--patchdir", distdir, "--clean", "--nolaunch"])


if __name__ == "__main__":
    main()
