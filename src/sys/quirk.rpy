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
        """A variation of ADVCharacter that takes a quirklist. 
        This intercepts calls and redirects them to a quirkSayer.
        """
        def __init__(self, name=NotSet, kind=renpy.store.adv, quirklist=[], *args, **kwargs):
            # Override name to prevent double-assignment
            # (although this bug was only noticed in NVL(?), needs research)
            # Name must be in arg list to support posargs
            super(QuirkChar, self).__init__(name=name, kind=kind, *args, **kwargs)
            self.quirklist = quirklist
            if not quirklist:
                try:
                    # if kind is not None and hasattr, but that's slower than just try/catch actually
                    self.quirklist = kind.quirklist
                except:
                    pass
            # self.kind = kind
            # self.sayer = quirkSayer(super(QuirkChar, self), self.quirklist)

        def __call__(self, what, *args, **kwargs):
            # If call is given any kwargs, ren'py will
            # fold those into a new character object, which creates
            # a whole new call tree. 
            #
            # We do NOT quirkify text in that case
            # or else it will be quirkified multiple times.
            # See character.rpy:1041 (__call__)
            safe_kwarg_keys = ["interact", "_mode", "_call_done", "multiple", "_with_none"]
            if all(k in safe_kwarg_keys for k in kwargs.keys()):
                what = quirkToTags(what, self.quirklist)

            print(QuirkChar, self, what, args, kwargs)
            super(QuirkChar, self).__call__(what, *args, **kwargs)


    class QuirkCharNVL(NVLCharacter):
        """A variation of NVLCharacter that takes a quirklist. 
        This intercepts calls and redirects them to a quirkSayer.
        """
        def __init__(self, name=NotSet, kind=renpy.store.adv, quirklist=[], *args, **kwargs):
            # Override name to prevent double-assignment 
            # Name must be in arg list to support posargs
            if name is not NotSet:
                kwargs["name"] = name

            super(QuirkCharNVL, self).__init__(kind=kind, *args, **kwargs)
            self.quirklist = quirklist
            if not quirklist:
                try:
                    # if kind is not None and hasattr, but that's slower than just try/catch actually
                    self.quirklist = kind.quirklist
                except:
                    pass
            # self.kind = kind
            # self.kind = kind
            # self.sayer = quirkSayer(super(QuirkCharNVL, self), self.quirklist)
        
        def __call__(self, what, *args, **kwargs):
            what = quirkToTags(what, self.quirklist)
            super(QuirkCharNVL, self).__call__(what, *args, **kwargs)

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

    def quirkSay(who, quirklist, what, *args, **kwargs):
        """Have an existing sayer say a line using a specified quirklist

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

    def quirkToTags(what, quirklist):
        """Wraps a string in {quirk} tags.
        Used internally; final quirk processing should be done by tags.
        """
        ret = what
        # Automatically fix single-element strings
        if type(quirklist) is type(""):
            quirklist = [quirklist]

        for q in quirklist:
            ret = "{quirk=" + q + "}" + ret + "{/quirk}"
        if __p__quirk_debug:
            print("quirktotags from what", what, "with quirklist", quirklist, "returns", ret)
        return ret

    def quirkSub(quirklist, what):
        """Returns the input as a quirk-formatted string.
        This should NOT be used in most cases! Use {quirk} tags or a processor like quirkSayer instead.
        This is the function that ultimately does regex replacement

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

    def texttag_quirk(tag, argument, contents):
        """The text tag {quirk}. Handles most quirk behavior internally.
        Takes a single quirk argument, so syntax is {quirk=id}text{/quirk}
        Only applies one quirk, but can be wrapped recursively."""
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
        """The text tag {quirked}. 
        Takes a single string argument, so syntax is {quirked=cre8}create{/quirked}
        This is used to manually specify what 'quirked' text should look like, for accessibility and translation."""

        quirked_text = argument
        has_done = False

        rv = []
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                if has_done:
                    raise Exception("Tag {quirked} cannot contain multiple text segments!")
                rv.append((kind, (text if persistent.fse_disablequirks else quirked_text)))
                has_done = True
            else:
                rv.append((kind, text))
        return rv

    config.custom_text_tags["quirked"] = texttag_quirked