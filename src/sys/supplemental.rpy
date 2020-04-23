python:
    """
    Misc additional functionality.

    This file also includes the helper label that transitions to the 
    custom volume select screen.

    Various generic transformations are also here

    """


init offset = 0

init python:

    # Script
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
        overflows = sum((len(line) / chars_per_line) for line in logical_lines)
        return len(logical_lines) + overflows

    def getImageOrPlaceholder(target, failbg, failsize, failtext=None):
        print("Running giop for %s" % target)
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
