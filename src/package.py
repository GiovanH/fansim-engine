# Experimental
# RPA files go in custom_volumes/{package_id}/
# You should not use RPA files if you also have an assets folder!


from sys import version_info

try:
    assert version_info.major >= 3
    assert version_info.minor >= 6
except (AssertionError, AttributeError):
    print("This script requires Python 3.6 or newer.")
    print("Press enter to exit.")
    input()
    exit()

import os
import sys
import subprocess
import glob
import shutil

for package_id in sys.argv[1:]:
    pysubdir = f"../custom_volumes_other/{package_id}/"

    pysubdir_new = f"../custom_volumes/{package_id}_min/"

    os.makedirs(pysubdir_new, exist_ok=True)

    shutil.copy2(f"{pysubdir}meta.json", f"{pysubdir_new}meta.json")
    shutil.copy2(f"{pysubdir}credits.yml", f"{pysubdir_new}credits.yml")

    merged = "init offset = 1\n\n"
    for rpy in glob.glob(os.path.join(pysubdir, "*.rpy")):
        with open(rpy, "r") as rpyfp:
            merged += f"# {rpy}\n{rpyfp.read()}\n"
    with open(os.path.join(pysubdir_new, f"{package_id}.rpy"), "w") as fp:
        fp.write(merged)

    rpapath = f"../custom_volumes/{package_id}_min/assets.rpa"
    cmdstr = f"python rpatool.py -c {rpapath}"
    if os.path.isdir(os.path.join(pysubdir, "assets")):
        cmdstr += f" custom_assets_{package_id}={pysubdir}assets"
    if os.path.isdir(os.path.join(pysubdir, "assets_common")):
        cmdstr += f" custom_assets={pysubdir}assets_common"
    print(cmdstr)

    if os.path.isfile(rpapath):
        os.unlink(rpapath)
    retcode = subprocess.call(cmdstr.split(" "))
