# Define characters

# Always prefix your definitions with {{p}} so they won't conflict with existing resources.

define {{p}}.jo = Character(name="ectoBiologist", kind=pesterchum, what_color='#0715cd', image="john")
# define {{p}}.jo = Character(kind=pesterchum,  what_color='#0715cd', image="john")
define {{p}}.vr = Character(name="arachnidsGrip", kind=trollian, show_blood="cerulean", image="vriska")
define {{p}}.bo = Character(name="BOLDIR", kind=hiveswap, image="boldir", show_blood="olive")

define {{p}}.tz = Character("[tztitle]", kind=trollian, show_blood='teal', image="{{p}}_terezi")

# Give characters poses
# image vriska neutral3 = Image("images/Vriska_Neutral_3.png", ypos=730, xanchor=640, yanchor=730)
image vriska {{p}}_ngreen = Image("{{assets}}/Vriska_Green.png", ypos=730, xanchor=640, yanchor=730)
image {{p}}_terezi neutral = Image("{{assets}}/terezi.png", ypos=730, xanchor=640, yanchor=730)

# Define backgrounds
# image bg johnroom = im.Scale("images/john_s room.png", 1300,730)

# Define other graphics, end cards
image {{p}}_fakemenu = "{{assets}}/fakemenu.png"
image {{p}}_vriskaend = "images/vriska_endcard_badend1.png"
image {{p}}_fakemenu = "{{assets}}/fakemenu.png"

# ob_meulin is already defined; define a new copy using the openround style
define {{p}}_meu2 = Character(name="MEULIN", show_blood="olive", kind=openround, image="ob_meulin", namebox_xanchor=0.5, who_ypos=3, show_use_nameframe=True)


