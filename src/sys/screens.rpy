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

style fse_volume_select_title:
    font "verdana.ttf" 
    size 48 
    xalign 0.5 
    color "#b4b4b5"

style fse_volume_select_subtitle:
    font "verdana.ttf" 
    size 38 
    xalign 0.5 
    color "#00baff"

style fse_volume_select_author:
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
    key "trickster" action ToggleDevModeMenu
    key "game_menu" action Hide("mainmenu_devbox")
    key "hide_windows" action Hide("mainmenu_devbox")

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
            textbutton "Credits+" action Hide("mainmenu_devbox"), ShowMenu("dlc_credits")
            textbutton "Warnings+" action Hide("mainmenu_devbox"), ShowMenu("dlc_warnings")
            null height 12
            if config.developer:
                textbutton "Reload (Ctrl+R)" action _reload_game
            textbutton "Developer Tools" action ToggleDevModeMenu

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
            

define fse_block_devbox = False
screen ingame_devbox_loader:
    if config.developer and not fse_block_devbox:
        key "trickster" action getMousePosition, ShowMenu('ingame_devbox')


# Extended choice screen allowing more choices if possible
# https://www.renpy.org/doc/html/screen_special.html#choice

screen choice_scrollable(items):
    style_prefix "choice"
    viewport:
        xsize 820
        ysize 600
        xalign 0.5

        mousewheel True
        scrollbars ("vertical" if len(items) > 8 else None)

        side_yfill True

        style_prefix "choice"

        vbox:
            for i in items:
                textbutton i.caption action i.action


style __p__spoiler_button_show:
    background "#E5E5E5" 
    hover_background "#C7C9CB"

style __p__spoiler_text_show:
    color "#32363B"

style __p__spoiler_button_hide:
    background "#B9BBBE" 
    hover_background "#C7C9CB"

style __p__spoiler_text_hide:
    color "#B9BBBE"
    hover_color "#C7C9CB"

screen spoiler_box(label, content, warningoffset=42):
    default spoil_style_state_text = "__p__spoiler_text_hide"
    default spoil_style_state_button = "__p__spoiler_button_hide"
    hbox:
        text label + ": "
        textbutton content style spoil_style_state_button text_style spoil_style_state_text action [
            ToggleLocalVariable("spoil_style_state_button", "__p__spoiler_button_hide", "__p__spoiler_button_show"),
            ToggleLocalVariable("spoil_style_state_text", "__p__spoiler_text_hide", "__p__spoiler_text_show"),
        ]
            


define dlc_volumes_data = []
screen vol_select_custom():

    use game_menu_volumes(_("Friend Select")):

        default icon = "gui/volumeselect_icon_blank.png"
        default title = "Volume Select"

        default subtitle = "Hover over an icon for info!"
        default author = "Fansim Engine"

        default num_cols = 8

        $ volumes_by_author = sorted(dlc_volumes_data, key=lambda v: v["author"])
                    
        # fixed area contains overlapping elements
        fixed:
            xpos 10
            image "gui/volumeselect_background.png" xpos 30
            image icon xpos 50 ypos 15
            text title xpos 526 ypos 32 style "fse_volume_select_title"
            text subtitle xpos 526 ypos 90  style "fse_volume_select_subtitle"
            text author xpos 860 ypos 160 style "fse_volume_select_author"

        viewport:
            mousewheel True
            scrollbars ("vertical" if len(dlc_volumes_data) > (num_cols*3) else None)
            ypos 180
            ysize 350

            vbox:
                null height 20
                vpgrid:
                    xpos 10
                    cols num_cols
                    spacing 10

                    for volume in volumes_by_author:
                        imagebutton idle "custom_assets_{package_id}/volumeselect_{volume_id}_small.png".format(**jsonReEscape(volume)) action Jump("custom_entry_{package_id}_{volume_id}".format(**jsonReEscape(volume))) hovered[
                            SetScreenVariable("icon", "custom_assets_{package_id}/volumeselect_{volume_id}.png".format(**jsonReEscape(volume))), 
                            SetScreenVariable("title", volume.get("title", "")), 
                            SetScreenVariable("subtitle", volume.get("subtitle", "")),
                            SetScreenVariable("author", volume.get("author", ""))
                        ] unhovered[        
                            SetScreenVariable("icon", "gui/volumeselect_icon_blank.png"), 
                            SetScreenVariable("title", "Volume Select"), 
                            SetScreenVariable("subtitle", "Hover over an icon!"),
                            SetScreenVariable("author", "Pesterquest Modsuite")
                        ] alt volume.get("subtitle", "")
                # these buttons will jump to selected volume, and make the volume number/title appear in the fixed area

        text "do what thou whilst shall be the whole of the law" xalign 0.5 text_align 0.5 ypos 540
        # text customVolumeSplash() 



define dlc_credits_data = {}  # Overwritten in custom_credits.rpy
screen dlc_credits():
    tag menu
    use game_menu(_("Credits (DLC)"), scroll="viewport"):
        style_prefix "about"
        vbox:
            spacing 14

            for role, list_ in dlc_credits_data.get("LIST", {}).items():
                text role text_align 0.5 color gui.accent_color size 30
                for name in list_:
                    hbox:
                        text name text_align 0.0 min_width 440

            for role, person_credits in dlc_credits_data.get("DICT", {}).items():
                text role text_align 0.5 color gui.accent_color size 30
                for name, list_ in person_credits.items():
                    hbox:
                        text name text_align 0.0 min_width 440
                        text ", ".join(list_) text_align 1.0


            text "\n\n" text_align 1.0

            for text_ in dlc_credits_data.get("POSTSCRIPT", []):
                text text_


define dlc_warning_data = {}  # Overwritten in custom_warnings.rpy
screen dlc_warnings():
    tag menu
    use game_menu(_("Warnings (DLC)"), scroll="viewport"):
        hbox:
            text "As a general rule, Pesterquest contains adult language, violence, and innuendo. Content warnings for specific routes can be accessed by clicking on the route title."

        for title, warning in dlc_warning_data.items():
            use spoiler_box(title, warning)
