# Define characters

define {{p}}_jostart = Character(name="ectoBiologist", kind=pesterchumstart, what_color='#0715cd', image="john")
define {{p}}_jo = Character(kind=pesterchum,  what_color='#0715cd', image="john")
define {{p}}_vr = Character(name="arachnidsGrip", kind=trollean, what_color='#005682', image="vriska", window_background="gui/textbox_trollian_cobalt.png")
define {{p}}_bo = Character(name="BOLDIR", kind=hiveswap, image="boldir", window_background="gui/textbox_olive.png", who_outlines=[(4, "#416600")])


define {{p}}_tz = Character("[tztitle]", kind=trollean, what_color='#008282', image="{{p}}_terezi", window_background="gui/textbox_trollian_teal.png",)

# Give characters poses
image {{p}}_terezi neutral = Image("{{assets}}/terezi.png", ypos=730, xanchor=640, yanchor=730)

# Other images
image {{p}}_fakemenu = "{{assets}}/fakemenu.png"

# Give characters poses
# image vriska neutral3 = Image("images/Vriska_Neutral_3.png", ypos=730, xanchor=640, yanchor=730)
image vriska ngreen = Image("{{assets}}/Vriska_Green.png", ypos=730, xanchor=640, yanchor=730)

# Define backgrounds
# image bg johnroom = im.Scale("images/john_s room.png", 1300,730)

# Define other graphics, end cards
image {{p}}_fakemenu = "{{assets}}/fakemenu.png"
image {{p}}_vriskaend = "images/vriska_endcard_badend1.png"

# Start of route
label {{package_entrypoint}}_sandbox:

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

    flarp "Flarp instructions."
    narrator_prattle "Generic prattle"
    narrator_dirk "Some ultimate dirk narration."
    narrator_calliope "Narrator calliope"

    show john neutral
    {{p}}_jostart "hi! i'm john"
    $ quirkSay({{p}}_jo, "john", "Quirk formatting")
    $ quirkSay({{p}}_jo, "gamZee", "Gamzee Quirk formatting")
    {{p}}_jo "i'm still john"
    hide john

    show vriska neutral1
    {{p}}_vr "I'm 8riska"
    hide vriska


    show boldir neutral
    {{p}}_bo "I'm secrets"
    hide boldir

    show {{p}}_terezi neutral
    # play music "music/fs_BOLDIR.wav" loop
    hide blackcover with dissolve

    $ tztitle = "A"
    {{p}}_tz "1"
    $ tztitle = "AAAAAAAAAAAA"
    {{p}}_tz "2"
    $ tztitle = "AAAAAAAAAAAAAAAAAAAAAAAAAAA"
    {{p}}_tz "3"
    $ tztitle = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    {{p}}_tz "4"
    # Write dialogue!
    {{p}}_tz neutral "Hey. Hey. Over here."

    "Oh shit. You’re just standing out here with all his mail, he’s going to think you’re trying to rob the place."
    menu:
        "Oh shit. You’re just standing out here with all his mail, he’s going to think you’re trying to rob the place.{fast}"

        "[pick] Play it cool":
            pass
        "[pick] Hide the evidence":
            pass

    show {{p}}_fakemenu
    {{p}}_tz "UHHHHHHHH"

    show {{p}}_terezi at right1280 with ease
    {{p}}_tz "*SNIFFFFFFFF*"

    show {{p}}_terezi at left1280 with move
    {{p}}_tz "TF 1S TH1S TH1NG :?"

    hide {{p}}_terezi
    hide {{p}}_fakemenu

    show vriska neutral4

    # Write dialogue!
    vr neutral3 "Hey. Hey. Over here."
    vr ngreen "8itch."

    hide vriska  # goodbye

    # You can also use assets that have already been definied in other pesterquest routes directly!
    show bg gamzeehive
    show gamzee pie1
    gam pie1 "cAn I oFfEr YoU a PiE iN tHeSe TrYiNg TiMeS"
    # Be careful about naming your resources so they don't conflict with other ones. 
    # I help where I can by offering the substitutions like {{package_id}}.

    # Show end card
    call ending pass ("{{p}}_vriskaend", True, True)
    return
