style trollean_namebox:
    properties gui.text_properties("name", accent=True)
    yalign 0.5
    xalign 0.0
    xpos -365
    ypos 16
    size 17

style hiveswap_namebox:
    properties gui.text_properties("name", accent=True)
    yalign 0.5
    xalign 0.0
    xpos -380
    ypos -34
    size 42

style pesterchum_namebox:
    properties gui.text_properties("name", accent=True)
    yalign 0.5
    xalign 0.5
    xpos 0

style hiveswap_textbox:
    size 26
    xpos 300
    ypos 26
    xmaximum 720

define trollean = Character(
    color='#FFFFFF', who_style="trollean_namebox", who_prefix="trolling: ",
    # Characters will need to set these attributes manually:
    name="trollTag", image="", window_background="gui/textbox_trollian_teal.png"
)

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

define hiveswap = Character(
    color='#FFFFFF', what_color='#FFFFFF', 
    who_style="hiveswap_namebox", who_font="Berlin Sans FB Demi Bold.ttf",
    what_style="hiveswap_textbox", what_font="Berlin Sans FB Regular.ttf", 
    window_ypos=744, 
    # Characters will need to set these attributes manually:
    name="NAME", image="", window_background="gui/textbox_olive.png", who_outlines=[(4, "#416600")]
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
        "john": ("([A-Z])", lambda m: m.group(1).lower()),
        "gamzee": ("([a-zA-Z])([a-zA-Z]?)", lambda m: m.group(1).lower() + m.group(2).upper())
    }

    def quirkSay(who, quirk, what, *args, **kwargs):
        pattern, repl = quirks.get(quirk.lower())
        return who(re.sub(pattern, repl, what), *args, **kwargs)


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

    
    # text_align 1.0
