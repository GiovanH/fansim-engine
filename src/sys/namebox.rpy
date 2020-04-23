python:
    """
    Namebox code.

    The FSE nameboxes provide an alternative to the way WP handles nameboxes,
    drastically simplifying the process of defining and using characters.

    This also provides helper functions for constructing and displaying
    the grype interface. A reusable example is provided here:

    >>> image !vriska grype neutral = GrypeMasked("vriska neutral1")
    >>> image !vriska grype pose2 = GrypeMasked("vriska pose2")
    >>> image grype_frame __p__vriska = GrypeFrame(
    >>>         handle="arachnidsGrip",
    >>>         blood="cerulean", 
    >>>         avatar="{{assets}}/vriskagrype.png"
    >>>     )
    >>> 
    >>> label script:
    >>>     show grype_frame __p__vriska
    >>>     show !vriska grype neutral 
    >>>     !.vr "Dialogue"
    >>>     show !vriska grype pose2 
    >>>     !.vr "Dialogue"
    >>>     hide !vriska 
    >>>     hide grype_frame


    The following magic ids for styling are allowed:
        "show", "cb", "what", "window", "who", "namebox", "say_dialogue"

    """



init offset = 0

# Pesterchum
style pesterchum_namelabel is say_label
# style pesterchum_namelabel:
#     pass

screen pesterchum_say:
    style_prefix "say"
    default big = False
    if big:
        window:
            id "window"
            background "gui/textbox_pesterlog_large.png"
            text what id "what" ypos 34 line_spacing 2
    else: 
        window:
            id "window"
            background "gui/textbox_pesterlog.png"
            if who is not None:
                window:
                    id "namebox"
                    style "namebox"
                    text ":: " + who + " ::" id "who" color '#FFF'
            text what id "what" ypos 65

define pesterchum = Character(
    ### A standard human, using the yellow pesterchum template.
    ### The chumhandle is automatically formatted ":: [name] ::"
    ###
    ### Args:
    ###     name (string): chumhandle, i.e. "arachnidsGrip"
    ###     image (string): Base image name for character poses
    ###     what_color (html color): Hexadecimal color code.
    ### Extra args:
    ###     big (boolean): Hide the name label to provide more space for text.
    ###     >>> !john "Dialogue" (show_big=True)
    screen="pesterchum_say", who_style="pesterchum_namelabel",
    # Characters will need to set these attributes manually:
    name="chumHandle", what_color='#e00707', image="john"
)


# Trollean
style trollian_namebox is namebox:
    xpos 24
    xanchor 0

style trollian_namelabel is say_label:
    ypos 16
    xalign 0.0
    size 17

style trollian_dialogue is say_dialogue:
    xpos 44

screen trollian_say:
    style_prefix "say"
    default blood = "gray"
    default big = False
    window:
        id "window"
        xsize 793
        background Composite(
            (793, 194),
            (0, 0), "{{assets_common}}/trollian_bg_" + ("large" if big else "small") + ".png",
            (0, 0), doTint(
                "{{assets_common}}/trollian_" + ("large" if big else "small") + "_rim.png",
                hemospectrum(blood), 200.0
            )
        )
        if big:
            text what id "what" ypos 34 line_spacing 2 color hemospectrum(blood)
        else:
            if who is not None:
                window:
                    id "namebox"
                    style "trollian_namebox"
                    text "trolling: " + who id "who"
            text what id "what" ypos 65 color hemospectrum(blood)

define trollian = Character(
    ### A standard troll, using the red "trollian" template.
    ### The trolltag is automatically formatted "trolling: [name]"
    ### The decorations are colored based on the show_blood argument. 
    ###
    ### Args:
    ###     name (string): Trolltag, i.e. "arachnidsGrip"
    ###     image (string): Base image name for character poses
    ###     show_blood (blood name): Blood hue name OR hexadecimal color code.
    ### Extra args:
    ###     big (boolean): Hide the name label to provide more space for text.
    ###     >>> !vriska "Dialogue" (show_big=True)
    color='#FFFFFF', who_style="trollian_namelabel", screen="trollian_say", what_style="trollian_dialogue",
    # Characters will need to set these attributes manually:
    name="trollTag", image="", show_blood="gray"
)

# Hiveswap
style hiveswap_namebox is namebox:
    xalign 0.0
    xpos 71
    ypos -56

style hiveswap_namelabel is say_label:
    # yalign 0.5
    xalign 0.0
    yalign 1.0
    size 42

style hiveswap_dialogue is say_dialogue:
    size 26
    xpos 123
    ypos 28
    xmaximum 720

