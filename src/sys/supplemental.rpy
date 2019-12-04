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

    def debug_dump_character(sayer):
        renpy.say(None, repr(sayer))
        for name, image in sorted(get_images_from_sayer(sayer)):
            renpy.show(name)
            ja(repr(name))
        renpy.hide(sayer.image_tag)


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
    call screen vol_select_custom() with Dissolve(0.5)
    return

define config.autoreload = False