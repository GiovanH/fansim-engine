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
