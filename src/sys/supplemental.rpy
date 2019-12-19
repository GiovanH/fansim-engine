python:
    """
    Misc additional functionality.

    $ debug_dump_character(sayer)
    This causes a sayer to iterate through all their poses, and is a helpful tool.
    This is also used in the developer tools.

    This file also includes the helper label that transitions to the 
    custom volume select screen.

    Various generic transformations are also here

    """


init offset = 0

init python:

    # Script
    def get_all_sayers(store_=store):
        return filter(
            lambda i: isinstance(i[1], ADVCharacter),
            store_.__dict__.items()
        )

    def get_all_images():
        return renpy.display.image.images.items()

    def get_images_from_sayer(sayer):
        return filter(
            lambda i: i[0][0] == sayer.image_tag,
            get_all_images()
        )

    def reEscapeString(str_):
        return str_.replace('"', '\\"')

    def jsonReEscape(table1):
        return {
            k: (reEscapeString(v) if type(v) is str else v)
            for k, v in
            table1.items()
        }

label debug_dump_character(sayer):

    # This is basically a whole convolution in order to keep rollback working

    $ renpy.say(None, repr(sayer))

    $ renpy.choice_for_skipping()
    
    $ __p__dumpcollection = sorted(get_images_from_sayer(sayer))
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
    $ pick = "{color=#000000}>{/color}"
    $ quick_menu = False

    # Stop main menu music, or any other music playing, and transition to volume select.
    stop music fadeout 1

    show image "gui/main_menu.png"
    window hide
    scene black with Dissolve(0.5)
    $ main_menu = True
    $ pqms_block_devbox = False
    call screen vol_select_custom() with Dissolve(0.5)
    return

define config.autoreload = False

# Various hiveswap transforms

transform floaties3:
    alpha 0.0 xpos 900 ypos 225
    pause 28
    parallel:
        easeout 4 alpha 0.4
        pause 2
        easein 4 alpha 0.0
