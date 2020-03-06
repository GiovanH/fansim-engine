python:
    """
    Overrides

    These are the few areas we intentionally override names.
    We have to replace the main menu.
    We also switch around a few key bindings.

    """


init offset = 1

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['trickster'] = []
    config.keymap['trickster'].append('ctrl_K_t')
    config.keymap['trickster'].append('alt_K_t')
    config.keymap['trickster'].append('shift_K_t')

    # renpy.loader.auto_mtimes.clear()
    # renpy.loader.add_auto(os.path.abspath("autoreload"), force=True)
    # renpy.config.autoreload_blacklist.append("")
    # with renpy.loader.auto_lock:
    #     renpy.loader.auto_mtimes[fn]

define config.autoreload = False

transform menustill:
    xpos 20

# This doesn't really get used now, because main_menu from the liteskin takes over
screen main_menu():
    tag menu

    style_prefix "main_menu"

    add "titlesky"

    # Pesterquest originally used an animation here, but now
    # uses a prerendered video file. 

    #add "gui/sun2.png" at titlesun
    #add "gui/lensflare.png" at titleflare
    #add "gui/clouds.png" at titleclouds
    add "gui/title_noglitch" pos(5, 5) at title

    #imagebutton auto "gui/title_%s.png" action NullAction() pos (5, 5)

    vbox:
        xpos 20
        xanchor 0
        yalign 1.0

        imagebutton auto "gui/start_%s.png" ysize 60 action Start("start") at menumove
        imagebutton auto "{{assets}}/start_fanon_%s.png" ysize 60 action Start("start_custom") alternate (lambda: renpy.play("music/honk_short.wav")) at menumove
        imagebutton auto "gui/load_%s.png" ysize 60 action ShowMenu('load') at menumove
        imagebutton auto "gui/options_%s.png" ysize 60 action ShowMenu('preferences') at menumove
        hbox:
            imagebutton auto "gui/friends_%s.png" ysize 60 action ShowMenu("achievements") at menustill
            imagebutton auto "{{assets}}/dlc_superscript_%s.png" ysize 60 action ShowMenu("dlc_achievements") at menustill
        hbox:
            imagebutton auto "gui/credits_%s.png" ysize 60 action ShowMenu("about") at menustill
            imagebutton auto "{{assets}}/dlc_superscript_%s.png" ysize 60 action ShowMenu("dlc_credits") at menustill
        imagebutton auto "gui/exit_%s.png" ysize 60 action Quit(confirm=not main_menu) at menumove

    # use mainmenu_devbox
    key "trickster" action getMousePosition, ShowMenu("mainmenu_devbox")


## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing
        
        if not main_menu:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Options") action ShowMenu("preferences")
        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()
        textbutton _("Chumroll") action ShowMenu("achievements")
        textbutton _("Achievements (DLC)") action ShowMenu("dlc_achievements")
        textbutton _("Credits (PQ)") action ShowMenu("about")
        textbutton _("Credits (DLC)") action ShowMenu("dlc_credits")
        textbutton _("Warnings (PQ)") action ShowMenu("content_warnings")
        textbutton _("Warnings (DLC)") action ShowMenu("dlc_warnings")
        textbutton _("Close Menu"):
            action Return()
