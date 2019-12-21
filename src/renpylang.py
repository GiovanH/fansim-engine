import re

REGEX_SINGLE_WORD = r"[^\"' )]+"


ATL_KEYWORDS = [
    "as", "at", "behind", "onlayer", "zorder", "show", "expression", "scene", "hide", "with", "window", "call", "jump", "stop", "pause", "play", "menu"
]


def tokenizeString(string):
    import tokenize
    from io import BytesIO
    return tokenize.tokenize(BytesIO(string.encode('utf-8')).readline)


def getDataFromCallstr(callstr):
    import ast
    tree = ast.parse(callstr)

    call = tree.body[0].value

    function_name = call.func.id
    args = [{k: v for k, v in ast.iter_fields(n)} for n in call.args]
    kwargs = {n.arg: {k: v for k, v in ast.iter_fields(n)} for n in ast.walk(call) if isinstance(n, ast.keyword)}

    return function_name, args, kwargs


def findNameDefs(rpy):            
    with open(rpy, "r", encoding="utf-8") as rpyfp:
        lineno = 0
        for line in rpyfp.readlines():
            lineno += 1
            for match in re.finditer(regexDefines(r"[^=:]+\s*"), line, flags=re.MULTILINE):
                __, space, type, name, __ = match.groups()
                yield (type, name, lineno, line)


def findNameUses(rpy):    
    with open(rpy, "r", encoding="utf-8") as rpyfp:
        lineno = 0
        for line in rpyfp.readlines():
            lineno += 1
            for match in re.finditer(regexTransform(), line):
                __, name = match.groups()      
                yield (type, name, lineno, line)


def regexDefines(name=REGEX_SINGLE_WORD):
    """Detects defines, styles, transforms, images, labels
    Groups:
    1. Spacing
    2. Spacing
    3. Type
    4. Name
    5. '='
    """
    return r"(\n|^)(\s*)(define|style|transform|image|label)\s+(" + name + ") *(=|:)" 


def regexImageKwarg(name=REGEX_SINGLE_WORD):
    """Detects image parameters in character definitions and other argument lists
    Groups:
    1. Args before, "
    2. Name
    3. ", args after
    """
    return r"(\(.+image=[\"'])(" + name + ")([\"'].+)"


def regexTransform(name=REGEX_SINGLE_WORD):
    """Detects transforms and names in atl statements
    Groups:
    1. Statement
    2. Name
    """
    return r"\b(" + "|".join(ATL_KEYWORDS) +  ") (" + name + r")\b"


def regexDefinedName(name=REGEX_SINGLE_WORD):
    return r"(\n\s+)" + name + r"(\s+)"


def regexLabel(name=REGEX_SINGLE_WORD):
    return r"(Jump\([\"'])(" + name + r")([\"']\))"


def dialogueToHtml(text):
    tagsubs = [
        (r"{a=jump:([^}]*)}", r"<a href='#\g<1>'>"),  # Jump to tags
        (r"{a=([^}]*)}", r"<a href='\g<1>'>"),  # Web links
        (r"{color=([^}]+)}(.+?){/color}", r"<span style='color: \g<1>;'>\g<2></span>"),
        (r"{font=([^}]+)\..{3,4}}(.+?){/font}", r"<span style='font-family: \g<1>;'>\g<2></span>"),
        (r"(?<!{){([ibusa])}(.+?)({/\1}|(?=\"))", r"<\g<1>>\g<2></\g<1>>"),  # Simple tags
        (r"(?<!{){/{0,1}[^}]+}", r""),  # Unsupported tags
        (r"\\([\"])", r"\g<1>"),
        (r"(?<!\\)\\n", r"<br>"),
        (r"([{[\\])\1", r"\g<1>")  # Escape characters
    ]

    try:
        for (pattern, repl) in tagsubs:
            text = re.sub(pattern, repl, text)
        return text
    except TypeError:
        print('"Text" passed:', repr(text))
        raise


def getDialogueLines(rpy):
    with open(rpy, "r", encoding="utf-8") as fp:
        body = fp.read()
    dialogue_line_regex = r"(?P<indent>^\s*)((jump (?P<jumplabel>.+))|(call ending [a-z]+ \(\"(?P<endcard>.+?)\", (?P<win>.+?),)|(((label )|(\"\[pick\]\s*))(?P<label>(((?<=\\)\")|[^\"\n])+)\"{0,1}.*:\s*$)|(((?P<sayer>[^\"\#\ \:]+)\s+){0,1}([a-zA-Z0-9_]+ )*\"(?P<text>.+?)\"\s*(?P<args>\(.+\)){0,1}$))"
    in_label = False
    for line in re.finditer(dialogue_line_regex, body, flags=re.MULTILINE):
        if line.groupdict().get("label"):
            in_label = True
        if not in_label:
            continue

        if line.groupdict().get("sayer") in (ATL_KEYWORDS + ["play"]):
            continue

        yield line.groupdict()


def getColoredCharacters(rpy):
    for name, args, kwargs in getCharacters(rpy):
        image_node = kwargs.get("image")
        image = image_node.get("value").s if image_node else None
        
        blood_node = kwargs.get("what_color") or kwargs.get("show_blood")
        color = blood_node.get("value").s if blood_node else None
        yield name, image, color


def getCharacters(rpy):
    char_def_regex = r"define (?P<name>[^\"' )]+)\s+=\s+(?P<call>Character\(.+\))"
    with open(rpy, "r", encoding="utf-8") as fp:
        rpy_body = fp.read()

    for chardef in re.finditer(char_def_regex, rpy_body):
        function, args, kwargs = getDataFromCallstr(chardef["call"])
        yield chardef["name"], args, kwargs
