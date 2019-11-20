import os
import glob
from pprint import pprint

platform = os.name

# Point to your decompiled resources here
gamedir_root = "../../pesterquest"

# rpy_files = {}
rpy_files = list(map(os.path.normpath, sum([
    glob.glob(os.path.join(gamedir_root, "**", "*.rpy"), recursive=True),
    glob.glob("custom_volumes/**/*.rpy", recursive=True),
    glob.glob("sys/**/*.rpy", recursive=True)
], [])))

pprint(rpy_files)

