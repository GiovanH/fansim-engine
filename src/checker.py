import os
import glob
from pprint import pprint
import json
import re

platform = os.name

# Point to your decompiled resources here
gamedir_root = "../../pesterquest"


def listmapglob(p):
    return list(map(os.path.normpath, glob.glob(p, recursive=True)))


def init():
    global rpy_files_custom_vols, rpy_files_custom_sys, rpy_files_vanilla
    global rpy_files_custom, rpy_files

    rpy_files_custom_vols = listmapglob("../custom_volumes/**/*.rpy")
    rpy_files_custom_sys = listmapglob("sys/**/*.rpy")
    rpy_files_vanilla = listmapglob(os.path.join(gamedir_root, "**", "*.rpy"))

    rpy_files_custom = rpy_files_custom_vols + rpy_files_custom_sys
    rpy_files = rpy_files_custom + rpy_files_vanilla

    # pprint([rpy_files_custom_vols, rpy_files_custom_sys, rpy_files_vanilla])


def checkMeta():
    for subdir in glob.glob(os.path.join("../custom_volumes", "*/")):
        meta_filepath = os.path.join(subdir, "meta.json")
        with open(meta_filepath, "r") as fp:
            meta = json.load(fp)

        # Grab metadata id
        package_id = meta["package_id"]

        dirname = os.path.split(os.path.dirname(subdir))[-1]
        if package_id != dirname:
            print(f"[WARNING]\tPackage {package_id} is in incorrectly named folder {dirname}")


def checkNames():
    global names
    names = {}

    def checkGlobalNames(lineno, line, ignore=False):
        pattern = r"(\n|^)\s*(define|style|transform|image)\s+([^{}]+\s*)(=|:)"
        for match in re.finditer(pattern, line):
            __, type, name, __ = match.groups()
            key = (type, name)

            if names.get(key) and not ignore:
                conflict = names.get(key)
                (cfile, clineno, cline) = conflict
                print(f"[ERROR]\t[{rpy}:{lineno}] '{line[:-1][:75]}[...]'\n\t{type} '{name}' already defined at \n\t[{cfile}:{clineno}] '{cline}[...]'")
            else:
                names[key] = (rpy, lineno, line[:-1][:75])

    def checkCustomNames(lineno, line):
        pattern = r"(\n|^)\s*(define|style|transform|image)\s+([^\s{}]+)\s*="
        for match in re.finditer(pattern, line):
            __, type, name = match.groups()
            print(f"[WARNING]\t[{rpy}:{lineno}] '{line[:-1][:75]}[...]'\n\t\t{type} '{name}' is not namespaced! Please include a substitution " + r"('{{p}}') to prevent conflicts.")

    for rpy in rpy_files_vanilla:
        with open(rpy, "r") as rpyfp:
            lineno = 0
            for line in rpyfp.readlines():
                lineno += 1
                checkGlobalNames(lineno, line, ignore=True)

    for rpy in rpy_files_custom_sys:
        with open(rpy, "r") as rpyfp:
            lineno = 0
            for line in rpyfp.readlines():
                lineno += 1
                checkGlobalNames(lineno, line)

    for rpy in rpy_files_custom_vols:
        with open(rpy, "r") as rpyfp:
            lineno = 0
            for line in rpyfp.readlines():
                lineno += 1
                checkGlobalNames(lineno, line)
                checkCustomNames(lineno, line)


def main():
    checkMeta()
    checkNames()


if __name__ == "__main__":
    init()
    main()
