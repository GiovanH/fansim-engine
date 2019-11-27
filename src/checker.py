import os
import glob
from pprint import pprint
import json
import re
import textwrap

platform = os.name


def listmapglob(p):
    return list(map(os.path.normpath, glob.glob(p, recursive=True)))


def checkMeta(searchnormal, searchother):
    subdirs = []
    if searchnormal:
        subdirs += glob.glob(os.path.join("../custom_volumes", "*/"))
    if searchother:
        subdirs += glob.glob(os.path.join("../custom_volumes_other", "*/"))
    for subdir in subdirs:
        meta_filepath = os.path.join(subdir, "meta.json")
        with open(meta_filepath, "r") as fp:
            meta = json.load(fp)

        # Grab metadata id
        package_id = meta["package_id"]

        dirname = os.path.split(os.path.dirname(subdir))[-1]
        if package_id != dirname:
            print(f"[WARNING]\tPackage {package_id} is in incorrectly named folder {dirname}")


def findNames(rpy):            
    pattern = r"(\n|^)\s*(define|style|transform|image)\s+([^{}=:]+\s*) +(=|:)"
    with open(rpy, "r") as rpyfp:
        lineno = 0
        for line in rpyfp.readlines():
            lineno += 1
            for match in re.finditer(pattern, line):
                __, type, name, __ = match.groups()
                yield (type, name, lineno, line)


def checkNameConflicts():
    global names
    names = {}

    def checkGlobalNames(rpy, ignore=False):
        for type, name, lineno, line in findNames(rpy):
            key = (type, name)
            shortline = textwrap.shorten(line[:-1], width=75)

            if names.get(key) and not ignore:
                conflict = names.get(key)
                (cfile, clineno, cline) = conflict
                print(f"[ERROR]\t[{rpy}:{lineno}] '{shortline}'\n\t{type} '{name}' already defined at \n\t[{cfile}:{clineno}] '{cline}'")
            else:
                names[key] = (rpy, lineno, shortline)

    for rpy in rpy_files_vanilla:
        checkGlobalNames(rpy, ignore=True)

    for rpy in rpy_files_custom:
        checkGlobalNames(rpy)


def checkNameNamespace():
    for rpy in rpy_files_custom_vols:
        for type, name, lineno, line in findNames(rpy):
            shortline = textwrap.shorten(line[:-1], width=75)
            print(f"[WARNING]\t[{rpy}:{lineno}] '{shortline}'\n\t\t{type} '{name}' is not namespaced! Please include a substitution " + r"('{{p}}') to prevent conflicts.")


def writeNameReport():
    with open("report_names.txt", "w") as outfp:
        for rpy in rpy_files:
            for type, name, lineno, line in sorted(findNames(rpy)):
                outfp.write(f"{type} {name}\t[{rpy}:{lineno}]\t{line}")


def main():
    import argparse

    def add_bool_arg(parser, name, default=True, help=None):
        group = parser.add_mutually_exclusive_group(required=False)
        group.add_argument('--' + name, dest=name, action='store_true', help=help)
        group.add_argument('--no-' + name, dest=name, action='store_false', help=help)
        parser.set_defaults(**{name: default})

    ap = argparse.ArgumentParser()
    ap.add_argument(
        '--volumes', nargs="+", default=[],
        help="If set, only look at custom volumes with these IDs."
    )

    ap.add_argument("-d", "--decompiled-at", default="../../pesterquest",
        help="Location of decompiled pesterquest resources (game)")

    # ap.add_argument("-o", "--overwrite", action="store_true",
    #     help="Attempt to automatically correct errors. Experimental!")

    add_bool_arg(ap, "searchnormal", default=True, help="Search in custom_volumes")
    add_bool_arg(ap, "searchother", default=False, help="Search in custom_volumes_other")
    add_bool_arg(ap, "searchvanilla", default=True, help="Search in vanilla pesterquest")
    add_bool_arg(ap, "searchsys", default=True, help="Search in pqms system")

    add_bool_arg(ap, 'checkmeta', help="Verify metadata")
    add_bool_arg(ap, 'checknames', help="Verify names")
    add_bool_arg(ap, 'checkglobals', help="Detect global names")
    add_bool_arg(ap, 'namereport', help="Write summary of names")
    args = ap.parse_args()

    print(args)

    # global overwrite
    # overwrite = args.overwrite

    global rpy_files_custom_vols, rpy_files_custom_sys, rpy_files_vanilla
    global rpy_files_custom, rpy_files

    rpy_files_custom_vols = []
    if args.searchnormal:
        rpy_files_custom_vols += listmapglob("../custom_volumes/**/*.rpy")
    if args.searchother:
        rpy_files_custom_vols += listmapglob("../custom_volumes_other/**/*.rpy")
    rpy_files_custom_sys = listmapglob("sys/**/*.rpy") if args.searchsys else []
    rpy_files_vanilla = listmapglob(os.path.join(args.decompiled_at, "**", "*.rpy")) if args.searchvanilla else []

    if args.volumes:
        rpy_files_custom_vols = list(filter(
            lambda f: any(f"{os.path.sep}{v}{os.path.sep}" in f for v in args.volumes),
            rpy_files_custom_vols
        ))

    rpy_files_custom = rpy_files_custom_vols + rpy_files_custom_sys
    rpy_files = rpy_files_custom + rpy_files_vanilla

    if args.checkmeta:
        checkMeta(args.searchnormal, args.searchother)
    if args.checknames:
        checkNameConflicts()
    if args.checkglobals:
        checkNameNamespace()
    if args.namereport:
        writeNameReport()


if __name__ == "__main__":
    main()
