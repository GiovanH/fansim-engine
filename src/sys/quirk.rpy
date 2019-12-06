"""
Automatic quirk translation subsystem

This provides functions to help you with quirks!

Using quirks:
# Approach 1: Call quirksay
# Arguments are sayer (character), quirk name, text
$ quirkSay(gam, "gamzee", "Quirk formatting 1")

# Approach 2: Define a new sayer
# Define a new character, given an existing character and a quirk
# New sayer is reusable!
$ __p__gamq = quirkSayer(gam, "gamzee")
__p__gamq "Quirk formatting 2"
__p__gamq "Quirk formatting 2 forever"

# Approach 3
# You can quirk format text without saying it directly
$ gam(quirkSub("gamzee", "Quirk formatting 3") + " and I guess other stuff")
    

Writing quirks:

Each quirk has a name (key) and a series of regex rules (value).
When the quirk is applied to a string, each regex replacement is applied.
The regex replacements are in the form (pattern, repl) as tuples.
In python regex, \g<1> in a replacement substitues matching grouup 1, etc.

To add a quirk, set a quirk value in a python block.

init python:
    quirks["amisia"] = [("u", "uu")]

init python:
    quirks["diemen"] = [("(.+)", "(| \g<1> |)")]

You can also use inline python, if you wish. 

    $ quirks["azdaja"] = [("(.+)", "||| \g<1> |||")]

"""


init offset = 0

# Automatic quirk translation

init python:
    import re

    quirks = {
        "gamzee": [("([a-zA-Z])([a-zA-Z]?)", lambda m: m.group(1).lower() + m.group(2).upper())],
        "kankri": [("[Bb]", "6"), ("[Oo]", "9")],
        "lower": [("(.+)", lambda m: m.group(1).lower())],
        "upper": [("(.+)", lambda m: m.group(1).upper())]
    }

    def quirkSayer(who, quirk):
        def _sayer(what, amt=0, stmt=None, **kwargs):
            return quirkSay(who, quirk, what)
        return _sayer

    def quirkSay(who, quirk, what, **kwargs):
        return who(quirkSub(quirk, what), **kwargs)

    def quirkSub(quirk, what):
        quirksubs = quirks.get(quirk.lower(), None)
        if not quirksubs:
            if renpy.config.developer:
                raise Exception("ERROR: No such quirk {}".format(quirk))
            return what
        for (pattern, repl) in quirksubs:
            what = re.sub(pattern, repl, what)
        return what