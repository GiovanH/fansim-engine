init offset = 2

# Splash screen on first load

label splashscreen:
    if persistent.firstscreen:
        scene black
        fscreen "Pesterquest Lite contains spoilers for Homestuck, The Homestuck Epilogues, and Hiveswap: Friendsim. You do not need to have read The Homestuck Epilogues or Hiveswap: Friendsim to enjoy the game, but you may miss occasional references.\n\n\nPesterquest contains flashing lights and similar imagery. You may disable these animations in the options menu.\n\n\nPesterquest contains mature content and sensitive themes. For detailed content warnings, consult the {a=call:dlc_warnings}\"Warnings\"{/a} menu."
        $ persistent.firstscreen = False
    return

# Main menu for default liteskin
# Offset = 2 to override SYS overrides

image titlesky = "gui/game_menu.png"
define config.main_menu_music = "music/main_menu.wav"

transform menumove:
    xpos 20
    on hover:
        linear .25 xpos 50
        
    on idle:
        linear .25 xpos 20
        
screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add "titlesky"

    #add "gui/sun2.png" at titlesun
    #add "gui/lensflare.png" at titleflare
    #add "gui/clouds.png" at titleclouds


    add "gui/title_noglitch" pos(5, 5) at title

    #imagebutton auto "gui/title_%s.png" action NullAction() pos (5, 5)

    imagebutton auto "gui/start_%s.png" action ShowVolSelectAction pos (20, 345) at menumove
    imagebutton auto "gui/load_%s.png" action ShowMenuFallback('load') pos (20, 405) at menumove
    imagebutton auto "gui/options_%s.png" action ShowMenuFallback("preferences") pos (20, 465) at menumove
    imagebutton auto "gui/friends_%s.png" action ShowMenuFallback('dlc_achievements') pos (20, 525) at menumove
    imagebutton auto "gui/credits_%s.png" action ShowMenuFallback('credits') pos (20, 585) at menumove
    imagebutton auto "gui/exit_%s.png" action Quit() pos (20, 645) at menumove

    # use mainmenu_devbox
    key "trickster" action getMousePosition, ShowMenuFallback('mainmenu_devbox')


transform title:

    "gui/logo-noglitch.png"
    pause 3.0
    "gui/logo-glitch1.png"
    pause 0.04
    "gui/logo-glitch2.png"
    pause 0.04
    "gui/logo-glitch3.png"
    pause 0.04
    "gui/logo-glitch4.png"
    pause 0.04
    "gui/logo-glitch5.png"
    pause 0.04
    "gui/logo-glitch6.png"
    pause 0.04
    "gui/logo-noglitch.png"
    pause 4.0
    "gui/logo-glitch1.png"
    pause 0.04
    "gui/logo-glitch2.png"
    pause 0.06
    "gui/logo-glitch3.png"
    pause 0.17
    "gui/logo-glitch4.png"
    pause 0.03
    "gui/logo-glitch5.png"
    pause 0.04
    "gui/logo-glitch6.png"
    pause 0.04
    repeat

transform titlesun:

    rotate 30 pos (1175, 85) around (2.0, 2.0)
    easeout 16.0 rotate 0 pos (720, -100) around (2.0, 2.0)

transform titleflare:

    additive 1.0
    alpha 0.0
    pause 8.0
    easeout 8.0 alpha 1.0

transform titleclouds:

    alpha 0.9
    additive 1.0


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