import argparse
import re
import textwrap


preamble = """label {{package_entrypoint}}_route:
    $ renpy.block_rollback()
    $ main_menu = False
    show image "gui/game_menu.png"
    window hide
    scene black with Dissolve(1.0)
    show blackcover
    $ quick_menu = True
    scene bg black
\n"""

sayeraliases = {}
namealiases = {}
introposes = {}
prev_sayer = ""

sayer_to_name = {}

sayer_positions = ["default", "left1280", "right1280"]
recent_sayers = set()
all_sayers = set()
all_names = set()


def dialogEscape(text):
    return text.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", "")


def aliasGetN(match, key):
    value = match.groupdict()[key]
    return namealiases.get(value, value)


def aliasGetS(match, key):
    value = match.groupdict()[key]
    return sayeraliases.get(value, value)

# Generic line say


def rpy_line(line):
    global prev_sayer
    pattern = r"(?P<sayer>^[^:]+): (?P<text>.*)"

    match = re.match(pattern, line)
    assert match

    text = match.groupdict()["text"]
    sayer = aliasGetS(match, "sayer")

    if sayer not in recent_sayers:
        yield rpy_do_enter(sayer_to_name.get(sayer, sayer), sayer)

    if prev_sayer != sayer:
        if args.use_speaking:
            if prev_sayer:
                yield f"show {sayer_to_name.get(prev_sayer, prev_sayer)} at stopspeaking"
                yield ""
            yield f"show {sayer_to_name.get(sayer, sayer)} at speaking"
        else:
            yield ""
    prev_sayer = sayer

    all_sayers.add(sayer)
    yield f'{sayer} "{dialogEscape(text)}"\n'

# Chats


def rpy_begin_chat(line):
    pattern = r"(?P<name1>[^ ]+) \[(?P<id1>[^\]]+)\] began [A-Za-z]+ (?P<name2>[^ ]+) \[(?P<id2>[^\]]+)\]"

    match = re.match(pattern, line)
    assert match

    name1 = aliasGetN(match, "name1")
    name2 = aliasGetN(match, "name2")

    id1 = aliasGetS(match, "id1")
    id2 = aliasGetS(match, "id2")

    sayer_to_name[id1] = name1
    sayer_to_name[id2] = name2

    yield f'"{dialogEscape(line)}"'
    yield rpy_do_enter(name1, id1, "left1280")
    yield rpy_do_enter(name2, id2, "right1280")


def rpy_end_chat(line):
    pattern = r"^(?P<name1>[^ ]+) \[(?P<id1>[^\]]+)\] ceased [A-Za-z]+ (?P<name2>[^ ]+) \[(?P<id2>[^\]]+)\]"

    match = re.match(pattern, line)
    assert match

    name1 = aliasGetN(match, "name1")
    name2 = aliasGetN(match, "name2")

    id1 = aliasGetS(match, "id1")
    id2 = aliasGetS(match, "id2")

    sayer_to_name[id1] = name1
    sayer_to_name[id2] = name2

    print(sayer_to_name)

    yield rpy_do_exit(name1, id1)
    yield rpy_do_exit(name2, id2)

    yield f'"{dialogEscape(line)}"'


# Memos

def rpy_begin_memo(line):
    pattern = r"^[A-Z]+ (?P<name>[^ ]+) \[(?P<id>[^\]]+)\] [A-Z ]+ opened memo on board (?P<memoname>.+)\."

    match = re.match(pattern, line)
    assert match

    name = aliasGetN(match, "name")
    id = aliasGetS(match, "id")
    sayer_to_name[id] = name

    print(sayer_to_name)

    yield f'"{dialogEscape(line)}"'
    yield rpy_do_enter(name, id)


