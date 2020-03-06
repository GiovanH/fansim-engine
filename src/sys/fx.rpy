python:
    """
    Graphical effects:
        Toast notifications
        Toast music boxes
        
    """


init offset = 0

# Toast transformations

transform toast_down(l=0.3):
    # Sticks until hidden.
    on show:
        yanchor 1.0
        linear l yanchor 0.0
    on hide:
        linear l yanchor 1.0

transform toast_up(l=0.3):
    # Sticks until hidden.
    on show:
        yanchor 0.0
        linear l yanchor 1.0
    on hide:
        linear l yanchor 0.0

transform toast_peek_down(p=2.0, l=0.3):
    # Hides itself after p seconds.
    yanchor 1.0
    linear l yanchor 0.0
    pause p
    linear l yanchor 1.0

transform toast_peek_up(p=2.0, l=0.3):
    # Hides itself after p seconds.
    yanchor 0.0
    linear l yanchor 1.0
    pause p
    linear l yanchor 0.0

transform toast_flyby:
    # Is this even a toast anymore?
    yanchor 0.0
    xanchor 1.0
    xpos 0
    parallel:
        linear 0.5 xanchor 0.0
    parallel:
        easein 0.5 xpos 100
        xpos 100
        linear 0.6 xpos 300
        xpos 300
        easeout 0.5 xpos 1280

# Music telop as toast

# style music_toast_frame:
#     background Solid("#D4D4D4")

style music_toast_title:
    size 36 

style music_toast_artist:
    size 22

style music_toast_album is music_toast_artist

screen MusicToast:
    ### A toast notification to indicate a new music track.
    ### This is only a visual. This does not change the music.
    ### Strings support format tags, including links.
    ### Recommended usage is to set tf to toast_down if you want it to be interactable.
    ### 
    ### Args:
    ###     tf (transformation): The animation used
    ###     albumart (displayable): Displayable album art
    ###     title (string): Song title
    ###     artist (string): Song artist
    ###     album (string): Song album name
    ### Advanced
    ###     ttitle (string): Template format strings for title
    ###     tartist = Template format strings for artist
    ###     talbum = Template format strings for album

    default tf = toast_peek_down
    default style = "music_toast"

    default albumart = "{{assets}}/itunes.png"
    default title = "TITLE"
    default artist = "ARTIST"
    default album = "ALBUM"

    default ttitle = "[title]"
    default tartist = "{color=aaa}by{/color} [artist]"
    default talbum = "{color=aaa}from{/color} [album]"
    default albumartsize = (96, 96)

    frame:
        style_prefix style
        hbox:
            add albumart size albumartsize
            null width 6
            vbox:
                text ttitle style_suffix "title"
                text tartist style_suffix "artist"
                text talbum style_suffix "album"
        at tf

define quickfade = Dissolve(0.1)
define zapfade = Dissolve(0.2)
define slowzapfade = Dissolve(0.4)
define quickmove = MoveTransition(0.2)

# a bunch of stabby and hurty animation
define stab = Fade(.08, 0.0, .2, color="#FF0000")
define redstab = Fade(0.09, 0.09, 0.15, color="#FF0000")
define pinkflash = Fade(0.05, 0.05, 0.35, color="#ff82d9")
define slowpinkflash = Fade(0.35, 0.35, 0.65, color="#ff82d9")
define bluestab = Fade(0.09, 0.25, 0.25, color="#0000AA")
define olivestab = Fade(0.09, 0.25, 0.25, color="#416600")

define slowmove = MoveTransition(1.0)

# close/open eyes
define closeeyes = ImageDissolve("eye.png", 0.8, ramplen=128, reverse=True, time_warp=eyewarp)
define openeyes = ImageDissolve("eye.png", 0.8, ramplen=64, time_warp=eyewarp)

define pushrighthard = PushMove(0.3, "pushright")
define quickfade = Dissolve(0.1)
define zapfade = Dissolve(0.2)
define slowzapfade = Dissolve(0.4)
define quickmove = MoveTransition(0.2)



## COMMON TRANSFORMS ##

transform bounce:
    ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730

transform lowerbounce:
    ypos 780
    easeout 0.12 ypos 766
    linear 0.12 ypos 780

transform bouncetwice:
    ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730
    pause(0.2)
    easeout 0.12 ypos 716
    linear 0.12 ypos 730

transform quickbouncetwice:
    ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730

transform nod:
    ypos 730
    easeout 0.12 ypos 742
    linear 0.12 ypos 730

transform nodding:
    ypos 730
    easeout 0.12 ypos 742
    linear 0.12 ypos 730
    pause(0.1)
    easeout 0.15 ypos 742
    linear 0.15 ypos 730
    pause(0.1)
    repeat

transform slownodding:
    ypos 730
    easeout 0.3 ypos 742
    linear 0.3 ypos 730
    pause(0.25)
    easeout 0.32 ypos 742
    linear 0.32 ypos 730
    pause(0.25)
    repeat

transform lowernod:
    ypos 780
    easeout 0.12 ypos 792
    linear 0.12 ypos 780

transform nodtwice:
    ypos 730
    easeout 0.12 ypos 742
    linear 0.12 ypos 730
    pause 0.5
    easeout 0.15 ypos 742
    linear 0.15 ypos 730

transform quicknodtwice:
    ypos 730
    easeout 0.12 ypos 742
    linear 0.12 ypos 730
    pause(0.1)
    easeout 0.15 ypos 742
    linear 0.15 ypos 730

