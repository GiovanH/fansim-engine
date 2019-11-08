# Define characters

define {{p}}_tz = Character("trolling: gallowsCalibrator", color='#FFFFFF', who_xpos=-80, who_text_align=1.0, who_ypos=16, who_size=17, what_color='#008282', image="{{p}}_terezi", window_background="gui/textbox_trollian_teal.png",)

# Give characters poses
image {{p}}_terezi neutral = Image("{{assets}}/terezi.png", ypos=730, xanchor=640, yanchor=730)

image {{p}}_fakemenu = "{{assets}}/fakemenu.png"

# Start of route
label {{package_entrypoint}}_terezi:

    # Menu boilerplate: Exit main menu, fade to black
    $ renpy.block_rollback()
    $ main_menu = False
    show image "gui/game_menu.png"
    window hide
    scene black with Dissolve(1.0)
    show blackcover
    $ quick_menu = True

    # Set the scene, fade in from black
    scene bg johnroom
    show {{p}}_terezi neutral
    play music "music/fs_BOLDIR.wav" loop
    hide blackcover with dissolve

    # Write dialogue!
    {{p}}_tz neutral "Hey. Hey. Over here."

    "Oh shit. You’re just standing out here with all his mail, he’s going to think you’re trying to rob the place."
    menu:
        "Oh shit. You’re just standing out here with all his mail, he’s going to think you’re trying to rob the place.{fast}"

        "[pick] Play it cool":
            pass
        "[pick] Hide the evidence":
            pass


    show {{p}}_fakemenu
    {{p}}_tz "UHHHHHHHH"
    show {{p}}_terezi at right1280 with ease
    {{p}}_tz "*SNIFFFFFFFF*"
    show {{p}}_terezi at left1280 with move
    {{p}}_tz "TF 1S TH1S TH1NG :?"

    # Show end card
    call ending pass ("vriska end", True, True)
    return