screen hiveswap_say:
    style_prefix "say"
    default blood = "gray"
    window:
        id "window"
        yalign 1.0
        xsize 926
        ysize 175
        # ypos 744

        background doTint(
            "{{assets_common}}/hiveswap_textbox_base.png",
            hemospectrum(blood), 200.0
        )

        if who is not None:
            window:
                id "namebox"
                style "hiveswap_namebox"
                text who id "who" color '#FFF' font "Berlin Sans FB Demi Bold.ttf" outlines [(4, hemospectrum(blood))]
        text what id "what" color '#FFF' font "Berlin Sans FB Regular.ttf"

define hiveswap = Character(
    ### A standard troll, using the hexagonal "hiveswap" template.
    ### The textbox and outlines are colored based on the show_blood argument.
    ### n.b. Hiveswap uses alternate versions of some background colors for readability.
    ### These are availible as burgundy_fs, bronze_fs, and indigo_fs.
    ### Use this with kind=hiveswap
    ###
    ### Args:
    ###     name (string): Trolltag, i.e. "arachnidsGrip"
    ###     image (string): Base image name for character poses
    ###     show_blood (blood name): Blood hue name OR hexadecimal color code.
    color='#FFFFFF', screen="hiveswap_say",
    who_style="hiveswap_namelabel", 
    what_style="hiveswap_dialogue",
    # Characters will need to set these attributes manually:
    name="NAME", image="", show_blood="gray"
)

# Openbound

style openbound_namebox is namebox:
    xpos 0
    xanchor 0
    ypos -52

style openbound_namelabel is say_label:
    # yalign 0.5
    xalign 0.0
    size 42
    yalign 1
    ypos 2
    

style openbound_dialogue is say_dialogue:
    size 26
    xpos 44
    ypos 30
    xmaximum 720

screen openbound_say:
    # See sandbox for examples
    style_prefix "say"
    default blood = "gray"
    default hashtags = ""
    default obstyle = "pixel"
    default chuckle = False
    default use_nameframe = False
    default frame_border_size = 21  # Parameter for the Frame object

    default hashtag_lines = 1
    default sandwich = False
    default sandwich_overlap = 0  # How much to overlap the windows in sandwhich mode
    default hashtag_line_height = 21  # Height of each line of text, in pixels
    default hashtag_height_offset = -10  # Manual offset to adjust around borders

    default total_ysize = 225

    $ hashbar_ysize = frame_border_size*2 + (hashtag_line_height * hashtag_lines) + hashtag_height_offset
    $ say_dialogue_ysize = total_ysize - hashbar_ysize if sandwich else total_ysize
    $ say_dialogue_yoffset = sandwich_overlap - hashbar_ysize if sandwich else 0

    $ purple = "#6600DA"

    $ chucklefix = ("_chuckle" if chuckle else "")
    $ textbox_bg_frame = Frame("{{assets_common}}/openbound_textbox_" + obstyle + chucklefix + ".png", left=frame_border_size, top=frame_border_size)
    $ hashbox_bg_frame = Frame("{{assets_common}}/openbound_hashbox_" + obstyle + chucklefix + ".png", left=frame_border_size, top=frame_border_size)
    $ who_color = purple if chuckle else hemospectrum(blood)
    $ who_outlines = [(0 if use_nameframe else 4, "#FFF")] 

    window:
        id "ob"
        style "default"
        xalign 0.5
        yalign 1.0

        xsize 793

        window:
            id "say_dialogue"
            yalign 1.0
            yoffset say_dialogue_yoffset
            xfill True
            ysize say_dialogue_ysize
            background textbox_bg_frame
            if chuckle:
                text what id "what" color purple font "{{assets_common}}/BONEAPA.TTF" size 48
            else:
                text what id "what" color hemospectrum(blood)
            if who is not None:
                window:
                    id "namebox"
                    style "openbound_namebox"
                    if use_nameframe:
                        padding (24, 8)
                        background hashbox_bg_frame
                    text who id "who" color who_color outlines who_outlines

        if hashtags:
            window:
                id "tagbox"
                style "default"
                yalign 1.0

                xfill True
                ysize hashbar_ysize
                 
                background hashbox_bg_frame 

                text "[hashtags]": #tags:
                    style "default"
                    yalign 0.5
                    pos (44, 0)
                    color (purple if chuckle else "#000")  # hemospectrum(blood)
                    line_spacing 0
                    size 18

init python:
    NotSet = renpy.object.Sentinel("NotSet")
    class HtagChar(ADVCharacter):
        def __init__(self, name=NotSet, kind=None, quirklist=[], *args, **kwargs):
            super(type(self), self).__init__(name=name, kind=kind, *args, **kwargs)
            self.quirklist = quirklist

        def __call__(self, what, *args, **kwargs):
            hashtags = kwargs.get("show_hashtags")
            what_text = quirkSub(self.quirklist, what)
            if hashtags:
                k2 = kwargs.copy()
                k2.pop("show_hashtags")

                super(type(self), self).__call__(what_text + "{p=0.1}{nw}", *args, **k2)
                self.do_extend()
                super(type(self), self).__call__(what_text + "{fast}", *args, **kwargs)
                self.do_done(self.name, hashtags)
            else:
                super(type(self), self).__call__(what_text, *args, **kwargs)

