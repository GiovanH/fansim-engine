init offset = 2

# Main menu for Hiveswap Liteskin

# Splash screen on first load

label splashscreen:

    if persistent.firstscreen:

        scene black

        fscreen "Pesterquest Lite contains spoilers for Homestuck, The Homestuck Epilogues, and Hiveswap: Friendsim. You do not need to have read The Homestuck Epilogues or Hiveswap: Friendsim to enjoy the game, but you may miss occasional references.\n\n\nPesterquest contains flashing lights and similar imagery. You may disable these animations in the options menu.\n\n\nPesterquest contains mature content and sensitive themes. For detailed content warnings, consult the {a=call:dlc_warnings}\"Warnings\"{/a} menu."

        $ persistent.firstscreen = False

    return


image titlesky = "gui/game_menu.png"
define config.main_menu_music = "music/datingsimtitlehvs.wav"

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background
    
    imagebutton auto "gui/title_%s.png" action NullAction() yanchor 0 xanchor 0 xpos 20 ypos 20 # at wiggle
    
    imagebutton auto "gui/start_%s.png" action Start("start_custom") pos (20, 345) at menumove
    imagebutton auto "gui/load_%s.png" action ShowMenu('load') pos (20, 405) at menumove
    imagebutton auto "gui/options_%s.png" action ShowMenu('preferences') pos (20, 465) at menumove
    imagebutton auto "gui/friends_%s.png" action ShowMenu('achievements') pos (20, 525) at menumove
    imagebutton auto "gui/credits_%s.png" action ShowMenu('dlc_credits') pos (20, 585) at menumove
    imagebutton auto "gui/exit_%s.png" action Quit(confirm=not main_menu) pos (20, 645) at menumove


    # use mainmenu_devbox
    key "trickster" action getMousePosition, ShowMenu('mainmenu_devbox')



style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")