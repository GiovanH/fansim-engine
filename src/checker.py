import os
import glob
from pprint import pprint
import json
import re
import textwrap
import shutil

import renpylang
from patcher import subtableReplace
from fse_mod import Package


platform = os.name

autofix = False


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
        with open(meta_filepath, "r", encoding="utf-8") as fp:
            meta = json.load(fp)

        # Grab metadata id
        package_id = meta["package_id"]

        dirname = os.path.split(os.path.dirname(subdir))[-1]
        if package_id != dirname:
            print(f"[WARNING]\tPackage {package_id} is in incorrectly named folder {dirname}")


def checkStructure(searchnormal, searchother):
    subdirs = []
    if searchnormal:
        subdirs += glob.glob(os.path.join("../custom_volumes", "*/"))
    if searchother:
        subdirs += glob.glob(os.path.join("../custom_volumes_other", "*/"))
    for subdir in subdirs:
        loose_assets = sum([
            glob.glob(os.path.join(subdir, "*.png")),
            glob.glob(os.path.join(subdir, "*.jpg")),
            glob.glob(os.path.join(subdir, "*.mp3")),
            glob.glob(os.path.join(subdir, "*.wav")),
        ], [])
        for asset in loose_assets:
            print(f"[WARNING]\tAsset file {asset} is not in an assets folder! It cannot be accessed.")

        for rpyc in glob.glob(os.path.join(subdir, "*.rpyc")):
            print(f"[WARNING]\tSource file file {asset} is in compiled rpyc form, not rpy, and canont be used.")


def checkNameConflicts():
    global names
    names = {}

    known_undefined_names = set()

    def checkGlobalNames(rpy, ignore=False):
        for type, name, lineno, line in renpylang.findNameDefs(rpy):
            key = (type, name)
            shortline = textwrap.shorten(line[:-1], width=75)

            if name != subtableReplace(name):
                continue

            if names.get(key) and not ignore:
                (cfile, clineno, cline) = names.get(key)
                print(f"[ERROR]\t[{rpy}:{lineno}] '{shortline}'\n\t{type} '{name}' already defined at \n\t[{cfile}:{clineno}] '{cline}'")
            else:
                names[key] = (rpy, lineno, shortline)

    def checkUndefinedNames(rpy):
        pass
        # for type, name, lineno, line in renpylang.findNameUses(rpy):
        #     key = (type, name)
        #     shortline = textwrap.shorten(line[:-1], width=75)
        #     if key not in known_undefined_names:
        #         print(f"[ERROR]\t[{rpy}:{lineno}] '{shortline}'\n\t{type} '{name}' is never defined!")
        #         known_undefined_names.add(key)
            
    for rpy in rpy_files_vanilla:
        checkGlobalNames(rpy, ignore=True)
        checkUndefinedNames(rpy)

    for package in packages:
        for rpy in package.getScriptFiles():
            if package.private:
                checkGlobalNames(rpy)
            checkUndefinedNames(rpy)


def checkNameNamespace():
    for rpy in sum((list(p.getScriptFiles()) for p in packages if p.private), []):
        global_names = []
        for type, name, lineno, line in renpylang.findNameDefs(rpy):
            if subtableReplace(line) == line:
                global_names.append((type, name, lineno, line,))
                shortline = textwrap.shorten(line[:-1], width=75)
                print(f"[WARNING]\t[{rpy}:{lineno}] '{shortline}'\n\t\t{type} '{name}' is not namespaced! Please include a substitution " + r"('{{p}}', '__p__', '!') to prevent conflicts.")
        if autofix:
            i = 1
            bakfilepath = rpy + f".bak"
            while os.path.isfile(bakfilepath):
                i += 1
                bakfilepath = rpy + f".bak{i}"
            shutil.copy2(rpy, bakfilepath)

            with open(rpy, "r", encoding="utf-8") as fp:
                contents = fp.read()

            for type, name, lineno, line in global_names:
                contents = re.sub(
                    renpylang.regexDefines(name),
                    r"\g<1>\g<2>\g<3> __p__" + name + r"\g<5>", contents
                )
                fname = name.split(" ")[0]
                if type == "image":
                    contents = re.sub(
                        renpylang.regexImageKwarg(fname),
                        r"\g<1>__p__" + fname + r"\g<3>", contents
                    )
                if type == "image" or type == "transform":  
                    contents = re.sub(
                        renpylang.regexTransform(fname),
                        r"\g<1> !" + fname, contents
                    )
                if type == "define":
                    contents = re.sub(
                        renpylang.regexDefinedName(fname), 
                        r"\g<1>!\." + fname + r"\g<2>", contents
                    )
                if type == "label":
                    contents = re.sub(
                        renpylang.regexLabel(fname),
                        r"\g<1>__p__" + fname + r"\g<3>", contents
                    )

            with open(rpy, "w", encoding="utf-8") as fp:
                fp.write(contents)

            try:
                import subprocess
                out = subprocess.run(['diff', rpy, bakfilepath], capture_output=True)
                print(out.stdout.decode())
            except FileNotFoundError:
                pass


