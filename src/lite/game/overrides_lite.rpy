init offset = 2

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
        # textbutton _("Chumroll") action ShowMenu("achievements")
        textbutton _("Achievements") action ShowMenu("dlc_achievements")
        # textbutton _("Credits (PQ)") action ShowMenu("about")
        textbutton _("Credits") action ShowMenu("dlc_credits")
        # textbutton _("Warnings (PQ)") action ShowMenu("content_warnings")
        textbutton _("Warnings") action ShowMenu("dlc_warnings")
        textbutton _("Close Menu"):
            action Return()