def rpy_join_memo(line):
    pattern = r"^[A-Z]+ (?P<name>[^ ]+)( [0-9]+){0,1} \[(?P<id>[^\]]+)\] [:0-9A-Z ]+ responded to memo"

    match = re.match(pattern, line)
    assert match

    name = aliasGetN(match, "name")
    id = aliasGetS(match, "id")
    sayer_to_name[id] = name

    yield f'"{dialogEscape(line)}"'
    yield rpy_do_enter(name, id)
    yield ""


def rpy_memo_ban(line):
    pattern = r"^(?P<id1>[^ ]+) (?P<un>un){0,1}(banned) ((?P<id2>[A-Z0-9]+)|((?P<self>her|him|them)self)) from responding.+"

    match = re.match(pattern, line)
    assert match

    id1 = aliasGetS(match, "id1")

    yield ""
    yield f'"{dialogEscape(line)}"'

    if match.groupdict()["self"]:
        id2 = id1
    else:
        id2 = aliasGetS(match, "id2")

    name = sayer_to_name.get(id2, id2)
    if match.groupdict()["un"]:
        yield rpy_do_enter(name, id2)
    else:
        yield rpy_do_exit(name, id2)
    yield ""


def rpy_memo_leave(line):
    pattern = r"^(?P<id>[^ ]+) ceased responding to memo."

    match = re.match(pattern, line)
    assert match

    id = aliasGetS(match, "id")
    name = sayer_to_name.get(id, id)

    yield f'"{dialogEscape(line)}"'
    yield rpy_do_exit(name, id)
    yield ""


def rpy_memo_close(line):
    pattern = r"^(?P<id>[^ ]+) closed memo."

    match = re.match(pattern, line)
    assert match

    id = aliasGetS(match, "id")
    name = sayer_to_name.get(id, id)

    yield f'"{dialogEscape(line)}"'
    yield rpy_do_exit(name, id)
    for l in rpy__cleanup():
        yield l


def rpy__cleanup():
    yield ""
    for sayer in list(recent_sayers):
        try:
            name = sayer_to_name.get(sayer, sayer)
            yield rpy_do_exit(name, sayer)
        except KeyError:
            print(f"Sayer id '{sayer}' not in")
            print(sayer_to_name)
    yield ""


def rpy_do_exit(name, id):
    if id in recent_sayers:
        recent_sayers.remove(id)

    out = f"hide {name} with moveoutbottom"

    if args.use_speaking:
        global prev_sayer
        if prev_sayer and id == prev_sayer:
            out = f"show {name} at stopspeaking\n" + out
            prev_sayer = ""

    return out


def rpy_do_enter(name, id, at="default"):
    recent_sayers.add(id)
    all_names.add(name)
    all_sayers.add(id)
    return f'show {name} {introposes.get(name, "neutral")} at {at} with moveinbottom'


def rpy_fail(line):
    print("Can't recognize line:", repr(line))
    yield f"# {line}"


def main():
    global args

    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="out.rpy")
    ap.add_argument("--in", dest="infile", default="pesterlog.txt")
    ap.add_argument("--namealias", default=[], nargs="+")
    ap.add_argument("--initialalias", default=[], nargs="+")
    ap.add_argument("--introposes", default=[], nargs="+")
    ap.add_argument("--use-speaking", action="store_true")
    args = ap.parse_args()

    for aline in args.namealias:
        key, value = aline.split("=")
        namealiases[key] = value
    for aline in args.initialalias:
        key, value = aline.split("=")
        sayeraliases[key] = value
    for aline in args.introposes:
        key, value = aline.split("=")
        introposes[key] = value

    outfile = open(args.out, "w")
    outfile.write(preamble)

    rpy_functions = [
        rpy_line,
        rpy_begin_chat,
        rpy_end_chat,
        rpy_begin_memo,
        rpy_join_memo,
        rpy_memo_ban,
        rpy_memo_leave,
        rpy_memo_close,
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

    for name, val in [
        ("All names", all_names),
        ("All sayers", all_sayers)
    ]:
        outfile.write(f"\n\n# {name}: \n# - " + " \n# - ".join(val))

    outfile.close()


main()
