import glob
import bs4
import os
import re
import textwrap

def dialogEscape(text):
    return (
        text.replace("\\", "\\\\")
        .replace("\"", "\\\"")
        .replace("\n", "")
        .replace("[", "[[")
    )

globstr = "Openbound/openbound-part*/**/*.xml"

xml_files = glob.glob(globstr, recursive=True)


def writeDialogBlock(rpy, action):
    parser = r"@(?P<sayer>[^: _]+)(?P<pose>[^: ~%]+){0,1}([~%][^ ]+){0,1}(?P<tags>:[^ ]*){0,1} ([A-Z]+: ){0,1}(?P<dialogue>.+)$"
    rpy.write(f"label {action.get('class')[0]}:\n")
    for line in action.text.split("\n"):
        match = re.search(parser, line)
        if not match:
            print(f"{line}")
            continue
        sayer, pose, notes, tags, __, dialogue = match.groups()
        sayer = f"ob_{sayer}" if (sayer and sayer != "!") else "narrator"
        pose = " " + pose[1:] if pose else ""
        tags = f' (show_hashtags="{tags[1:]}")' if tags else ""
        notes = f" #{notes}" if notes else""
        rpy.write(f'    {sayer}{pose} "{dialogEscape(dialogue)}"{tags}{notes}\n')



for xmlpath in xml_files:
    __, filename = os.path.split(xmlpath)
    name, __ = os.path.splitext(filename)

    with open(xmlpath, encoding='utf-8') as xmlfile:
        b = bs4.BeautifulSoup(xmlfile, features="html.parser")
        actions = b.find_all("action", class_=True)
    if actions:
        with open(f"{name}.rpy", "w", encoding="utf-8") as rpy:
            for action in actions:
                writeDialogBlock(rpy, action)

