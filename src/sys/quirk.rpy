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