define openbound = HtagChar(
    ### A character who speaks with an openbound-style textbox.
    ### Elements can be restyled and repositioned using the standard what, namebox, and say_dialogue tags.
    ###
    ### Args:
    ###     name (string): Character name, i.e. "Vriska"
    ###     image (string): Base image name for character poses
    ###     show_blood (blood name): Blood hue name OR hexadecimal color code.
    ### Extra args:
    ###     hashtags (string): Hashtags to show.
    ###     Unlike openbound, the tag bar is only shown when `hashtags` is not empty.
    ###     To simulate an empty bar, set the default hashtag value to " " using show_hashtags=" " in the character definition.
    ###     hashtag_lines (int): Number of lines of text to allocate hashtag space for
    ###     sandwich (bool): (Default False) Show stacked text and hashtags, instead of overlapping.
    ###     >>> !vriska "Dialogue" (show_hashtags="#;;;;)")
    ###     
    ###     chuckle (boolean): Use chucklevoodoo mode.
    ###     When this is set, textboxes will have purple and black coloring, and the font will be in large bones.
    ###     >>> !vriska "Dialogue" (show_chuckle=True)
    screen="openbound_say", what_style="openbound_dialogue", who_style="openbound_namelabel"
)
define openround = Character(
    ### Interface is the same as openbound.
    ### This is a shortcut that only changes the show_obstyle parameter.
    kind=openbound, show_obstyle="round"
)


screen chan_say:
    ### 4chan-style textbox, based on mituna's from openbound. Supports attachments.
    ### Unlike other characters, this is not a "kind", but a screen.
    ### Use this with Character("Mituna", screen="chan_say")
    ### For automatic greentext, wrap this in a quirksayer: quirkSayer(Character("Mituna", screen="chan_say"), "greentext")
    ###
    ### Args:
    ###     show_blood (blood name): Blood hue name OR hexadecimal color code. Defaults to black text.
    ###     show_attachment (displayable, optional): Shows a zoomable attachment as part of the "post"
    
    style_prefix "say"
    default blood = "#000"
    default attachment = None
    default who = "Anonymous"

    window:
        id "window"
        background Frame(
            "{{assets_common}}/4chan_textbox.gif",
            left=28, top=28
        )
        xsize 796
        right_padding 20 
        text who id "who" xpos 40 ypos 18 color "#117743" xanchor 0 
        hbox:
            xpos 10
            ypos 30
            spacing 20
            if attachment is not None:
                button:
                    image scaleBestFit(attachment, 150, 150) xpos 0 ypos 0
                    action NullAction()
                    tooltip scaleBestFit(attachment, 700, 500)
            text what id "what" xpos 0 ypos 0 xsize 800 color hemospectrum(blood)

    $ tooltip = GetTooltip()

    if tooltip:
        frame:
            xpos 300 
            ypos 550 
            yanchor 1.0 
            background Solid("D6DAF0")
            image tooltip 

# Grype UI for hiveswap

image grype_alpha = "{{assets_common}}/grype_alpha.png"
image !grype_avatar_alpha = "{{assets_common}}/grype_avatar_alpha.png"

style grype_namelabel is hiveswap_namelabel:
    xanchor 0.5
    yanchor 1.0


transform grype_namelabel_pos:
    # size (660, 660)
    rotate -49 around (0.5, 0)


init python:
    def GrypeMasked(displayable):
        """Returns a displayable masked for grype.
        >>> image !vriska grype neutral = GrypeMasked("vriska neutral1")
        """
        return AlphaMask(displayable, "grype_alpha")

    def GrypeFrame(blood, handle, avatar="__p__grype_avatar_alpha"):
        """Creates a dynamic grype frame for a character.
        Args:
            blood (hemospectrum): Blood color
            handle (string): The displayed grype handle
            avatar (displayable): The avatar image. See grype_avatar_alpha for a template.
        """
        
        # the worst thing ever: anchor is broke on At()
        handledisp = Text(handle, color='#FFF', font="Berlin Sans FB Demi Bold.ttf", outlines=[(4, hemospectrum(blood))])
        square_size = max(*handledisp.size())
        handlex, handley = (298-int(square_size/2), 128-int(square_size/2))

        return Composite(
            (1280, 720),
            (956, 23), AlphaMask(
                im.Scale(avatar, 112, 112), "__p__grype_avatar_alpha"
            ),
            (0, 0), doTint(
                "{{assets_common}}/grype.png", hemospectrum(blood), 200.0
            ),
            (handlex, handley), At(handledisp, grype_namelabel_pos)
        )
