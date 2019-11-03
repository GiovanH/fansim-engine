# Define characters
define vr = Character("[vriskatitle]", color='#FFFFFF', who_xpos=-78, who_ypos=16, who_size=17, what_color='#005682', image="vriska", window_background="gui/textbox_trollian_cobalt.png",)

# Give characters poses
image vriska neutral3 = Image("images/Vriska_Neutral_3.png", ypos=730, xanchor=640, yanchor=730)
image vriska ngreen = Image("{{assets}}/Vriska_Green.png", ypos=730, xanchor=640, yanchor=730)

# Define backgrounds
image bg johnroom = im.Scale("images/john_s room.png", 1300,730)

# Define other graphics, end cards
image vriska end = "images/vriska_endcard_badend1.png"

# Start of route
label {{package_entrypoint}}_vriska:

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
    show vriska neutral4
    play music "music/WORST_END.wav" loop
    hide blackcover with dissolve

    # Write dialogue!
    vr neutral3 "Hey. Hey. Over here."
    vr ngreen "8itch."

    hide vriska  # goodbye

    # You can also use assets that have already been definied in other pesterquest routes directly!
    show bg gamzeehive
    show gamzee pie1
    gam pie1 "cAn I oFfEr YoU a PiE iN tHeSe TrYiNg TiMeS"
    # Be careful about naming your resources so they don't conflict with other ones. 
    # I help where I can by offering the substitutions like {{package_id}}.

    # Show end card
    call ending pass ("vriska end", True, True)
    return