def writeNameReport():
    with open("report_names.txt", "w", encoding="utf-8") as outfp:
        for rpy in sum((list(p.getScriptFiles()) for p in packages), []):
            for type, name, lineno, line in sorted(renpylang.findNameDefs(rpy)):
                outfp.write(f"{type} {name}\t[{rpy}:{lineno}]\t{line}")


def writeTranscriptions():
    lbrack = "{"
    rbrack = "}"
    char_to_color = {}
    char_to_name = {}
    with open("../transcripts/dynamic_colors.css", "w") as cssfp:
        for rpy in all_rpy_files:
            print(rpy)
            for name, image, color in renpylang.getColoredCharacters(rpy):
                if not (image and color):
                    continue

                for package in packages:
                    if rpy in package.getScriptFiles():
                        name = subtableReplace(name, package.metadata)
                        image = subtableReplace(image, package.metadata)

                if name in char_to_color.keys():
                    continue

                cssfp.write(f"span.{name} {lbrack}\n    color: {color};\n{rbrack}\n")
                char_to_color[name] = color
                char_to_name[name] = image

    def getNameCaption(sayer):
        return char_to_name.get(sayer, sayer).upper()

    for rpy in all_rpy_files:
        dest_dir = os.path.join("../transcripts", os.path.split(os.path.dirname(rpy))[1])
        outpath_base = os.path.join(dest_dir, os.path.basename(rpy))
        print(outpath_base)

        os.makedirs(os.path.join(dest_dir), exist_ok=True)
        txtfp = open(outpath_base + ".txt", "w", encoding="utf-8")
        htmlfp = open(outpath_base + ".htm", "w", encoding="utf-8")
        last_sayer = None
        try:
            txtfp.write(f"# {os.path.basename(rpy)}\n")
            htmlfp.write(f"<link rel='stylesheet' href='../transcript.css' type='text/css'>\n")
            htmlfp.write(f"<link rel='stylesheet' href='../dynamic_colors.css' type='text/css'>\n")
            htmlfp.write(f"<h1>{os.path.basename(rpy)}</h1>\n")

            in_paragraph = False

            for dialogue_line in renpylang.getDialogueLines(rpy):
                indent_level = len(dialogue_line.get("indent")) // 4

                label = dialogue_line.get("label")
                if label:
                    txtfp.write(f"## {label}\n")

                    if in_paragraph:
                        htmlfp.write("</p>")
                        in_paragraph = False
                    htmlfp.write(f"<h3 id='{label}'>{renpylang.dialogueToHtml(label)}</h3>\n")
                    continue

                jumplabel = dialogue_line.get("jumplabel")
                if jumplabel:
                    txtfp.write(f"[Go to {jumplabel}]\n")
                    htmlfp.write(f"<a class='line' href='#{jumplabel}'>Jump to {jumplabel}</a>\n")
                    if in_paragraph:
                        htmlfp.write("</p>")
                        in_paragraph = False
                    continue

                ending = dialogue_line.get("endcard")
                if ending:
                    end_kind = "GOOD END" if dialogue_line.get("win") == "True" else "BAD END"
                    txtfp.write(end_kind + "\n")
                    if in_paragraph:
                        htmlfp.write("</p>")
                        in_paragraph = False
                    htmlfp.write(f"<h3 class='line'>{end_kind}</h3><hr>")
                    continue

                sayer = dialogue_line.get("sayer")
                text = dialogue_line.get("text")
                if sayer != last_sayer:
                    txtfp.write("\n")
                    htmlfp.write("\n")
                    if in_paragraph:
                        htmlfp.write("</p>\n<p>")
                    else:
                        htmlfp.write("<p>")
                        in_paragraph = True
                if sayer:
                    for package in packages:
                        if rpy in package.getScriptFiles():
                            sayer = subtableReplace(sayer, package.metadata)
                    txtfp.write(f"{getNameCaption(sayer)}: {text}\n")
                    htmlfp.write(f"<span class='line'><span class='sayer_label {sayer}'>{getNameCaption(sayer)}: </span><span class='{sayer} dialogue'>{renpylang.dialogueToHtml(text)}</span></span>\n")
                else:
                    txtfp.write(f"{text}\n")
                    htmlfp.write(f"<span class='nosayer dialogue line'>{renpylang.dialogueToHtml(text)}</span>\n")
                last_sayer = sayer

            if in_paragraph:
                htmlfp.write("</p>")
                in_paragraph = False

        finally:
            txtfp.close()
            htmlfp.close()


