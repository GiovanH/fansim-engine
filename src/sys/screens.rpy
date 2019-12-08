python:
    """
    Custom screens:
        Developer mode menu
        Mouse utilities
        Volume select styling
        Developer boxes for main menu and ingame
        Watcher
    """


init offset = 0

init python:
    if persistent.developer is not None:
        config.developer = persistent.developer

    def ToggleDevModeMenu():
        message = "Developer mode is currently [[{}].\n\nEnabling developer mode will enable the console and reload the game.\nToggle developer mode?".format(
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

    # Add devbox
    config.overlay_screens.append("ingame_devbox_loader")

# Styles and other for menu, defined in overrides

style pqms_volume_select_title:
    font "verdana.ttf" 
    size 48 
    xalign 0.5 
    color "#b4b4b5"

style pqms_volume_select_subtitle:
    font "verdana.ttf" 
    size 38 
    xalign 0.5 
    color "#00baff"

style pqms_volume_select_author:
    font "verdana.ttf" 
    size 12 
    xalign 1.0 
    text_align 1.0 
    color "#b4b4b5" 

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

    key "trickster" action ToggleDevModeMenu
    key "game_menu" action Return()
    key "hide_windows" action Return()
    modal True
    add "gui/overlay/confirm.png"
    frame:
        anchor (0.0, 0.0)
        xpos mousex
        ypos mousey
        style_prefix "mainmenu_devbox"
        vbox:
            # background Solid("#0A0")
            textbutton "Music Player" action Hide("mainmenu_devbox"), ShowMenu("__p__music_room")
            textbutton "Displayables" action Hide("mainmenu_devbox"), ShowMenu("__p__panel_room")
            textbutton "Characters" action Hide("mainmenu_devbox"), ShowMenu("__p__sayer_room")
            null height 12
            if config.developer:
                textbutton "Reload (Ctrl+R)" action _reload_game
            textbutton "Developer Tools" action ToggleDevModeMenu
    # frame:
    #     style_prefix "mainmenu_devbox"
    #     vbox:
    #         textbutton "Developer Tools" action ToggleDevModeMenu
            # if config.developer:
            #     textbutton "Mode: Normal" action ToggleDevMode
            # else:
            #     textbutton "Mode: Dev" action ToggleDevMode

label __p__NewWatchAction:
    $ __p__expr = renpy.input(prompt="Expression to watch")
    $ renpy.watch(__p__expr)
    $ renpy.show_screen("_trace_screen")
    return 

screen ingame_devbox:

    # on "show" action getMousePosition

    key "trickster" action ToggleDevModeMenu
    key "game_menu" action Return()
    key "hide_windows" action Return()
    modal True
    add "gui/overlay/confirm.png"
    frame:
        anchor (0.0, 0.0)
        xpos mousex
        ypos mousey
        style_prefix "mainmenu_devbox"
        vbox:
            # background Solid("#0A0")
            textbutton "Watcher" action Call("__p__NewWatchAction"), Return()
            textbutton "Unwatch All" action (lambda: map(renpy.unwatch, _console.traced_expressions)), Return()
            null height 12
            textbutton "Reload (Ctrl+R)" action _reload_game
            textbutton "Developer Tools" action ToggleDevModeMenu
            

define pqms_block_devbox = False
screen ingame_devbox_loader:
    if config.developer and not pqms_block_devbox:
        key "trickster" action getMousePosition, ShowMenu('ingame_devbox')

