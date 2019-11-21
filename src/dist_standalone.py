from distutils.dir_util import copy_tree
import sys
import os
import subprocess

from patcher import main

sys.argv.append("--makepatch")
sys.argv.append("--nolaunch")

litedir = "lite"
patchdir = "../patch"
distdir = "../dist"

subprocess.run(["rm", "-rv", os.path.join(distdir, "game")])
subprocess.run(["rm", "-rv", patchdir])

print("Copying PQ lite")
copy_tree(litedir, distdir)
print("Patching")
main()
copy_tree(patchdir, distdir)
