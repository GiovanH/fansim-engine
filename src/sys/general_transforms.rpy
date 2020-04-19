## COMMON TRANSFORMS ##

# Basic placement

transform default:
    xalign 0.5
    ypos 0

transform height(y):
    ypos y

transform xpos(x):
    xpos x

transform sitting:
    ### Lower position
    xpos 640 ypos 850

transform leftsitting:
    ### Lower left position
    xpos 360 ypos 850

transform rightsitting:
    ### Lower right position
    xpos 960 ypos 850

transform leftfallen:
    xpos 360 ypos 1000

transform passenger:
    xpos 900 zoom 1.2

transform flipped:
    xzoom -1.0

transform fallen:
    ypos 1000


# General movement, action

transform shoveright:
    ### Quickly push sprite to right side of screen
    linear 0.1 xpos 960

transform shoveleft:
    ### Quickly push sprite to left side of screen
    xpos 640
    linear 0.1 xpos 320

transform shoveoffleft:
    ### Quickly push sprite off left side of screen
    linear 0.1 xpos -320

transform shoveup:
    ### Quickly push sprite to default position, from offscreen bottom
    yoffset 720
    linear 0.1 yoffset 0



# Nodding, bouncing

transform bounce(height=12, pause=0.2, repeat=0):
    ### Small bounce up, then immeditately reset.
    ### Negative numbers bounce down.
    block:
        easeout 0.12 yoffset -height
        linear 0.12 yoffset 0
        pause(pause)
        repeat repeat

transform nod(height=12, delay=0.0, speed=0.12, pause=0.2, repeat=0):
    ### Small nod down, delay, then reset.
    ### Negative numbers nod up.
    block:
        easeout speed yoffset -height
        pause(delay)
        linear speed yoffset 0
        pause(pause)
        repeat repeat

transform bouncing:
    yoffset 0
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0
    repeat

transform bobbing:
    yoffset 0
    easeout 0.12 yoffset 8
    linear 0.12 yoffset 0
    pause 0.2
    easeout 0.12 yoffset 8
    linear 0.12 yoffset 0
    pause 0.8
    repeat

transform driving:
    ### Slow bounce, as if from a car, repeating
    yoffset 0
    linear 0.07 yoffset 2
    linear 0.07 yoffset 0
    repeat
# Twitching, shuddering

transform twitch:
    easein 0.06 xoffset 6 xoffset 4
    linear 0.06 yoffset 0 xoffset 0

transform shudder:
    # X-shaking
    xoffset 0
    linear 0.04 xoffset -3
    linear 0.04 xoffset 0
    linear 0.04 xoffset 3
    linear 0.04 xoffset 0
    repeat 4

transform shuddering:
    ### X-shaking, looped
    xoffset 0
    linear 0.04 xoffset -3
    linear 0.04 xoffset 0
    linear 0.04 xoffset 3
    linear 0.04 xoffset 0
    repeat

transform shaking:
    yoffset 0
    linear 0.07 yoffset 2
    linear 0.07 yoffset 0
    repeat

# Breathing, panting, sighing

transform sigh:
    ### Small vertical breath
    yoffset 0
    easein 0.4 yoffset -5
    easeout 0.6 yoffset 0

transform breathe:
    ### Deep breath, vertical.
    yoffset 0
    easein 1 yoffset -10
    easeout 1.1 yoffset 0

transform breathein:
    yoffset 10
    easein 1 yoffset 0

transform breatheout:
    yoffset 0
    easeout 1.1 yoffset 10

transform breathing:
    easein 1 yoffset 0
    easeout 1.1 yoffset 10
    pause(1.0)
    repeat

transform outofbreath:
    yoffset 10
    easein 0.4 yoffset 4
    pause(0.1)
    easeout 0.5 yoffset 10
    pause(0.5)
    easein 0.4 yoffset 4
    pause(0.1)
    easeout 0.5 yoffset 10
    pause(0.4)
    repeat

# Transforms to indicating speaking character(s)

transform speaking:
    easein 0.1 zoom 1.01

transform stopspeaking:
    easein 0.1 zoom 1

transform speakbounce:
    parallel:
        easein 0.1 zoom 1.01
    parallel:
        yoffset 0
        easeout 0.12 yoffset -14
        linear 0.12 yoffset 0

transform speaknod:
    parallel:
        easein 0.1 zoom 1.01
    parallel:
        yoffset 10
        easeout 0.12 yoffset 22
        linear 0.12 yoffset 10

transform speakingtodefault:
    parallel:
        easein 0.1 zoom 1.01
    parallel:
        yoffset 16
        linear 0.14 yoffset 10

transform stopspeakingtodefault:
    parallel:
        easein 0.1 zoom 1
    parallel:
        yoffset 16
        linear 0.14 yoffset 10

# Utility
transform invisible:
    alpha 0.0