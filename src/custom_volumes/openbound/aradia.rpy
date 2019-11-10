define ob_aradia = Character("aradia", kind=trollean, what_color="#000000", image="ob_aradia", window_background="gui/textbox_trollian_rust.png")
image ob_aradia happy = Image("{{assets}}/dialogs/aradia_happy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aradia happytalk = Image("{{assets}}/dialogs/aradia_happytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aradia idle = Image("{{assets}}/dialogs/aradia_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aradia laugh = Image("{{assets}}/dialogs/aradia_laugh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aradia point = Image("{{assets}}/dialogs/aradia_point.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aradia talk = Image("{{assets}}/dialogs/aradia_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aradia wink = Image("{{assets}}/dialogs/aradia_wink.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aradia happytalk:
    Image("{{assets}}/dialogs/aradia_happytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/aradia_happytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_aradia talk:
    Image("{{assets}}/dialogs/aradia_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/aradia_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
