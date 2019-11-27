import glob
import subprocess
import os
import re


blood_data = {
    "??????": ("gold", "#a1a100"),
    "AMISIA": ("blue", "#000056"),
    "ARDATA": ("cobalt", "#005682"),
    "AZDAJA": ("gold", "#a1a100"),
    "BAIZLI": ("purple", "#2b0057"),
    "BARZUM": ("purple", "#2b0057"),
    "BOLDIR": ("olive", "#416600"),
    "CHARUN": ("olive", "#416600"),
    "BRONYA": ("jade", "#0aa85b"),
    "CHAHUT": ("purple", "#2b0057"),
    "CHIXIE": ("bronze", "#bb6405"),
    "CIRAVA": ("gold", "#a1a100"),
    "DARAYA": ("jade", "#0aa85b"),
    "WANSHI": ("jade", "#0aa85b"),
    "ELWURD": ("cobalt", "#005682"),
    "FOLYKL": ("gold", "#a1a100"),
    "FOLYKLKUPRUM": ("gold", "#a1a100"),
    "GALEKH": ("blue", "#000056"),
    "JOURNO": ("teal", "#008282"),
    "TEGIRI": ("teal", "#008282"),
    "KARAKO": ("purple", "#2b0057"),
    "KONYYL": ("olive", "#416600"),
    "KUPRUM": ("gold", "#a1a100"),
    "LANQUE": ("jade", "#0aa85b"),
    "LYNERA": ("jade", "#0aa85b"),
    "MALLEK": ("cobalt", "#005682"),
    "MALLEK": ("teal", "#008282"),
    "DIEMEN": ("rust", "#a20000"),
    "FOZZER": ("rust", "#a20000"),
    "MARSTI": ("rust", "#a20000"),
    "MARVUS": ("purple", "#2b0057"),
    "POLYPA": ("olive", "#416600"),
    "REMELE": ("cobalt", "#005682"),
    "SKYLLA": ("bronze", "#bb6405"),
    "SMUGGLER": ("cobalt", "#005682"),
    "STELSA": ("teal", "#008282"),
    "TAGORA & TYZIAS": ("teal2", "#008282"),
    "TAGORA": ("teal", "#008282"),
    "TYZIAS": ("teal", "#008282"),
    "TIRONA": ("teal", "#008282"),
    "VIKARE": ("bronze", "#bb6405"),
    "ZEBEDE": ("gold", "#a1a100"),
    "ZEBRUH": ("blue", "#000056"),
    "NIKHEE": ("blue", "#000056"),
}

char_kwargs = {
}


char_exdata = {
    "DIEMEN": r"""
init python:
    quirks["diemen"] = [("(.+)", "(| \g<1> |)")]
""",
    "AZDAJA": r"""
init python:
    quirks["azdaja"] = [("(.+)", "||| \g<1> |||")]
""",
    "AMISIA": r"""
init python:
    quirks["amisia"] = [("u", "uu")]
""",
    "TAGORA": r"""
init python:
    quirks["tagora"] = [("(.+)", "<1>\n\n*__________")]
""",
    "POLYPA": r"""
init python:
    quirks["polypa"] = [("(.+)", "<1> *|")]
""",
    "ZEBRUH": r"""
init python:
    quirks["zebruh_hearts"] = [("(.+)", "{image=char heart} \g<1> {image=char heart}")]
    quirks["zebruh_diamonds"] = [("(.+)", "{image=char diamond} \g<1> {image=char diamond}")]
    quirks["zebruh_clubs"] = [("(.+)", "{image=char club} \g<1> {image=char club}")]
    quirks["zebruh_spades"] = [("(.+)", "{image=char spade} \g<1> {image=char spade}")]
""",
}

char_extests = {
    "ZEBRUH": """
    $ quirkSay(zebruh, "zebruh_hearts", "Hearts")
    $ quirkSay(zebruh, "zebruh_spades", "Spades")
    $ quirkSay(zebruh, "zebruh_diamonds", "Diamonds")
    $ quirkSay(zebruh, "zebruh_clubs", "Clubs")
"""
}

talksprites = glob.glob("assets/sprite/*.*")

characters = set(
    os.path.split(talksprite)[1].split("_")[0].lower()
    for talksprite in talksprites
)

routefp = open("route.rpy", "w")
routefp.write("""
label {{package_entrypoint}}_route:
    # Menu boilerplate: Exit main menu, fade to black
    $ renpy.block_rollback()
    $ main_menu = False
    show image "gui/game_menu.png"
    window hide
    scene black with Dissolve(1.0)
    show blackcover
    $ quick_menu = True
    scene bg alternia4
""")

for character in characters:
    with open(f"{character}.rpy", "w") as charfp:
        try:
            guicolor, outlines = blood_data[character.upper()]
        except:
            print("Don't know character", character)
            continue
        define = f'define {character.lower()} = Character(name="{character.upper()}", kind=hiveswap, image="{character}", window_background="gui/textbox_{guicolor}.png", who_outlines=[(4, "{outlines}")])\n\n'

        charfp.write(define)
        for charsprite in glob.glob(f"assets/sprite/{character}_*.*"):
            filedir, filename = os.path.split(charsprite)
            charname, *rest = filename.split("_")
            charname = charname.lower()
            rest = "_".join(rest)
            pose = os.path.splitext(rest)[0]
            # print(charname, rest)

            kwargs = char_kwargs.get(charname, ", ypos=730")

            imgpath = charsprite.replace("assets/", "{{assets}}/").replace("\\", "/")
            image = f'image {charname} {pose} = Image("{imgpath}"{kwargs})\n'
            charfp.write(image)

        charfp.write(char_exdata.get(character.upper(), ""))
        charfp.close()
        routefp.write(f"\n    $ debug_dump_character({character.lower()})")

routefp.write("""
    call ending pass ("gui/game_menu.png", True, True)
    return
""")

routefp.close()

with open(f"backgrounds.rpy", "w") as bgfp:   
    for file in glob.glob(f"assets/bg/*.*"):
        filedir, filename = os.path.split(file)
        filename, fileext = os.path.splitext(filename)
        imgpath = file.replace("assets/", "{{assets}}/").replace("\\", "/")
        bgfp.write(f'image bg {filename} = Image("{imgpath}")\n')

with open(f"objects.rpy", "w") as bgfp:   
    for file in glob.glob(f"assets/object/*.*"):
        filedir, filename = os.path.split(file)
        filename, fileext = os.path.splitext(filename)
        imgpath = file.replace("assets/", "{{assets}}/").replace("\\", "/")
        bgfp.write(f'image {filename} = Image("{imgpath}")\n')

with open(f"effects.rpy", "w") as bgfp:   
    for file in glob.glob(f"assets/object/*.*"):
        filedir, filename = os.path.split(file)
        filename, fileext = os.path.splitext(filename)
        imgpath = file.replace("assets/", "{{assets}}/").replace("\\", "/")
        bgfp.write(f'image fx {filename} = Image("{imgpath}")\n')

with open(f"text.rpy", "w") as bgfp:   
    for file in glob.glob(f"assets/text/*.*"):
        filedir, filename = os.path.split(file)
        filename, fileext = os.path.splitext(filename)
        imgpath = file.replace("assets/", "{{assets}}/").replace("\\", "/")
        bgfp.write(f'image char {filename} = Image("{imgpath}")\n')
