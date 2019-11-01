#!/bin/python3

import subprocess
import os
import shutil
import glob
from distutils.dir_util import copy_tree
import json

gamedir_root = "C:/Program Files (x86)/Steam/steamapps/common/Homestuck Pesterquest"
executable = "pesterquest.exe"
outdir = "./pesterquest"
rpatool = "./rpatool/rpatool"

gamedir = os.path.normpath(os.path.join(gamedir_root, "game"))


def _doFileOp(op, source, destination, quiet=False):
    try:
        result = op(source, destination)
        if not quiet:
            print("{} --> {}".format(source, destination))
        return result
    except Exception:
        if not quiet:
            print("{} -x> {}".format(source, destination))
        raise


def mergeDirIntoDir(src, dst):
    copy_tree(src, dst, update=True)


def copyFileToFile(src, dst):
    assert os.path.isfile(src)
    assert not os.path.isfile(dst)
    return _doFileOp(shutil.copy2, src, dst)


def copyFileToDir(src, dst, asfile=None):
    if asfile:
        src_dir, src_filename = os.path.split(src)
        dst_path = os.path.join(dst, asfile)
        return copyFileToFile(src, dst_path)
    else:
        assert os.path.isdir(dst)
        assert os.path.isfile(src)
        return _doFileOp(shutil.copy2, src, dst)


warn = False

print("\nClearing old scripts")
for rpy in glob.glob(os.path.join(gamedir, "custom*.rpy*")):
    print(f"{rpy} --> [X]")
    os.unlink(rpy)

all_volumes = []

print("\nCopying user scripts")
sysdir = os.path.join(".", "sys/")

for subdir in [sysdir] + glob.glob(os.path.join("custom_volumes", "*/")):
    print()
    try:
        meta_filepath = os.path.join(subdir, "meta.json")
        with open(meta_filepath, "r") as fp:
            meta = json.load(fp)

        meta_id = meta["id"]
        all_volumes += meta["volumes"]
    except FileNotFoundError:
        print(f"[ERROR] Missing configuration file {meta_filepath}, required!")
        warn = True
        continue
    except KeyError as e:
        print(f"[ERROR] {meta_filepath} missing required key '{e.args[0]}'!")
        warn = True
        continue

    prefix = ("" if (subdir == sysdir) else "_vol")
    print(f"Detected package {meta_id} at {subdir}")

    for rpy in glob.glob(os.path.join(subdir, "*.rpy")):
        __, filename = os.path.split(rpy)
        destfile = os.path.join(gamedir, f"custom{prefix}_{meta_id}_{filename}")
        copyFileToFile(rpy, destfile)

    assets_dir = os.path.join(subdir, "assets")
    if os.path.isdir(assets_dir):
        destdir = os.path.join(gamedir, f"custom_assets_{meta_id}")
        mergeDirIntoDir(assets_dir, destdir)

    assets_common_dir = os.path.join(subdir, "assets_common")
    if os.path.isdir(assets_common_dir):
        destdir = os.path.join(gamedir, f"custom_assets")
        mergeDirIntoDir(assets_common_dir, destdir)

print("\nCompiling volumes")

with open("vol_select_custom_template.rpy", "r") as fp:
    template_data = fp.read() 

for volume in all_volumes:
    print("Volume:", volume["title"], volume["subtitle"], volume["entrypoint"])
    tileid = volume["tileid"]
    assert os.path.isfile(os.path.join(gamedir, "custom_assets", f"volumeselect_{tileid}_idle.png"))
    assert os.path.isfile(os.path.join(gamedir, "custom_assets", f"volumeselect_{tileid}_small_idle.png"))

    new_entry = f"""
                imagebutton idle "custom_assets/volumeselect_{tileid}_small.png" action Jump("{volume['entrypoint']}") hovered[
                    SetScreenVariable("icon", "custom_assets/volumeselect_{tileid}.png"), 
                    SetScreenVariable("title", "{volume['title']}"), 
                    SetScreenVariable("subtitle", "{volume['subtitle']}")
                ] unhovered[
                    SetScreenVariable("icon", "gui/volumeselect_icon_blank.png"), 
                    SetScreenVariable("title", "Volume Select"), 
                    SetScreenVariable("subtitle", "Hover over an icon!")
                ] alt "you know what it be"
    """

    template_data = template_data.replace("{{}}", new_entry + "{{}}")

template_data = template_data.replace("{{}}", "")        
with open(os.path.join(gamedir, "custom_volumeselect.rpy"), 'w') as fp:
    fp.write(template_data)

if warn:
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Errors occured. Please review this window and then press enter to quit.")
    input()

print(f"Starting {executable}")
subprocess.run(os.path.join(gamedir_root, executable))