# Start of route
# Start of route should always be named like this, where sandbox is replaced
# with your volume_id.
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
    scene bg johnroom with Dissolve(0.6)

    # Helper for rewind
    "rollback"

    # Test dialogue systems

    # Compare our dialog systems against the vanilla ones
    # to ensure everything matches up
    bo "Vanilla boldir"
    {{p}}.bo "Custom boldir"
    vr "Vanilla vriska"
    {{p}}.vr "Custom vriska"
    jo "Vanilla john"
    {{p}}.jo "Custom john"
    ob_meulin "Custom openbound"

    # Music notifications. 
    # See full implementation in sys/fx.rpy
    # By default, shows a notification and hides itself.
    show screen MusicToast()
    "Drink it in"

    # ...although you do need to hide it yourself eventually
    # if you want things to work right, even if you use the autohiding versions. 
    hide screen MusicToast

    # Set albumart, title, artist, and album fields to your data.
    # Set tf to toast_down instead of toast_down_peek to make the notification stick on the screen.
    # You can use tags here like other text.

    # Advanced:
    # You can supply an arbitrary transofmration to the tf parameter
    # You can style the entire window using stule=x
    # You can edit the template form strings using ttitle, tartist, and talbum
    # You can edit the size of the album art using albumartsize
    show screen MusicToast(
        tf=toast_down,
        albumart="{{assets}}/scourgequest.jpg",
        title="Let Me Tell You About (Instrumental)",
        artist="Flutterwhat",
        album="{a=https://flutterwhat.bandcamp.com/track/let-me-tell-you-about-insturmental}ScourgeQuest{/a}")
    
    "Drink it in {i}forever{/i}"
    # After *something*, hide the notification, if you used something like toast_down to make it stick.
    # Something that uses toast_down or toast_up will use the toast animation to hide the window.
    hide screen MusicToast

    "and I guess let it leave before bringing in the next thing"

    # pause 0.3

    show screen MusicToast(tf=toast_flyby)
    "Is this even a toast anymore?"
    hide screen MusicToast

    # Trollian multiline test
    show vriska neutral1
    vr "Vanilla vriska"
    {{p}}.vr "Hi! I'm vriska\nLines are loose"
    {{p}}.vr "Hi! I'm vriska, but busy.\nMultiple lines are tight." (show_big=True)
    
    # Trollian colorizing
    {{p}}.vr "Override" (show_color="#0A0", show_blood=None)
    {{p}}.vr "Gray" (show_blood="gray")
    {{p}}.vr "Candy red" (show_blood="candyred")
    {{p}}.vr "Burgandy" (show_blood="burgandy")
    {{p}}.vr "Bronze" (show_blood="bronze")
    {{p}}.vr "Gold" (show_blood="gold")
    {{p}}.vr "Lime" (show_blood="lime")
    {{p}}.vr "Olive" (show_blood="olive")
    {{p}}.vr "Jade" (show_blood="jade")
    {{p}}.vr "Teal" (show_blood="teal")
    {{p}}.vr "Cerulean" (show_blood="cerulean")
    {{p}}.vr "Indigo" (show_blood="indigo")
    {{p}}.vr "Purple" (show_blood="purple")
    {{p}}.vr "Violet" (show_blood="violet")
    {{p}}.vr "Fuchsia" (show_blood="fuchsia")
    hide vriska

    # Hiveswap colorizing
    show boldir neutral
    bo "Vanilla boldir"
    {{p}}.bo "Default"
    {{p}}.bo "Override" (show_color="#0A0")
    {{p}}.bo "Test" (show_blood="test")
    {{p}}.bo "Gray" (show_blood="gray")
    {{p}}.bo "Candy red" (show_blood="candyred")
    bo "Burgandy" (window_background="gui/textbox_rust.png")
    {{p}}.bo "Burgandy" (show_blood="burgandy")
    bo "Bronze" (window_background="gui/textbox_bronze.png")
    {{p}}.bo "Bronze" (show_blood="bronze")
    bo "Gold" (window_background="gui/textbox_gold.png")
    {{p}}.bo "Gold" (show_blood="gold")
    {{p}}.bo "Lime" (show_blood="lime")
    bo "Olive" (window_background="gui/textbox_olive.png")
    {{p}}.bo "Olive" (show_blood="olive")
    bo "Jade" (window_background="gui/textbox_jade.png")
    {{p}}.bo "Jade" (show_blood="jade")
    bo "Teal" (window_background="gui/textbox_teal.png")
    {{p}}.bo "Teal" (show_blood="teal")
    bo "Cobalt" (window_background="gui/textbox_cobalt.png")
    {{p}}.bo "Cerulean" (show_blood="cerulean")
    bo "Blue" (window_background="gui/textbox_blue.png")
    {{p}}.bo "Indigo" (show_blood="indigo")
    bo "Purple" (window_background="gui/textbox_purple.png")
    {{p}}.bo "Purple" (show_blood="purple")
    {{p}}.bo "Violet" (show_blood="violet")
    {{p}}.bo "Fuchsia" (show_blood="fuchsia")
    hide boldir

    # Pesterchum and multilines
    show john neutral
    jo "Vanilla john"
    {{p}}.jo "Hi! I'm john\nLines are loose"
    {{p}}.jo "Hi! I'm john, but busy.\nMultiple lines are tight." (show_big=True)
    hide john

    # Test our supplemental narrators, characters
    flarp "Flarp instructions."
    narrator_prattle "Generic prattle"
    narrator_dirk "Some ultimate dirk narration."
    narrator_calliope "Narrator calliope"

    # Openbound: Use parameters for effects.
    show ob_meulin idle
    ob_meulin idle "Color by color" (show_color="#0A0")
    ob_meulin idle "Color by blood" (show_blood="candyred")
    ob_meulin idle "!!"
    ob_meulin laugh "!!!" (show_hashtags="#hashtag1")
    ob_meulin hypno "A very spooky bit of text which reads about three lines at this size" (show_chuckle=True)
    ob_meulin hypno "spoop" (show_chuckle=True, show_hashtags="#HONK")

    {{p}}_meu2 idle "!!"
    {{p}}_meu2 laugh "!!!" (show_hashtags="#hashtag1")
    {{p}}_meu2 hypno "HONK" (show_chuckle=True)
    {{p}}_meu2 hypno "spoop" (show_chuckle=True, show_hashtags="#HONK")
    hide ob_meulin


    # Different approaches to quirk formatting
    show gamzee neutral

    # Approach 1: Call quirksay
    # Arguments are sayer (character), quirk name, text
    $ quirkSay(gam, "gamzee", "Quirk formatting 1")

    # Approach 2: Define a new sayer
    # Define a new character, given an existing character and a quirk
    # New sayer is reusable!
    $ {{p}}gamq = quirkSayer(gam, "gamzee")
    {{p}}gamq "Quirk formatting 2"
    {{p}}gamq "Quirk formatting 2 forever"

    # Approach 3
    # You can quirk format text without saying it directly
    $ gam(quirkSub("gamzee", "Quirk formatting 3") + " and I guess other stuff")
    hide gamzee

    show vriska neutral1
    {{p}}.vr "I'm 8riska"
    hide vriska

    show {{p}}_terezi neutral
    # play music "music/fs_BOLDIR.wav" loop
    hide blackcover with dissolve

    # Test dynamic name growth
    $ tztitle = "A"
    {{p}}.tz "1"
    $ tztitle = "AAAAAAAAAAAA"
    {{p}}.tz "2"
    $ tztitle = "AAAAAAAAAAAAAAAAAAAAAAAAAAA"
    {{p}}.tz "3"
    $ tztitle = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    {{p}}.tz "4"

    # Twitter demo
    {{p}}.tz neutral "Hey. Hey. Over here."

    "Oh shit. You’re just standing out here with all his mail, he’s going to think you’re trying to rob the place."
    menu:
        "Oh shit. You’re just standing out here with all his mail, he’s going to think you’re trying to rob the place.{fast}"

        "[pick] Play it cool":
            pass
        "[pick] Hide the evidence":
            pass

    show {{p}}_fakemenu
    {{p}}.tz "UHHHHHHHH"

    show {{p}}_terezi at right1280 with ease
    {{p}}.tz "*SNIFFFFFFFF*"

    show {{p}}_terezi at left1280 with move
    {{p}}.tz "TF 1S TH1S TH1NG :?"

    hide {{p}}_terezi
    hide {{p}}_fakemenu

    show vriska neutral4

    # Write dialogue!
    vr neutral3 "Hey. Hey. Over here."
    vr {{p}}_ngreen "8itch."

    hide vriska  # goodbye

    # You can use assets that have already been definied in other pesterquest routes directly!
    show bg gamzeehive
    show gamzee pie1
    gam pie1 "cAn I oFfEr YoU a PiE iN tHeSe TrYiNg TiMeS"
    # Be careful about naming your resources so they don't conflict with other ones. 
    # I help where I can by offering the substitutions like {{package_id}}.

    # Show end card
    call ending pass ("{{p}}_vriskaend", True, True)
    return
