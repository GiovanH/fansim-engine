init offset = 0

# Trollean
style trollean_namebox:
    properties gui.text_properties("name", accent=True)
    yalign 0.5
    xalign 0.0
    xpos -365
    ypos 16
    size 17

define trollean = Character(
    color='#FFFFFF', who_style="trollean_namebox", who_prefix="trolling: ",
    # Characters will need to set these attributes manually:
    name="trollTag", image="", window_background="gui/textbox_trollian_teal.png"
)

# Pesterchum
style pesterchum_namebox:
    properties gui.text_properties("name", accent=True)
    yalign 0.5
    xalign 0.5
    xpos 0

define pesterchumstart = Character(
    who_prefix=":: ", who_suffix=" ::", who_style="pesterchum_namebox",
    color='#FFFFFF', what_ypos=53, 
    # Characters will need to set these attributes manually:
    name="chumHandle", image="", what_color='#e00707', window_background="gui/textbox_pesterlog.png"
)
define pesterchum = Character(
    "", color='#FFFFFF', window_background="gui/textbox_pesterlog_large.png", 
    what_ypos=22, what_line_spacing=2,
    # Characters will need to set these attributes manually:
    what_color='#e00707', image=""
)

# Hiveswap
style hiveswap_namebox:
    properties gui.text_properties("name", accent=True)
    yalign 0.5
    xalign 0.0
    xpos -380
    ypos -34
    size 42

style hiveswap_textbox:
    properties gui.text_properties("dialogue")
    size 26
    xpos 300
    ypos 26
    xmaximum 720

define hiveswap = Character(
    color='#FFFFFF', what_color='#FFFFFF', 
    who_style="hiveswap_namebox", who_font="Berlin Sans FB Demi Bold.ttf",
    what_style="hiveswap_textbox", what_font="Berlin Sans FB Regular.ttf", 
    window_ypos=744, 
    # Characters will need to set these attributes manually:
    name="NAME", image="", window_background="gui/textbox_olive.png", who_outlines=[(4, "#416600")]
)

# Openbound
style openbound_namebox:
    properties gui.text_properties("name", accent=True)
    yalign 0.0
    xalign 0.0
    xpos -380
    ypos -52
    size 42
    outlines [(4, "#FFF")]
    color "#00baff"

style openbound_textbox:
    properties gui.text_properties("dialogue")
    size 26
    xpos 292
    ypos 30
    xmaximum 720

screen openbound_say:
    style_prefix "say"
    default color = "#000"
    default hashtags = ""
    default obstyle = "pixel"
    default chuckle = False

    default purple = "#6600DA"

    default chucklefix = ("_chuckle" if chuckle else "")
    default tagcolor = (purple if chuckle else "#000")

    window:
        id "ob"
        background "{{assets_common}}/openbound_textbox_" + obstyle + chucklefix + ".png"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who" style "openbound_namebox" color color

        if chuckle:
            text what id "what" style "openbound_textbox" color purple font "{{assets_common}}/BONEAPA.TTF" size 48
        else:
            text what id "what" style "openbound_textbox" color color

        if hashtags:
            vbox:
                image "{{assets_common}}/openbound_hashbox_" + obstyle + chucklefix + ".png":
                    pos(0, 142)

                text "[hashtags]": #tags:
                    pos(292, 106)
                    color tagcolor
                    line_spacing 0
                    size 18

define openbound = Character(
    screen="openbound_say", what_style="openbound_textbox", who_style="openbound_namebox"
)
define openround = Character(
    screen="openbound_say", what_style="openbound_textbox", who_style="openbound_namebox",
    show_obstyle="round"
)
# Examples using these templates instead of the vanilla method:
# define jostart = Character(name="ectoBiologist", kind=pesterchumstart, what_color='#0715cd', image="john")
# define jo = Character(kind=pesterchum,  what_color='#0715cd', image="john")
# define vr = Character(name="arachnidsGrip", kind=trollean, what_color='#005682', image="vriska", window_background="gui/textbox_trollian_cobalt.png")
# define bo = Character(name="BOLDIR", kind=hiveswap, image="boldir", window_background="gui/textbox_olive.png", who_outlines=[(4, "#416600")])

# Alternate narrators:

define narrator_dirk = Character(kind=narrator, what_color='#F2A400', what_font="AGaramondPro-Regular.otf", what_size=26)
define narrator_calliope = Character(kind=narrator, what_color='#F00', what_font="AGaramondPro-Regular.otf", what_size=26)
define narrator_prattle = Character(kind=narrator, what_color='#000', what_font="AGaramondPro-Regular.otf", what_size=26)


# Automatic quirk translation

init python:
    import re

    quirks = {
        "gamzee": [("([a-zA-Z])([a-zA-Z]?)", lambda m: m.group(1).lower() + m.group(2).upper())],
        "kankri": [("[Bb]", "6"), ("[Oo]", "9")],
        "lower": [("(.+)", lambda m: m.group(1).lower())],
        "upper": [("(.+)", lambda m: m.group(1).upper())]
    }

    def quirkSayer(who, quirk):
        def _sayer(what, amt=0, stmt=None, **kwargs):
            return quirkSay(who, quirk, what)
        return _sayer

    def quirkSay(who, quirk, what, **kwargs):
        return who(quirkSub(quirk, what), **kwargs)

    def quirkSub(quirk, what):
        quirksubs = quirks.get(quirk.lower(), None)
        if not quirksubs:
            if renpy.config.developer:
                raise Exception("ERROR: No quirk {}".format(quirk))
            return what
        for (pattern, repl) in quirksubs:
            what = re.sub(pattern, repl, what)
        return what

label start_custom:

    # This is used to easily add a formatted '>' to the start of choices in menus.
    $ pick = "{color=#000000}>{/color}"

    $ quick_menu = False

    # Stop main menu music, or any other music playing, and transition to volume select.
    stop music fadeout 1

    show image "gui/main_menu.png"

    window hide

    scene black with Dissolve(0.5)

    $ main_menu = True

    call screen vol_select_custom() with Dissolve(0.5)
    return