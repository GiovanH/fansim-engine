from distutils.dir_util import copy_tree
import sys
import os
import subprocess
import argparse


litedir = "lite"
distdir = "../dist"
skinbase = "liteskins"
skindir_default = os.path.join(skinbase, "default")


def copyLiteWithSkin(distdir, skindir=skindir_default):
    print("Copying PQ lite")
    copy_tree(litedir, distdir, update=True)

    print("Patching skin")
    copy_tree(skindir_default, distdir, update=True)
    if skindir != skindir_default:
        copy_tree(skindir, distdir, update=True)


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
