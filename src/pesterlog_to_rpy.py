import argparse
import re
import textwrap


preamble = """label {{package_entrypoint}}_route:

    # Menu boilerplate: Exit main menu, fade to black
    $ renpy.block_rollback()
    $ main_menu = False
    show image "gui/game_menu.png"
    window hide
    scene black with Dissolve(1.0)
    show blackcover
    $ quick_menu = True
    scene bg black
\n"""

aliases = {}
introposes = {}
prev_sayer = ""

sayer_to_name = {}

sayer_positions = ["default", "left1280", "right1280"]
recent_sayers = set()


def dialogEscape(text):
    return text.replace("\"", "\\\"").replace("\n", "")


def aliasGet(match, key):
    value = match.groupdict()[key]
    return aliases.get(value, value)


def rpy_line(line):
    global prev_sayer
    pattern = r"(?P<sayer>^[^:]+): (?P<text>.*)"

    match = re.match(pattern, line)
    assert match 

    sayer = match.groupdict()["sayer"]
    text = match.groupdict()["text"]

    sayer = aliases.get(sayer, sayer)
    text = aliases.get(text, text)

    recent_sayers.add(sayer)

    if args.use_speaking:
        if prev_sayer != sayer:
            if prev_sayer: 
                yield f"show {sayer_to_name[prev_sayer]} at stopspeaking"
                yield ""
            yield f"show {sayer_to_name[sayer]} at speaking"
    else:
        yield ""
    prev_sayer = sayer

    yield f'{sayer} "{dialogEscape(text)}"\n'


def rpy_begin_chat(line):
    pattern = r"^(?P<name1>[^ ]+) \[(?P<id1>[^\]]+)\] began [A-Za-z]+ (?P<name2>[^ ]+) \[(?P<id2>[^\]]+)\]"

    match = re.match(pattern, line)
    assert match 

    name1 = aliasGet(match, "name1")
    name2 = aliasGet(match, "name2")

    sayer_to_name[aliasGet(match, "id1")] = name1
    sayer_to_name[aliasGet(match, "id2")] = name2

    print(sayer_to_name)

    yield f'"{dialogEscape(line)}"'
    yield f'show {name1} {introposes[name1]} at left1280 with moveinbottom' 
    yield f'show {name2} {introposes[name2]} at right1280 with moveinbottom'


def rpy_end_chat(line):
    pattern = r"^(?P<name1>[^ ]+) \[(?P<id1>[^\]]+)\] ceased [A-Za-z]+ (?P<name2>[^ ]+) \[(?P<id2>[^\]]+)\]"

    match = re.match(pattern, line)
    assert match 

    name1 = aliasGet(match, "name1")
    name2 = aliasGet(match, "name2")

    id1 = aliasGet(match, "id1")
    id2 = aliasGet(match, "id2")

    sayer_to_name[id1] = name1
    sayer_to_name[id2] = name2

    print(sayer_to_name)

    if prev_sayer:
        yield f"show {sayer_to_name[prev_sayer]} at stopspeaking"

    yield f'hide {name1} with moveoutbottom' 
    recent_sayers.remove(id1)
    yield f'hide {name2} with moveoutbottom'
    recent_sayers.remove(id2)
    yield f'"{dialogEscape(line)}"'


def rpy__cleanup():
    yield ""
    for sayer in recent_sayers:
        try:
            name = sayer_to_name[sayer]
            yield f"hide {name} with moveoutright"
        except KeyError:
            print(f"Sayer id '{sayer}' not in")
            print(sayer_to_name)
    yield ""


def rpy_fail(line):
    print("Can't recognize line!")
    print(repr(line))
    yield f"# {line}"


def main():
    global args

    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="out.rpy")
    ap.add_argument("--in", dest="infile", default="pesterlog.txt")
    ap.add_argument("--alias", default=[], nargs="+")
    ap.add_argument("--introposes", default=[], nargs="+")
    ap.add_argument("--use-speaking", action="store_true")
    args = ap.parse_args()

    for aline in args.alias:
        key, value = aline.split("=")
        aliases[key] = value
    for aline in args.introposes:
        key, value = aline.split("=")
        introposes[key] = value

    outfile = open(args.out, "w")
    outfile.write(preamble)

    rpy_functions = [
        rpy_line,
        rpy_begin_chat,
        rpy_end_chat,
        rpy_fail
    ]

    with open(args.infile, "r") as fp:
        for line in fp.readlines():
            if not line.strip():
                outfile.write("\n")
                continue
            for function in rpy_functions:
                try:
                    out = function(line)
                    outfile.write(textwrap.indent("\n".join(out), " " * 4))
                    break
                except AssertionError:
                    continue
    outfile.write(textwrap.indent("\n".join(rpy__cleanup()), " " * 4))
    outfile.close()


main()
