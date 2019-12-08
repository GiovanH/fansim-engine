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
skindir_default = os.path.join(skinbase, "default")


def crcFile(fileName):
    prev = 0
    for eachLine in open(fileName, "rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X" % (prev & 0xFFFFFFFF)


def copyLiteWithSkin(destdir, skindir=skindir_default):
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
    copy_tree(skindir_default, destdir, update=True)
    if skindir != skindir_default:
        copy_tree(skindir, destdir, update=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--skin", default="default")
    ap.add_argument(
        '--volumes', nargs="+", default=[],
        help="If set, only look at custom volumes with these IDs."
    )
    args = ap.parse_args()

    skin = args.skin
    skindir = os.path.join(skinbase, skin)
    if not os.path.isdir(skindir):
        print("Skin not found:", skin)
        print("Should be located at", skindir)
        raise FileNotFoundError(skindir)

    # print("Clearing dist")
    # subprocess.run(["rm", "-rv", os.path.join(distdir, "game")])

    copyLiteWithSkin(distdir, skindir)

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
