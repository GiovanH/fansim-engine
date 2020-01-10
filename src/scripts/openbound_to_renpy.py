#!/bin/python3

import os
from glob import glob
import bs4
import traceback
from pprint import pprint
from PIL import Image   # Image IO libraries
import subprocess
import contextlib
import sys

globstr = "Openbound/openbound-part*/**/*.xml"

xml_files = glob(globstr, recursive=True)
# print(xml_files)

animations = {}
poses = []
assets = {}
resources = {}

char_animations = {}

blood = {
    "aradia": "#a10000",
    "aranea": "#005682",
    "cronus": "#6a006a",
    "damara": "#a10000",
    "dave": "#e00707",
    "gamzee": "#2b0057",
    "horuss": "#000056",
    "kanaya": "#008141",
    "kanaya2": "#008141",
    "kankri": "#ff0000",
    "karkat": "#626262",
    "kurloz": "#2b0057",
    "latula": "#008282",
    "meenah": "#77003c",
    "mituna": "#a1a100",
    "porrim": "#008141",
    "dirk": "#f2a400",
    "squarewave": "#000000",
    "rose": "#b536da",
    "rufioh": "#000000",
    "terezi": "#008282",
}

# for xml_file in xml_files:
#     with open(xml_file, encoding='utf-8') as file:
#         b = bs4.BeautifulSoup(file, features="html.parser")
#         for asset in b.find_all("asset", type="graphic"):
#             assets[asset.get('name')] = asset
#             if "RoomBG" in asset.get('name') or "RoomFG" in asset.get('name'):
#                 continue
#             poses.append("ob_" + asset.get('name').replace("_", " "))
#         for animation in b.find_all("animation"):
#             name = animation.get('sheet')
#             length = int(animation.get("length", 0))
#             if name and length:    
#                 animations.append(("ob_" + asset.get('name').replace("_", " "), length,))

for xml_file in xml_files:
    with open(xml_file, encoding='utf-8') as file:
        b = bs4.BeautifulSoup(file, features="html.parser")
        for asset in b.find_all("asset", type="graphic"):
            name = asset.get('name')
            if name:
                assets[name] = asset

                base, __, subbase, *__ = xml_file.split(os.path.sep)
                prefix = base + os.path.sep + "resources"
                if subbase.find("openbound") > -1:
                    prefix += os.path.sep + subbase
                resources[name] = prefix + os.path.sep + asset.text
                # asset.text = 
                
        for dialogsprites in b.find_all("dialogsprites"):
            for animation in dialogsprites.find_all("animation"):
                charname = animation.get("name").split("_")[0]
                char_animations[charname] = char_animations.get(charname, []) + [animation]

        for sprite in b.find_all("sprite"):
            for animation in sprite.find_all("animation"):
                charname = animation.get("name")
                char_animations[charname] = char_animations.get(charname, []) + [animation]

for charname, animations in char_animations.items():
    for animation in animations:
        key = animation.get("sheet")
        try:
            asset = assets[key]
            resource = resources[key]
        except KeyError:
            print("No resource", key)
            continue

        if animation.get('length'):
            length = int(animation['length'])
        else:
            length = 1
        if length <= 1:
            continue

        filedir, filename = os.path.split(asset.text)
        outdir = os.path.join("sliced", filedir)
        os.makedirs(outdir, exist_ok=True)
        filenamep, ext = os.path.splitext(filename)

        print(key, asset.text, resource, outdir)

        if len(glob(os.path.join(outdir, filenamep + "-*" + ext))) < 1:

            image = Image.open(resource)

            colsize = animation.get('colsize')
            rowsize = animation.get('rowsize')

            print()
            print(resource, animation, colsize, rowsize)

            if not colsize:
                colsize = int(image.width / length)
            if not rowsize:
                rowsize = image.height

            command = [
                "magick", 
                "convert",
                os.path.relpath(resource).replace("\\", "/"),
                "-crop", "{}x{}".format(colsize, rowsize),
                filename
            ]
            print(" ".join(command))
            result = subprocess.run(command, capture_output=True, check=False)
            if len(result.stderr) + len(result.stdout) > 0:
                print(*((c if c.count(" ") == 0 else '"{c}"'.format(c=c)) for c in command))
                # print("OUT:", bytes(result.stdout).decode("unicode_escape"))
                print("ERR:", bytes(result.stderr).decode("unicode_escape"))
                raise subprocess.CalledProcessError(result.returncode, command, result)

            command = ["mv", "-v", filenamep + "*" + ext, outdir]
            print(" ".join(command))
            result = subprocess.run(command, capture_output=True, check=False)
        else:
            print("Skipping", key)


for key, asset in assets.items():
    poses.append(("ob_" + asset.get('name').replace("_", " "), asset.text, key))

def imageify(asset):
    return "Image(\"{{assets}}/" + asset + f"\", yoffset=-197, xanchor=240, yalign=1.0)"

for character, animations in char_animations.items():
    if not character:
        continue
    with open(f"{character}.rpy", "w") as fp:
        with contextlib.redirect_stdout(fp):

            try:
                blood_clr = blood[character]
            except KeyError:
                continue
            print(f'define ob_{character} = Character(name="{character.capitalize()}", show_color="{blood_clr}", kind=openbound, image="ob_{character}")')

            for animation in animations:
                key = animation.get("sheet")
                try:
                    asset = assets[key].text
                    print("image ob_" + key.replace("_", " ") + " = " + imageify(asset))
                except KeyError:
                    continue

            for animation in animations:
                key = animation.get("sheet")
                try:
                    asset = assets[key]
                    resource = resources[key]
                except KeyError:
                    continue

                renpy_name = "ob_" + key.replace("_", " ")

                if animation.get('length'):
                    length = int(animation['length'])
                else:
                    length = 1
                if length <= 1:
                    continue
                    
                print(f"image {renpy_name}:")
                for i in range(length):
                    filename, ext = os.path.splitext(asset.text)
                    newfile = filename + f"-{i}" + ext
                    print("    " + imageify(newfile))
                    print("    pause 0.1")
                print("    repeat")
                poses.append((renpy_name, None, None))


with open(f"extras.log", "w") as fp:
    for character, animations in char_animations.items():
        with contextlib.redirect_stdout(fp):

            for animation in animations:
                key = animation.get("sheet")
                try:
                    asset = assets[key]
                    resource = resources[key]
                except KeyError:
                    continue

                renpy_name = "ob_" + key.replace("_", " ")

                if animation.get('length'):
                    length = int(animation['length'])
                else:
                    length = 1
                if length <= 1:
                    continue

                print(f"rm -v {asset.text}")

with open("openbound.rpy", "w") as fp:
    with contextlib.redirect_stdout(fp):

        print("""
# Start of route
label {{package_entrypoint}}_route:

    # Menu boilerplate: Exit main menu, fade to black
    $ renpy.block_rollback()
    $ main_menu = False
    show image "gui/game_menu.png"
    window hide
    scene black with Dissolve(1.0)
    show blackcover
    $ quick_menu = True

    # Set the scene, fade in from black
    scene bg alternia4
    play music "music/WORST_END.wav" loop
    hide blackcover with dissolve
""")
        for character, animations in char_animations.items():
            print(f"    show ob_{character} idle")
            for animation in animations:
                key = animation.get("sheet")
                print(f"    ob_{key.replace('_', ' ')} \"{key}\"")
            print(f"    hide ob_{character}\n")