transform slownod:
    ypos 730
    easeout 0.3 ypos 742
    pause 0.5
    linear 0.2 ypos 730

transform slowishnod:
    ypos 730
    easeout 0.27 ypos 742
    linear 0.2 ypos 730

transform lower:
    xpos 640 ypos 780

transform lowerbounce:
    ypos 780
    easeout 0.12 ypos 766
    linear 0.12 ypos 780

transform lowerhighbounce:
    ypos 780
    easeout 0.12 ypos 740
    linear 0.12 ypos 780
transform twitch:
    ypos 730 xpos 640
    easein 0.06 ypos 736 xpos 644
    linear 0.06 ypos 730 xpos 640

transform shudder:

    xpos 640
    linear 0.04 xpos 637
    linear 0.04 xpos 640
    linear 0.04 xpos 643
    linear 0.04 xpos 640
    repeat 4

transform lowered:
    ypos 730
    linear 0.75 ypos 765

transform loweredtodefault:
    ypos 765
    linear 0.3 ypos 730

transform loweredpos:
    ypos 765

transform loweredbrief:
    ypos 730
    pause 0.05
    linear 0.75 ypos 765
    pause 1.8
    linear 1.35 ypos 730

transform loweredbounce:
    ypos 765
    easeout 0.12 ypos 751
    linear 0.12 ypos 765

transform smalllower:
    ypos 730
    linear 0.15 ypos 736

transform smalllowertodefault:
    ypos 736
    linear 0.14 ypos 730

transform smalllowerpos:
    ypos 736

transform sitting:
    xpos 640 ypos 850

transform leftsitting:
    xpos 360 ypos 850

transform rightsitting:
    xpos 960 ypos 850

transform sitsigh:
    ypos 850 xpos 640
    easein 0.4 ypos 845
    easeout 0.6 ypos 850

transform sittingnod:
    ypos 850 xpos 640
    easein 0.4 ypos 845
    easeout 0.6 ypos 850

transform bouncing:
    ypos 730
    linear 0.1 ypos 720
    linear 0.1 ypos 730
    repeat

transform shaking:
    ypos 730
    linear 0.07 ypos 732
    linear 0.07 ypos 730
    repeat

transform bgshaking:
    ypos 720
    linear 0.07 ypos 722
    linear 0.07 ypos 720
    repeat

transform shakes:
    ypos 730
    linear 0.07 ypos 732
    linear 0.07 ypos 730
    repeat 3

transform shuddering:

    xpos 640
    linear 0.04 xpos 637
    linear 0.04 xpos 640
    linear 0.04 xpos 643
    linear 0.04 xpos 640
    repeat

transform sigh:
    ypos 730
    easein 0.4 ypos 725
    easeout 0.6 ypos 730

transform breathe:
    ypos 730
    easein 1 ypos 720
    easeout 1.1 ypos 730

transform breathein:
    ypos 730
    easein 1 ypos 720

transform breatheout:
    ypos 720
    easeout 1.1 ypos 730

transform breathing:
    easein 1 ypos 720
    easeout 1.1 ypos 730
    pause(1.0)
    repeat

transform outofbreath:
    ypos 730
    easein 0.4 ypos 724
    pause(0.1)
    easeout 0.5 ypos 730
    pause(0.5)
    easein 0.4 ypos 724
    pause(0.1)
    easeout 0.5 ypos 730
    pause(0.4)
    repeat

#transforms to indicating speaking character(s)
transform speaking:
    easein 0.1 zoom 1.01

transform stopspeaking:
    easein 0.1 zoom 1

transform leftspeaking:
    ypos 730 xpos 360
    easein 0.1 zoom 1.01

transform rightspeaking:
    ypos 730 xpos 960
    easein 0.1 zoom 1.01

transform speakbounce:
    parallel:
        easein 0.1 zoom 1.01
    parallel:
        ypos 730
        easeout 0.12 ypos 716
        linear 0.12 ypos 730

transform speaknod:
    parallel:
        easein 0.1 zoom 1.01
    parallel:
        ypos 730
        easeout 0.12 ypos 742
        linear 0.12 ypos 730

transform speakingtodefault:
    parallel:
        easein 0.1 zoom 1.01
    parallel:
        ypos 736
        linear 0.14 ypos 730

transform stopspeakingtodefault:
    parallel:
        easein 0.1 zoom 1
    parallel:
        ypos 736
        linear 0.14 ypos 730

transform driving:
    ypos 720
    linear 0.07 ypos 722
    linear 0.07 ypos 720
    repeat

transform highbounce:
    ypos 730
    easeout 0.12 ypos 690
    linear 0.12 ypos 730

transform lowbounce:
    ypos 730
    easeout 0.09 ypos 725
    linear 0.09 ypos 730

transform passenger:
    ypos 730 xpos 900 zoom 1.2

transform flipped:
    xzoom -1.0

transform fallen:
    xpos 640 ypos 1000

transform leftfallen:
    xpos 360 ypos 1000

#Quickly push sprite to side of screen
transform shoveright:

    linear 0.1 xpos 960

transform shoveleft:

    xpos 640
    linear 0.1 xpos 320

transform shoveoffleft:

    linear 0.1 xpos -320

#Quickly push sprite to default position, from offscreen bottom
transform shoveup:

    xpos 640 ypos 1440
    linear 0.1 ypos 730

transform bobbing:
    ypos 730
    easeout 0.12 ypos 738
    linear 0.12 ypos 730
    pause 0.2
    easeout 0.12 ypos 738
    linear 0.12 ypos 730
    pause 0.8
    repeat
