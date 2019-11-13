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
    pysubdir = f"custom_volumes/{package_id}/"

    pysubdir_new = f"custom_volumes/{package_id}_min/"

    os.makedirs(pysubdir_new, exist_ok=True)

    shutil.copy2(f"{pysubdir}meta.json", f"{pysubdir_new}meta.json")

    merged = ""
    for rpy in glob.glob(os.path.join(pysubdir, "*.rpy")):
        with open(rpy, "r") as rpyfp:
            merged += rpyfp.read()
    with open(os.path.join(pysubdir_new, f"{package_id}.rpy"), "w") as fp:
        fp.write(merged)

    cmdstr = f"python rpatool.py -c custom_volumes/{package_id}_min/assets.rpa"
    if os.path.isdir(os.path.join(pysubdir, "assets")):
        cmdstr += f" custom_assets_{package_id}={pysubdir}assets"
    if os.path.isdir(os.path.join(pysubdir, "assets_common")):
        cmdstr += f" custom_assets={pysubdir}assets_common"
    print(cmdstr)
    retcode = subprocess.call(cmdstr.split(" "))
