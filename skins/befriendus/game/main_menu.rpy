init offset = 2

# Main menu for Befriendus Liteskin

# define config.main_menu_music = "music/datingsimtitlehvs.wav"

# Splash screen on first load

label splashscreen:
    if persistent.firstscreen:
        scene black
        fscreen "Befriendus contains spoilers for Homestuck, The Homestuck Epilogues, and Hiveswap: Friendsim. You do not need to have read The Homestuck Epilogues or Hiveswap: Friendsim to enjoy the game, but you may miss occasional references.\n\n\nPesterquest contains flashing lights and similar imagery. You may disable these animations in the options menu.\n\n\nPesterquest contains mature content and sensitive themes. For detailed content warnings, consult the {a=call:dlc_warnings}\"Warnings\"{/a} menu."
        $ persistent.firstscreen = False
    return


define titletags = [
    "#this is a test tag #just for because", 
    "#this is a test tag", 
    "#testing for the game #let's hope it goes well", 
    "#should probably get some longer tags in here as well #just in case", 
    "#i love befriendus", 
    "#this is gonna be good", 
    "#damara rights", 
    "#i like making games", 
    "#uh oh #spaghettios"
]

define befriendus_achievement_tags = {
    "vol1_meenah": [
        "{color=#77003c}#this is a tag here{/color}", 
        "{color=#77003c}#yet another tag. whoop dee freakin doo{/color}", 
        "{color=#77003c}#HURRAH{/color}", 
        "{color=#77003c}#kankri is going to be a character in this game{/color}", 
        "{color=#77003c}#tags here{/color}", 
        "{color=#77003c}#insert tags here{/color}", 
        "{color=#77003c}#sweaters be gone{/color}", 
        "{color=#77003c}#stealing this from minecraft{/color}", 
        "{color=#77003c}#falcon.............. #penance{/color}", 
        "{color=#77003c}#let me tell you about homestuck in excruciating detail{/color}", 
        "{color=#77003c}#we've got tags up in here{/color}", 
        "{color=#77003c}#hats are fun{/color}"
    ]
}

# grant with $ achievement.grant("ach_bfs_kankri")
# Define achievements in meta.json

#define config.main_menu_music = "music/PQ_TITLE_LOOP.wav"

transform menumove:
    xpos 20
    on hover:
        linear .25 xpos 50
    on idle:
        linear .25 xpos 20

transform menulightflick:
    alpha 0.85
    linear 0.08 alpha 0.7
    linear 0.08 alpha 0.85
    repeat

transform menulightflickslow:
    alpha 0.85
    linear 0.5 alpha 0.7
    linear 0.5 alpha 0.85
    repeat

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add "gui/main_menu.png"

    if persistent.flash:
        add "gui/menu_light_flicker.png" at menulightflick
    else:
        add "gui/menu_light_flicker.png" at menulightflickslow

    #HASHTAG LISTS ~CHANGES EVERY ROUTE~
    $ titletag_groups = [titletags]

    for ach, new_tags in befriendus_achievement_tags.items():
        if achievement.has(ach):
            $ titletag_groups.append(new_tags)

    default titletag = renpy.random.choice(renpy.random.choice(titletag_groups))

    imagebutton auto "gui/title_%s.png" action SetScreenVariable("titletag", renpy.random.choice(renpy.random.choice(titletag_groups))) yanchor 0 xanchor 0 xpos 20 ypos 20 # at wiggle
    
    imagebutton auto "gui/start_%s.png" action Start("start_custom") pos (20, 345) at menumove
    imagebutton auto "gui/load_%s.png" action ShowMenu('load') pos (20, 405) at menumove
    imagebutton auto "gui/options_%s.png" action ShowMenu('preferences') pos (20, 465) at menumove
    imagebutton auto "gui/friends_%s.png" action ShowMenu('dlc_achievements') pos (20, 525) at menumove
    imagebutton auto "gui/credits_%s.png" action ShowMenu('dlc_credits') pos (20, 585) at menumove
    imagebutton auto "gui/exit_%s.png" action Quit(confirm=not main_menu) pos (20, 645) at menumove

    textbutton titletag:
        action NullAction()
        background Frame("gui/menu_hashtag_border.png", 10, 10)
        xpadding 10
        ypadding 10
        xmargin 5
        ymargin 5
        xpos 400
        ypos 190
        xanchor 0.5
        yanchor 0.0
        text_font "courbd.ttf"
        text_size 20
        text_color "#000000"
        text_xsize 500
        text_text_align 0.5

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