python:
    """
    Graphical effects:
        Toast notifications
        Toast music boxes
        
    """


init offset = 0

# Toast transformations

transform toast_down(l=0.3):
    ### Push up, sticks until hidden.
    on show:
        yanchor 1.0
        linear l yanchor 0.0
    on hide:
        linear l yanchor 1.0

transform toast_up(l=0.3):
    ### Push up, sticks until hidden
    on show:
        yanchor 0.0
        linear l yanchor 1.0
    on hide:
        linear l yanchor 0.0

transform toast_left(l=0.3):
    ### Push up, sticks until hidden.
    on show:
        xanchor 1.0
        linear l xanchor 0.0
    on hide:
        linear l xanchor 1.0

transform toast_right(l=0.3):
    xpos 1.0
    ### Push up, sticks until hidden
    on show:
        xanchor 0.0
        linear l xanchor 1.0
    on hide:
        linear l xanchor 0.0

transform toast_peek_down(p=2.0, l=0.3):
    ### Push down, hides itself after p seconds.
    yanchor 1.0
    linear l yanchor 0.0
    pause p
    linear l yanchor 1.0

transform toast_peek_up(p=2.0, l=0.3):
    ### Push down, hides itself after p seconds.
    yanchor 0.0
    linear l yanchor 1.0
    pause p
    linear l yanchor 0.0

transform toast_flyby:
    ### An elaborate "fly by" style animation
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
