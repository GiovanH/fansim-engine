
define vr = Character("[vriskatitle]", color='#FFFFFF', who_xpos=-78, who_ypos=16, who_size=17, what_color='#005682', image="vriska", window_background="gui/textbox_trollian_cobalt.png",)

image vriska dejected1 = Image("images/Vriska_Dejected_1.png", ypos=730, xanchor=640, yanchor=730)
image vriska dejected2 = Image("images/Vriska_Dejected_2.png", ypos=730, xanchor=640, yanchor=730)
image vriska dejected3 = Image("images/Vriska_Dejected_3.png", ypos=730, xanchor=640, yanchor=730)
image vriska hype1 = Image("images/Vriska_Hype_1.png", ypos=730, xanchor=640, yanchor=730)
image vriska hype2 = Image("images/Vriska_Hype_2.png", ypos=730, xanchor=640, yanchor=730)
image vriska neutral1 = Image("images/Vriska_Neutral_1.png", ypos=730, xanchor=640, yanchor=730)
image vriska neutral2 = Image("images/Vriska_Neutral_2.png", ypos=730, xanchor=640, yanchor=730)
image vriska neutral3 = Image("images/Vriska_Neutral_3.png", ypos=730, xanchor=640, yanchor=730)
image vriska neutral4 = Image("images/Vriska_Neutral_4.png", ypos=730, xanchor=640, yanchor=730)
image vriska shout1 = Image("images/Vriska_Shout_1.png", ypos=730, xanchor=640, yanchor=730)
image vriska shout2 = Image("images/Vriska_Shout_2.png", ypos=730, xanchor=640, yanchor=730)
image vriska smug1 = Image("images/Vriska_Smug_1.png", ypos=730, xanchor=640, yanchor=730)
image vriska smug2 = Image("images/Vriska_Smug_2.png", ypos=730, xanchor=640, yanchor=730)
image vriska talk1 = Image("images/Vriska_Talk_1.png", ypos=730, xanchor=640, yanchor=730)
image vriska talk2 = Image("images/Vriska_Talk_2.png", ypos=730, xanchor=640, yanchor=730)
image vriska talk3 = Image("images/Vriska_Talk_3.png", ypos=730, xanchor=640, yanchor=730)
image vriska upset1 = Image("images/Vriska_Upset_1.png", ypos=730, xanchor=640, yanchor=730)
image vriska upset2 = Image("images/Vriska_Upset_2.png", ypos=730, xanchor=640, yanchor=730)
image vriska control1 = Image("images/Vriska_Control_1.png", ypos=730, xanchor=640, yanchor=730)
image vriska control2 = Image("images/Vriska_Control_2.png", ypos=730, xanchor=640, yanchor=730)


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
    vr neutral3 "8itch."
