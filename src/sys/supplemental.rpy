python:
    """
    Misc additional functionality.

    This file also includes the helper label that transitions to the 
    custom volume select screen.

    Various generic transformations are also here

    """


init offset = 0

init python:

    # RenPy store wrappers
    def get_all_sayers(store_=store):
        """Return all the "sayers" in the global store."""
        if not isinstance(store_, dict):
            store_ = store_.__dict__
        return filter(
            lambda i: isinstance(i[1], ADVCharacter),
            store_.items()
        )

    def get_all_images():
        """Returns all the images in the global store."""
        return filter(
            lambda i: not isinstance(i[1], renpy.text.extras.ParameterizedText),
            renpy.display.image.images.items()
        )

    def get_images_from_sayer(sayer_name):
        """Returns all the images belonging to a given sayer."""
        return filter(
            lambda i: i[0][0] == sayer_name,
            get_all_images()
        )

    # Image/display helper functions
    def scaleBestFit(image, tw, th):
        """Returns a scaled version of a displayable, preserving the aspect ratio.
        Args:
            image (displayable): Input image
            tw (int): Maximum target height
            th (int): Maximum target width
        """
        mw, mh = im.image(image).load().get_size()
        mh, mw, th, tw = map(float, [mh, mw, th, tw])
        factor = min(tw / mw, th / mh)
        return im.FactorScale(image, width=factor, height=factor)

    def getImageOrPlaceholder(target, failbg, failsize, failtext=None):
        if not failtext:
            failtext = failbg
        if renpy.exists(target):
            return target
        else:
            print("Missing image")
            print(target)
            placeholder = Composite(
                failsize,
                (0, 0), failbg,
                (0, 0), Text(failtext, xsize=failsize[0])
            )
            return placeholder

    def hex_to_rgb(hex):
        """Returns a RGB tuple equivilant to the given hexadecimal color code."""
        hex = hex.lstrip('#')
        if len(hex) == 3:
            hex = "".join(c + c for c in hex)
        hlen = len(hex)
        return tuple(
            int(hex[i:i+hlen/3], 16)
            for i in range(0, hlen, hlen/3)
        )

    def calcLineHeight(text, chars_per_line):
        logical_lines = text.split("\n")
        overflows = 0
        for line in logical_lines:
            used_chars = 0
            for word in line.split(" "):
                if used_chars + len(word) + 1 > chars_per_line:
                    used_chars = 0
                    overflows += 1
                used_chars += len(word) + 1
        # print(text)
        # print(len(logical_lines), "llines")
        # print(overflows, "overflows")
        return len(logical_lines) + overflows

    # Data utility functions
    def reEscapeString(str_):
        """Escapes quotes in string"""
        return str_.replace('"', '\\"')

    def jsonReEscape(table1):
        """Escapes quotes in all strings in a given dictionary"""
        return {
            k: (reEscapeString(v) if type(v) is str else v)
            for k, v in
            table1.items()
        }

    def splitIntoLists(iterable, numlists, continuous=True):
        ### Utility function: splits an iterable evenly into lists.
        ### >>> splitIntoLists(range(7), 2, True)
        ### [[0, 1, 2, 3], [4, 5, 6]]
        ### >>> splitIntoLists(range(8), 3, False)
        ### [[0, 3, 6], [1, 4, 7], [2, 5]]
        ret = [[] for i in range(numlists)]
        index = 0
        if continuous:
            max_items_per = len(iterable) / numlists
            for i, e in enumerate(iterable):
                if len(ret[index]) >= max_items_per and (index + 1) < numlists:
                    index = index + 1 
                ret[index].append(e)
        else:
            for i, e in enumerate(iterable):
                index = i%numlists
                ret[index].append(e)
        return ret

    # RenPy control flow helpers
    def ShowMenuFallback(*screens):
        for screen in screens:
            if renpy.has_screen(screen):
                return ShowMenu(screen)
        raise Exception("No screens in set {} exist.".format(screens))

    # Dialogue helpers
    import random
    class Fun(NoRollback):
        def __init__(self, max_, val=None):
            """Create a rollback-proof Fun value between 0 and max_ OR preset to val"""
            self.value = val if val is not None else random.randint(0, max_)

        def check(self, value):
            """Returns True if value is equal to the stored value, else false."""
            return (self.value == value)

        def burn(self, target):
            """Like check, but, if True, resets the value to None, preventing future checks"""
            if self.value == target:
                self.value = False
                return True
            else:
                return False

        def __repr__(self):
            return "fun.value=" + repr(self.value)


label debug_dump_character(sayer, sayer_name):
    ### This causes a sayer to iterate through all their poses, and is a helpful tool.
    ### This is also used in the developer tools.
    ### This is basically a whole convolution in order to keep rollback working

    $ renpy.say(None, repr(sayer))

    $ renpy.choice_for_skipping()
    
    $ __p__dumpcollection = sorted(get_images_from_sayer(sayer_name))
    $ __p__dumplen = len(__p__dumpcollection)
    $ __p__dumpi = 0

    while __p__dumpi < __p__dumplen:
        $ (name, image) = __p__dumpcollection[__p__dumpi]
        $ renpy.show(name)
        $ sayer(" ".join(name))
        $ __p__dumpi += 1
    $ renpy.choice_for_skipping()
    $ renpy.pause()
    $ renpy.hide(sayer.image_tag)
    return 


label start_custom:

    # This is used to easily add a formatted '>' to the start of choices in menus.
    $ pick = "> "
    $ quick_menu = False

    # Stop main menu music, or any other music playing, and transition to volume select.

    show image "gui/main_menu.png"
    window hide
    scene black with Dissolve(1.5)
    $ main_menu = True
    $ fse_block_devbox = False

    stop music fadeout 1.0
    call screen vol_select_custom() with Dissolve(1.0)
    return

# Various hiveswap transforms

transform floaties3:
    alpha 0.0 xpos 900 ypos 225
    pause 28
    parallel:
        easeout 4 alpha 0.4
        pause 2
        easein 4 alpha 0.0
