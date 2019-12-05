# Define characters

image __p___greenscreen = Solid(hemospectrum("cerulean")["hex"])
# "{{assets}}/greenscreen.png"

image __p___namelabel = Text(
    "VRISKA\nSERKET", 
    color="#FFF", size=180, font="{{assets}}/LargoD.ttf", line_spacing=-40
)

transform __p___char_pos:
    ease 0.4 xpos 240

transform __p___namelabel_pos:
    yanchor 0.5
    xanchor 0.5
    yalign 0.5
    xalign 0.9

# Start of route
label __package_entrypoint___route:

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

    "rollback"
    $ quick_menu = False
    $ renpy.pause(0.2)

    show vriska neutral1 
    $ renpy.pause(0.9)
    show vriska neutral2 with Dissolve(0.1)
    $ renpy.pause(0.9)
    show vriska neutral3 with Dissolve(0.1)
    $ renpy.pause(0.9)

    show vriska neutral1 with Dissolve(0.1)

    show vriska at brushright
    show __p___greenscreen behind vriska with Dissolve(0.1)
    show vriska at shoveright
    show vriska at __p___char_pos

    show __p___namelabel at __p___namelabel_pos with Dissolve(0.1) 

    $ renpy.pause(8.0)
    
    $ quick_menu = True
    vr "Introducing vriska"

    hide vriska
    hide __p___greenscreen

    # Show end card
    call ending pass ("__p___greenscreen", True, True)
    return
