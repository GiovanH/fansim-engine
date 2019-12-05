init offset = 0

init python:
    if persistent.developer is not None:
        config.developer = persistent.developer

    def ToggleDevModeMenu():
        message = "Developer mode is currently [{}].\n\nEnabling developer mode will enable the console and reload the game.\nToggle developer mode?".format(
            "ON" if config.developer else "OFF")
        return ShowMenu(
            "confirm", message, 
            (Hide("confirm"), ToggleDevMode), 
            (Hide("confirm"))
        )()

    def ToggleDevMode():
        config.developer = not config.developer
        SetField(persistent, 'developer', config.developer)()
        _reload_game()

    store.mousex, store.mousey = 200, 200
    def getMousePosition():
        store.mousex, store.mousey = renpy.get_mouse_pos()


# Styles and other for menu, defined in overrides

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

    # on "show" action getMousePosition

    key "ctrl_K_t" action ToggleDevModeMenu
    key "game_menu" action Hide("mainmenu_devbox")
    key "hide_windows" action Hide("mainmenu_devbox")

    modal True

    imagebutton idle "gui/overlay/confirm.png" unhovered Hide("mainmenu_devbox")

    frame:
        anchor (0.0, 0.0)
        xpos mousex
        ypos mousey
        style_prefix "mainmenu_devbox"
        vbox:
            # background Solid("#0A0")
            textbutton "Music Room" action Hide("mainmenu_devbox"), ShowMenu("__p__music_room") 
            textbutton "Panel Room" action Hide("mainmenu_devbox"), ShowMenu("__p__panel_room")
            null height 12
            textbutton "Developer Tools" action Hide("mainmenu_devbox"), ToggleDevModeMenu
            if config.developer:
                textbutton "Reload (Ctrl+R)" action _reload_game
    # frame:
    #     style_prefix "mainmenu_devbox"
    #     vbox:
    #         textbutton "Developer Tools" action ToggleDevModeMenu
            # if config.developer:
            #     textbutton "Mode: Normal" action ToggleDevMode
            # else:
            #     textbutton "Mode: Dev" action ToggleDevMode