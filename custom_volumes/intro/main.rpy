# Define characters

image {{p}}_greenscreen = Solid(hemospectrum("cerulean")["hex"])
# "{{assets}}/greenscreen.png"

image {{p}}_namelabel = Text(
    "VRISKA\nSERKET", 
    color="#FFF", size=180, font="{{assets}}/LargoD.ttf", line_spacing=-40
)

transform {{p}}_char_pos:
    xpos 240

transform {{p}}_namelabel_pos:
    yanchor 0.5
    xanchor 0.5
    yalign 0.5
    xalign 0.9

# Start of route
label {{package_entrypoint}}_route:

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
    show {{p}}_greenscreen behind vriska with Dissolve(0.1)
    show vriska at {{p}}_char_pos  with ease

    show {{p}}_namelabel at {{p}}_namelabel_pos with Dissolve(0.1) 

    $ renpy.pause(8.0)
    
    $ quick_menu = True
    vr "Introducing vriska"

    hide vriska
    hide {{p}}_greenscreen

    # Show end card
    call ending pass ("{{p}}_greenscreen", True, True)
    return
