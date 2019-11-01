
define vr = Character("[vriskatitle]", color='#FFFFFF', who_xpos=-78, who_ypos=16, who_size=17, what_color='#005682', image="vriska", window_background="gui/textbox_trollian_cobalt.png",)

image vriska neutral3 = Image("images/Vriska_Neutral_3.png", ypos=730, xanchor=640, yanchor=730)
image vriska ngreen = Image("custom_assets_vriska/Vriska_Green.png", ypos=730, xanchor=640, yanchor=730)


image bg johnroom = im.Scale("images/john_s room.png", 1300,730)

image vriska control:
    "vriska control1"
    pause 0.05
    "vriska control2"
    pause 0.05
    repeat

label volume_vriska_custom:
    $ renpy.block_rollback()
    $ main_menu = False

    show image "gui/game_menu.png"

    window hide

    scene black with Dissolve(1.5)
    show blackcover

    scene bg johnroom

    hide blackcover with dissolve

    $ quick_menu = True
    play music "music/WORST_END.wav" loop

    show vriska neutral4
    vr ngreen "8itch."
