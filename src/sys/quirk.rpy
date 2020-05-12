python:
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
        QuirkStore["amisia"] = [("u", "uu")]

    init python:
        QuirkStore["diemen"] = [("(.+)", "(| \g<1> |)")]

    You can also use inline python, if you wish. 

        $ QuirkStore["azdaja"] = [("(.+)", "||| \g<1> |||")]

    """


init offset = 0

# Automatic quirk translation

init -1 python:
    import re

    __p__quirk_debug = False

    QuirkStore = {
        "gamzee": [ # List of replacements:
            # Replace this regex      # With this
            ("([a-zA-Z])([a-zA-Z]?)", lambda m: m.group(1).lower() + m.group(2).upper())
        ],
        "kankri": [("[Bb]", "6"), ("[Oo]", "9")],
        "lower": [("(.+)", lambda m: m.group(1).lower())],
        "upper": [("(.+)", lambda m: m.group(1).upper())],
        "mituna": [("(.+)", lambda m: m.group(1).upper())] + [(c, "4831057"[i]) for i, c in enumerate("ABEIOST")],
        "greentext": [(r"((?<=^)|(?<=\n))(>.+)(?=$|\n)", "{color=#789922}\g<2>{/color}")]
    }
    quirks = QuirkStore

    NotSet = renpy.object.Sentinel("NotSet")

    class QuirkChar(ADVCharacter):
        def __init__(self, name=NotSet, kind=None, quirklist=[], *args, **kwargs):
            super(type(self), self).__init__(name=name, kind=kind, *args, **kwargs)
            self.quirklist = quirklist
            self.kind = kind or renpy.store.adv
            self.sayer = quirkSayer(super(type(self), self), self.quirklist)
            
            # print(self)
            # print(type(self))
            # print(super(type(self), self))

        def __call__(self, what, *args, **kwargs):
            self.sayer.__call__(what, *args, **kwargs)


    def quirkSayer(who, quirklist):
        """Returns a sayer that wraps another sayer and applies quirks.
        Args:
            who (sayer)
            quirklist: Quirk name, or ordered list of quirk names, to apply. 
        """
        if __p__quirk_debug:
            print("quirksayer from who", who, "with quirklist", quirklist)
        def _sayer(what, *args, **kwargs):
            return quirkSay(who, quirklist, what, *args, **kwargs)
        return _sayer

    def quirkToTags(what, quirklist):
        ret = what
        # Automatically fix single-element strings
        if type(quirklist) is type(""):
            quirklist = [quirklist]

        for q in quirklist:
            ret = "{quirk=" + q + "}" + ret + "{/quirk}"
        if __p__quirk_debug:
            print("quirktotags from what", what, "with quirklist", quirklist, "returns", ret)
        return ret

    def quirkSay(who, quirklist, what, *args, **kwargs):
        """Say a line of dialogue, but postprocess it first.

        Args:
            who (sayer)
            quirklist: Quirk name, or ordered list of quirk names, to apply.
            what: Line of dialogue

        kwargs:
            [pass through to say]
        """
        tagged = quirkToTags(what, quirklist)
        if __p__quirk_debug:
            print("who", who, "quirksaying", tagged)
        return who.__call__(tagged, *args, **kwargs)

    def quirkSub(quirklist, what):
        """Returns the input as a quirk-formatted string.

        Args:
            quirklist: Quirk name, or ordered list of quirk names, to apply.
            what: Line of dialogue

        >>> quirkSub("mituna", "lorem ipsum")
        "L0R3M 1P5UM"

        >>> quirkSub(["mituna", "lower"], "lorem ipsum")
        "l0r3m 1p5um"

        """
        if persistent.fse_disablequirks:
            return what

        ret = what

        # Automatically fix single-element strings
        if type(quirklist) is type(""):
            quirklist = [quirklist]

        for quirkname in quirklist:
            quirksubs = QuirkStore.get(quirkname.lower(), None)
            if not quirksubs:
                if renpy.config.developer:
                    raise Exception("ERROR: No such quirk {}".format(quirkname))
                return ret
            for (pattern, repl) in quirksubs:
                ret = re.sub(pattern, repl, ret)
        if __p__quirk_debug:
            print("quirksub from what", what, "with quirklist", quirklist, "returns", ret)
        return ret

    def quirkSubManual(raw_text, quirked_text):
        return raw_text if persistent.fse_disablequirks else quirked_text

    def texttag_quirk(tag, argument, contents):
        quirklist = [argument]

        rv = []
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                # rv.append((kind, quirkSub(quirklist, text)))
                # Tokenize tags that are part of the quirk itself
                rv += renpy.text.textsupport.tokenize(quirkSub(quirklist, text))
            else:
                rv.append((kind, text))
        if __p__quirk_debug:
            print("quirk tag with arg", argument, "and contents", contents, "returns", rv)
        return rv

    config.custom_text_tags["quirk"] = texttag_quirk

    def texttag_quirked(tag, argument, contents):

        quirked_text = argument
        has_done = False

        rv = []
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                if has_done:
                    raise Exception("Tag {quirked} cannot contain multiple text segments!")
                rv.append((kind, quirkSubManual(text, quirked_text)))
                has_done = True
            else:
                rv.append((kind, text))
        return rv

    config.custom_text_tags["quirked"] = texttag_quirked