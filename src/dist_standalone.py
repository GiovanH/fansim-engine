from distutils.dir_util import copy_tree
import sys
import os
import subprocess
import argparse


litedir = "lite"
distdir = "../dist"
skinbase = "liteskins"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--skin", default="default")
    args = ap.parse_args()

    skin = args.skin
    skindir = os.path.join(skinbase, skin)
    if not os.path.isdir(skindir):
        print("Skin not found:", skin)
        print("Should be located at", skindir)
        raise FileNotFoundError(skindir)

    # print("Clearing dist")
    # subprocess.run(["rm", "-rv", os.path.join(distdir, "game")])

    print("Copying PQ lite")
    copy_tree(litedir, distdir, update=True)

    print("Patching skin")
    copy_tree(skindir, distdir, update=True)

    print("Patching mods")
    run_patcher()


def run_patcher():
    from patcher import main as patch
    argv_ = sys.argv
    sys.argv = [sys.argv[0]]
    sys.argv.append("--patchdir")
    sys.argv.append(distdir)
    sys.argv.append("--nolaunch")
    patch()
    sys.argv = argv_


main()
