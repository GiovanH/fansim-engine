init offset = 0

init python:

    # Menus

    def Secret():
        # bg_cur = renpy.music.get_playing(channel='music')
        # renpy.music.stop()
        renpy.play("music/honk_short.wav")
        # renpy.music.queue(bg_cur)

    # Script
    
    def debug_dump_character(sayer):
        images = filter(
            lambda i: i[0][0] == sayer.image_tag,
            renpy.display.image.images.items()
        )

        renpy.say(None, repr(sayer))
        for name, image in images:
            renpy.show(name)
            ja(repr(name))
        renpy.hide(sayer.image_tag)

    # if persistent.developer is not None:
    #     config.developer = persistent.developer

    # def ToggleDevMode():
    #     config.developer = not config.developer
    #     return SetField(persistent, 'developer', config.developer)()

style mainmenu_devbox_frame:
    xalign 1.0
    yalign 1.0
    spacing -10

style mainmenu_devbox_button:
    xalign 1.0 

style mainmenu_devbox_button_text:
    idle_color "#000" 
    text_align 1.0

style mainmenu_devbox_text is mainmenu_devbox_button_text

screen mainmenu_devbox:
    frame:
        style_prefix "mainmenu_devbox"
        vbox:
            # background Solid("#0A0")
            textbutton "Music Room" action ShowMenu("music_room") 
            textbutton "Panel Room" action ShowMenu("panel_room")

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

define config.developer = True
define config.autoreload = False