def main():
    import argparse

    def add_bool_arg(parser, name, default=True, help=None):
        group = parser.add_mutually_exclusive_group(required=False)
        group.add_argument('--' + name, dest=name, action='store_true', help=help + f" (Default: {default})")
        group.add_argument('--no-' + name, dest=name, action='store_false', help=help + f" (Default: {default})")
        parser.set_defaults(**{name: default})

    ap = argparse.ArgumentParser()
    ap.add_argument(
        '--volumes', nargs="+", default=[],
        help="If set, only look at custom volumes with these IDs."
    )

    ap.add_argument(
        "-d", "--decompiled-at", default="../../pesterquest/",
        help="Location of decompiled pesterquest resources (game)")

    # ap.add_argument("-o", "--overwrite", action="store_true",
    #     help="Attempt to automatically correct errors. Experimental!")

    add_bool_arg(ap, "searchnormal", default=True, help="Search in custom_volumes")
    add_bool_arg(ap, "searchother", default=False, help="Search in custom_volumes_other")
    add_bool_arg(ap, "searchvanilla", default=True, help="Search in vanilla pesterquest")
    add_bool_arg(ap, "searchsys", default=True, help="Search in fse system")

    add_bool_arg(ap, 'autofix', help="Attempt to fix errors and warnings", default=False)
    add_bool_arg(ap, 'checkmeta', help="Verify metadata")
    add_bool_arg(ap, 'checknames', help="Verify names")
    add_bool_arg(ap, 'checkstruct', help="Check folder structure")
    add_bool_arg(ap, 'checkglobals', help="Detect global names")
    add_bool_arg(ap, 'namereport', help="Write summary of names")
    add_bool_arg(ap, 'transcribe', help="Write dialog transcriptions")
    args = ap.parse_args()

    print(args)

    global autofix
    autofix = args.autofix

    # global overwrite
    # overwrite = args.overwrite

    global packages, rpy_files_vanilla, all_rpy_files
    packages = []

    if args.searchnormal:
        packages += [Package(p) for p in glob.glob("../custom_volumes/*/")]
    if args.searchother:
        packages += [Package(p) for p in glob.glob("../custom_volumes_other/*/")]

    rpy_files_vanilla = glob.glob(os.path.join(args.decompiled_at, "**", "*.rpy"), recursive=True) if args.searchvanilla else []

    if args.volumes:
        packages = list(filter(
            lambda p: p.id in args.volumes,
            packages
        ))

    all_rpy_files = sum((list(p.getScriptFiles()) for p in packages), rpy_files_vanilla)

    if args.checkmeta:
        checkMeta(args.searchnormal, args.searchother)
    if args.checkstruct:
        checkStructure(args.searchnormal, args.searchother)
    if args.checknames:
        checkNameConflicts()
    if args.checkglobals:
        checkNameNamespace()
    if args.namereport:
        writeNameReport()
    if args.transcribe:
        writeTranscriptions()


if __name__ == "__main__":
    main()
