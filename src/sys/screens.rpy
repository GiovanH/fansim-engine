python:
    """
    Custom screens:
        Custom volume select
        Custom warnings
        Custom credits
        Developer mode menu
        Mouse utilities
        Developer boxes, both main menu and ingame
        Variable watcher
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
        """Toggles developer mode and then reloads the game."""
        config.developer = not config.developer
        SetField(persistent, 'developer', config.developer)()
        _reload_game()

    store.mousex, store.mousey = 200, 200
    def getMousePosition():
        """Stores the current mouse position at store.mousex, store.mousey."""
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
    color gui.accent_color

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

style mainmenu_devbox_button_text is confirm_prompt_text:
    idle_color gui.idle_color
    text_align 1.0

style mainmenu_devbox_text is mainmenu_devbox_button_text

screen mainmenu_devbox:
    key "trickster" action HideFallback("mainmenu_devbox")
    key "game_menu" action HideFallback("mainmenu_devbox")
    key "hide_windows" action HideFallback("mainmenu_devbox")
    modal True

    frame:
        anchor (0.0, 0.0)
        xpos mousex
        ypos mousey
        style_prefix "mainmenu_devbox"
        vbox:
            label "Tools"
            textbutton "Clear achievements" action HideFallback("mainmenu_devbox"), ConfirmActionAction(
                achievement.clear_all, 
                "Are you sure you want to clear all your achievements?"
            )
            textbutton "Clear seen music" action HideFallback("mainmenu_devbox"), ConfirmActionAction(
                renpy.game.persistent._seen_audio.clear, 
                "Are you sure you want to clear your music history? This will re-lock music player entries."
            )

            if config.developer:
                textbutton "Reload (Shift+R)" action _reload_game
            textbutton "Developer Tools" action ToggleDevModeMenu

            null height 12
            if persistent.devbox_unlocked_spoilers:
                label "Gallery"
                textbutton "Music Player" action HideFallback("mainmenu_devbox"), ShowMenuFallback("__p__music_room")
                textbutton "Displayables" action HideFallback("mainmenu_devbox"), ShowMenuFallback("__p__panel_room")
                textbutton "Characters" action HideFallback("mainmenu_devbox"), ShowMenuFallback("__p__sayer_room")
            label ""
            vbox:
                style_prefix "check"
                textbutton _("Show spoilers") action ConfirmActionAction(
                    ToggleField(persistent, "devbox_unlocked_spoilers"),
                    "This unlocks features that spoil the game, including secrets and achievements.\nIt is recommended that you ONLY access these features after you have completed the game.\nDo you want to access these features now?"
                )
            transclude

label __p__NewWatchAction:
    python:
        __p__expr = renpy.input(prompt="Expression to watch")
        __p__expr.strip()
        renpy.python.py_compile(__p__expr, 'eval')
        _console.traced_expressions.append(__p__expr)
        renpy.show_screen("_trace_screen")
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
            transclude
            

define fse_block_devbox = False
screen ingame_devbox_loader:
    if config.developer and not fse_block_devbox:
        key "trickster" action getMousePosition, ShowMenuFallback('ingame_devbox')


# Extended choice screen allowing more choices if possible
# https://www.renpy.org/doc/html/screen_special.html#choice

screen choice_scrollable(items):
    ### A scrollable choice menu for very long selections.
    ### Invoke with
    ### >>> menu (screen="choice_scrollable"):
    ### >>>     "[pick] option":
    ### >>>     ...

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
            

init python:
    def getDlcVolumeIcons(volume):
        img_small = getImageOrPlaceholder(
            target="custom_assets_{package_id}/volumeselect_{volume_id}_small.png".format(**jsonReEscape(volume)),
            failbg="{{assets}}/volumeselect_fallback_small.png",
            failsize=(103, 103),
            failtext="assets/\nvolumeselect_\n{volume_id}_\nsmall.png".format(**jsonReEscape(volume))
        )
        img_norm = getImageOrPlaceholder(
            target="custom_assets_{package_id}/volumeselect_{volume_id}.png".format(**jsonReEscape(volume)),
            failbg="{{assets}}/volumeselect_fallback.png",
            failsize=(103, 103),
            failtext="assets/\nvolumeselect_\n{volume_id}.png".format(**jsonReEscape(volume))
        )

        return (img_small, img_norm,)

    ShowVolSelectAction = ShowMenuPlus(["vol_select_custom", "vol_select"], transition=Fade(1.0, 0.0, 1.0))

label vol_select_bootstrap:
    # Menu boilerplate: Exit main menu, fade to black
    $ renpy.block_rollback()
    $ main_menu = False
    $ quick_menu = False
    show image "gui/game_menu.png"
    window hide
    stop music fadeout 1.0
    scene black with Dissolve(1.5)
    $ quick_menu = True
    $ pick = "> "

    $ fse_callbacks.on("RouteStart", label=store.vol_select_label)

    jump expression store.vol_select_label

    $ fse_callbacks.on("RouteFinish", label=store.vol_select_label)
    return

screen __p__sayer_room:
    tag menu
    $ store.__p__sayer = "NotSet"
    $ store.__p__sayername = "NotSet"
    use game_menu_volumes(_("Choose a Character")):
        # A grid of buttons.
        vpgrid:
            mousewheel True
            scrollbars "vertical"
            cols 3
            xsize 940
            yfill True

            for sayername, sayer in sorted(get_all_sayers()):
                if sayername and sayer.image_tag:
                    textbutton ((sayer.image_tag + " (" + sayername + ")") if sayername != sayer.image_tag else sayername) action SetVariable("store.__p__sayer", sayer), SetVariable("store.__p__sayername", sayername), Start("__p__sayer_bootstrap2") xsize 300 ysize 60 yalign 0 xalign 0 text_style "button_text"


define fse_volume_data = []  # Overwritten
screen vol_select_custom():
    tag menu
    $ store.vol_select_label = "NotSet"
    use game_menu_volumes(_("Friend Select")):

        default icon = "gui/volumeselect_icon_blank.png"
        default title = "Volume Select"

        default subtitle = "Hover over an icon!"
        default author = ""
        
        $ num_cols = 8

        $ volumes_by_author = sorted(fse_volume_data, key=lambda v: v["author"])
                    
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
            scrollbars ("vertical" if len(fse_volume_data) > (num_cols*3) else None)
            ypos 180
            ysize 350

            vbox:
                null height 20
                vpgrid:
                    xpos 10
                    cols num_cols
                    spacing 10

                    for volume in volumes_by_author:
                        $ unlocked = True
                        if volume.get("unlocks_on"):
                            $ unlocks_on = "_".join(volume.get("unlocks_on"))
                            $ unlocked = achievement.has(unlocks_on)
                        if unlocked:
                            $ img_small, img_norm = getDlcVolumeIcons(volume)
                            imagebutton idle img_small:
                                action [
                                    SetVariable("store.vol_select_label", "custom_entry_{package_id}_{volume_id}".format(**jsonReEscape(volume))),
                                    Start("vol_select_bootstrap")
                                ]
                                hovered [
                                    SetLocalVariable("icon", img_norm), 
                                    SetLocalVariable("title", volume.get("title", "")), 
                                    SetLocalVariable("subtitle", volume.get("subtitle", "")),
                                    SetLocalVariable("author", volume.get("author", ""))
                                ]
                                unhovered [        
                                    SetLocalVariable("icon", "gui/volumeselect_icon_blank.png"), 
                                    SetLocalVariable("title", "Volume Select"), 
                                    SetLocalVariable("subtitle", "Hover over an icon!"),
                                    SetLocalVariable("author", "")
                                ]
                                alt volume.get("subtitle", "")
                # these buttons will jump to selected volume, and make the volume number/title appear in the fixed area

        text fse_vol_select_suffix xalign 0.5 yanchor 1.0 text_align 0.5 ypos 540
    transclude

define fse_credits_data = {}  # Overwritten in custom_credits.rpy

init python:
    import re
    def sortCreditsList(list_):
        def _splitSort(string):
            __, label, realstr = re.search(r"^(\(S([0-9]+)\)){0,1}(.*)", string).groups()
            return ((label or "999"), realstr)
        return [r for l, r in sorted(map(_splitSort, list_))]

    def sortCreditsDict(data):
        def _splitSort(kv):
            k, v = kv
            __, label, realstr = re.search(r"^(\(S([0-9]+)\)){0,1}(.*)", k).groups()
            return ((label or "999"), realstr, v)
        return [
            (k, v) for l, k, v 
            in sorted(map(_splitSort, data.items()))
        ]

    def angleBracketsToSquare(text):
        return text.replace("<", "[").replace(">", "]")

screen credits():
    tag menu
    use game_menu(_("Credits"), scroll="viewport"):
        style_prefix "about"
        vbox:
            spacing 14

            # There's no goddamned reason "store" should be required here. I can't puzzle it. Screen side effects?
            # alienoid says: "Looks like you weren't quite prepared for what was in `store` huh"
            
            # We COULD do this processing in advance, but we want to make it
            # easy to manually override the credits_sort config variable

            # Set local variables
            for name, value in fse_credits_data.get("ALIAS", {}).items():
                $ renpy.current_screen().scope[name] = value

            for role, list_ in sortCreditsDict(fse_credits_data.get("LIST", {})):
                text role text_align 0.5 color gui.accent_color size 30
                for name in sortCreditsList(list_):
                    hbox:
                        text angleBracketsToSquare(name) text_align 0.0 min_width 440

            for role, person_credits in sortCreditsDict(fse_credits_data.get("DICT", {})):
                text role text_align 0.5 color gui.accent_color size 30
                for name, list_ in sortCreditsDict(person_credits):
                    hbox:
                        if name:
                            text angleBracketsToSquare(name) text_align 0.0 min_width 440
                        vbox:
                            spacing 12
                            for item in sortCreditsList(list_):
                                text angleBracketsToSquare(item) text_align 0.0


            text "\n\n" text_align 1.0

            for text_ in sortCreditsList(fse_credits_data.get("POSTSCRIPT", [])):
                text angleBracketsToSquare(text_)


define fse_warning_data = {}  # Overwritten in custom_warnings.rpy
define fse_warning_data_extra = {}
screen dlc_warnings():
    tag menu
    use game_menu(_("Warnings"), scroll="viewport"):
        hbox:
            text fse_warnings_prefix
        vbox:
            spacing 2

            for title, warning in sorted(fse_warning_data.items()):
                use spoiler_box(title, warning)
            for title, warning in sorted(fse_warning_data_extra.items()):
                use spoiler_box(title, warning)


screen dlc_achievements():
    tag menu
    $ achievement.sync()
    use game_menu(_("Achievements"), scroll="viewport"):
        style_prefix "about"
        vpgrid:
            cols 10
            xspacing 20
            yspacing 20

            for ach in fse_achievements_data:
                if achievement.has(ach.get("_id")):
                    $ _img_unlocked = getImageOrPlaceholder(
                        target=ach.get("_img_unlocked"),
                        failbg="{{assets}}/ach_fallback.png",
                        failsize=(64, 64),
                        failtext="assets/\n" + ach.get("img_unlocked")
                    )
                    imagebutton idle _img_unlocked: 
                        action NullAction() 
                        hovered Show("ach_desc", None, True, ach.get("name", "name"), ach.get("desc", "desc"))
                        unhovered Hide("ach_desc")
                        # alt Hide("ach_desc")
                        # ShowMenu(
                        #     "confirm", "Are you sure you want to un-achieve this achievement?", 
                        #     (Hide("confirm"), lambda: achievement.clear(ach.get("_id"))), 
                        #     (Hide("confirm"))
                        # )
                else:
                    $ _img_locked = getImageOrPlaceholder(
                        target=ach.get("_img_locked"),
                        failbg="{{assets}}/ach_fallback.png",
                        failsize=(64, 64),
                        failtext="assets/\n" + ach.get("img_locked")
                    )
                    imagebutton idle _img_locked:
                        action NullAction() 
                        hovered Show("ach_desc", None, False, ach.get("name", "name"), ach.get("hint", "hint")) 
                        unhovered Hide("ach_desc")

screen ach_desc(is_unlocked, ach_name, ach_description):
    vbox:
        xpos 320 ypos 465

        text ach_name style "label_text" xsize 900
        text ach_description xsize 900
            
        # if is_unlocked:
        # else:

