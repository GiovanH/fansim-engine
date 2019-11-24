init offset = 0

# Blood helper

init python:
    _hemospectrum = {
        'gray': {
            "hex": "#646464",
            "r": 64,
            "g": 64,
            "b": 64
        },
        'candyred': {
            "hex": "#FF0000",
            "r": 200,
            "g": 0,
            "b": 0
        },
        'test': {
            "hex": "#f00",
            "r": 200,
            "g": 200,
            "b": 200
        },
        'burgandy': {
            "hex": '#a20000',
            "r": 111,
            "g": 33,
            "b": 14
        },
        'bronze': {
            "hex": '#bb6405',
            "r": 162,
            "g": 82,
            "b": 0
        },
        'gold': {
            "hex": '#a1a100',
            "r": 162,
            "g": 162,
            "b": 0
        },
        'lime': {
            "hex": '#84A224',
            "r": 132,
            "g": 162,
            "b": 36
        },
        'olive': {
            "hex": '#416600',
            "r": 66,
            "g": 105,
            "b": 0
        },
        'jade': {
            "hex": '#0aa85b',
            "r": 0,
            "g": 131,
            "b": 66
        },
        'teal': {
            "hex": '#008282',
            "r": 0,
            "g": 132,
            "b": 132
        },
        'cerulean': {
            "hex": '#005682',
            "r": 0,
            "g": 86,
            "b": 130
        },
        'indigo': {
            "hex": '#0021cb',
            "r": 0,
            "g": 0,
            "b": 88
        },
        'purple': {
            "hex": '#2b0057',
            "r": 44,
            "g": 0,
            "b": 89
        },
        'violet': {
            "hex": '#6a006a',
            "r": 106,
            "g": 0,
            "b": 106
        },
        'fuchsia': {
            "hex": '#77003c',
            "r": 119,
            "g": 0,
            "b": 60
        },
    }
    hemoalias = {
        "grey": "gray",  # i HATE
        "rust": "burgandy",
        "blue": "indigo",
        "cobalt": "cerulean"
    }

    def hex_to_rgb(hex):
        # Doesn't currently handle three-digit hex codes right :(
        hex = hex.lstrip('#')
        if len(hex) == 3:
            hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2]
        hlen = len(hex)
        return tuple(int(hex[i:i+hlen/3], 16) for i in range(0, hlen, hlen/3))
    
    def hemospectrum(color):
        try:
            return _hemospectrum[color]
        except KeyError:
            return _hemospectrum[hemoalias[color]]

    def bloodTint(color, fallback):
        try:
            return im.matrix.tint(
                hemospectrum(color)["r"]/200.0, 
                hemospectrum(color)["g"]/200.0, 
                hemospectrum(color)["b"]/200.0
            )
        except KeyError:
            return im.matrix.tint(*map(lambda c: c/200.0, hex_to_rgb(fallback)))

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
    screen="pesterchum_say", who_style="pesterchum_namelabel",
    # Characters will need to set these attributes manually:
    name="chumHandle", what_color='#e00707', image="john"
)


# Trollean
style trollian_namebox is namebox
style trollian_namebox:
    xpos 272
    xanchor 0

style trollian_namelabel is say_label
style trollian_namelabel:
    ypos 16
    xalign 0.0
    size 17

screen trollian_say:
    style_prefix "say"
    default blood = "gray"
    default color = hemospectrum(blood)["hex"]
    default big = False
    window:
        id "window"
        background Composite(
            (1280, 194),
            (0, 0), "{{assets_common}}/trollian_bg_" + ("large" if big else "small") + ".png",
            (0, 0), im.MatrixColor(
                "{{assets_common}}/trollian_" + ("large" if big else "small") + "_rim.png",
                bloodTint(blood, color)
            )
        )
        if big:
            text what id "what" ypos 34 line_spacing 2 color color
        else:
            if who is not None:
                window:
                    id "namebox"
                    style "trollian_namebox"
                    text "trolling: " + who id "who"
            text what id "what" ypos 65 color color

define trollian = Character(
    color='#FFFFFF', who_style="trollian_namelabel", screen="trollian_say",
    # Characters will need to set these attributes manually:
    name="trollTag", image="", show_blood="gray"
)

# Hiveswap
style hiveswap_namebox is namebox
style hiveswap_namebox:
    xpos 248
    xanchor 0
    ypos -58

style hiveswap_namelabel is say_label
style hiveswap_namelabel:
    # yalign 0.5
    xalign 0.0
    size 42
    yalign 1

style hiveswap_dialogue is say_dialogue
style hiveswap_dialogue:
    size 26
    xpos 300
    ypos 26
    xmaximum 720

screen hiveswap_say:
    style_prefix "say"
    default blood = "gray"
    default color = hemospectrum(blood)["hex"]
    window:
        id "window"
        ypos 744
        background im.MatrixColor(
            "{{assets_common}}/hiveswap_textbox_base.png",
            bloodTint(blood, color)
        )

        if who is not None:
            window:
                id "namebox"
                style "hiveswap_namebox"
                text who id "who" color '#FFF' font "Berlin Sans FB Demi Bold.ttf" outlines [(4, color)]
        text what id "what" color '#FFF' font "Berlin Sans FB Regular.ttf"

define hiveswap = Character(
    color='#FFFFFF', screen="hiveswap_say",
    who_style="hiveswap_namelabel", 
    what_style="hiveswap_dialogue",
    # Characters will need to set these attributes manually:
    name="NAME", image="", show_blood="gray"
)

# Openbound

style openbound_namebox is namebox
style openbound_namebox:
    xpos 248
    xanchor 0
    ypos -58

style openbound_namelabel is say_label
style openbound_namelabel:
    # yalign 0.5
    xalign 0.0
    size 42
    outlines [(4, "#FFF")]

style openbound_dialogue is say_dialogue
style openbound_dialogue:
    size 26
    xpos 292
    ypos 30
    xmaximum 720

screen openbound_say:
    style_prefix "say"
    default blood = "gray"
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
                style "openbound_namebox"
                text who id "who" color hemospectrum(blood)["hex"] 

        if chuckle:
            text what id "what" color purple font "{{assets_common}}/BONEAPA.TTF" size 48
        else:
            text what id "what" color hemospectrum(blood)["hex"]

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
    screen="openbound_say", what_style="openbound_dialogue", who_style="openbound_namelabel"
)
define openround = Character(
    screen="openbound_say", what_style="openbound_dialogue", who_style="openbound_namelabel",
    show_obstyle="round"
)
# Examples using these templates instead of the vanilla method:
# define jostart = Character(name="ectoBiologist", kind=pesterchumstart, what_color='#0715cd', image="john")
# define jo = Character(kind=pesterchum,  what_color='#0715cd', image="john")
# define vr = Character(name="arachnidsGrip", kind=trollian, what_color='#005682', image="vriska", window_background="gui/textbox_trollian_cobalt.png")
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