
from distutils.dir_util import copy_tree
import sys
import os

from patcher import main

sys.argv.append("--makepatch")
sys.argv.append("--nolaunch")

litedir = "lite"
patchdir = "../patch"
distdir = "../dist"

# os.unlink(distdir)

print("Copying PQ lite")
copy_tree(litedir, distdir)
print("Patching")
main()
copy_tree(patchdir, distdir)
