import re

REGEX_SINGLE_WORD = r"[^\"' )]+"


def findNameDefs(rpy):            
    pattern = r"(\n|^)(\s*)(define|style|transform|image|label)\s+([^=:]+\s*) *(=|:)"
    with open(rpy, "r", encoding="utf-8") as rpyfp:
        lineno = 0
        for line in rpyfp.readlines():
            lineno += 1
            for match in re.finditer(pattern, line):
                __, space, type, name, __ = match.groups()
                yield (type, name, lineno, line)


def findNameUses(rpy):            
    raise NotImplementedError


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
    return r"\b(as|at|behind|onlayer|zorder|show|expression|scene|hide|with|window|call|jump|stop|pause|play|menu) " + name + r"\b"


def regexDefinedName(name=REGEX_SINGLE_WORD):
    return r"(\n\s+)" + name + r"(\s+)"


def regexLabel(name=REGEX_SINGLE_WORD):
    return r"(Jump\([\"'])(" + name + r")([\"']\))"
