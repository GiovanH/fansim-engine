# Define characters

image {{p}}_greenscreen = "{{assets}}/greenscreen.png"

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

    show vriska neutral1 
    $ renpy.pause(1.0)
    show vriska neutral2 with Dissolve(0.1)
    $ renpy.pause(1.0)
    show vriska neutral3 with Dissolve(0.1)
    $ renpy.pause(1.0)

    show vriska neutral1 with Dissolve(0.1)

    show {{p}}_greenscreen behind vriska with dissolve
    show vriska at right1280 with ease
    show vriska at left1280 with ease

    $ renpy.pause(2.0)
    
    vr "Introducing vriska"

    hide vriska
    hide {{p}}_greenscreen

    # Show end card
    call ending pass ("{{p}}_greenscreen", True, True)
    return
