# Define characters

# Always prefix your definitions with __p__ so they won't conflict with existing resources.

define __p__.jo = Character(name="ectoBiologist", kind=pesterchum, what_color='#0715cd', image="john")
# define __p__.jo = Character(kind=pesterchum,  what_color='#0715cd', image="john")
define __p__.vr = Character(name="arachnidsGrip", kind=trollian, show_blood="cerulean", image="vriska")
define __p__.bo = Character(name="BOLDIR", kind=hiveswap, image="boldir", show_blood="olive")

define __p__.tz = Character("[tztitle]", kind=trollian, show_blood='teal', image="__p___terezi")

# Give characters poses
# image vriska neutral3 = Image("images/Vriska_Neutral_3.png", ypos=730, xanchor=640, yanchor=730)
image vriska __p___ngreen = Image("{{assets}}/Vriska_Green.png", ypos=730, xanchor=640, yanchor=730)
image __p___terezi neutral = Image("{{assets}}/terezi.png", ypos=730, xanchor=640, yanchor=730)

# Define backgrounds
# image bg johnroom = im.Scale("images/john_s room.png", 1300,730)

# Define other graphics, end cards
image __p___fakemenu = "{{assets}}/fakemenu.png"
image __p___vriskaend = "images/vriska_endcard_badend1.png"
image __p___fakemenu = "{{assets}}/fakemenu.png"

# ob_meulin is already defined; define a new copy using the openround style
define __p___meu2 = Character(name="MEULIN", show_blood="olive", kind=openround, image="ob_meulin", namebox_xanchor=0.5, who_ypos=3, show_use_nameframe=True)


# Start of route
# Start of route should always be named like this, where sandbox is replaced
# with your volume_id.
label __package_entrypoint___sandbox:

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
    __p__.bo "Custom boldir"
    vr "Vanilla vriska"
    __p__.vr "Custom vriska"
    jo "Vanilla john"
    __p__.jo "Custom john"
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
    __p__.vr "Hi! I'm vriska\nLines are loose"
    __p__.vr "Hi! I'm vriska, but busy.\nMultiple lines are tight." (show_big=True)
    
    # Trollian colorizing
    __p__.vr "Override" (show_color="#0A0", show_blood=None)
    __p__.vr "Gray" (show_blood="gray")
    __p__.vr "Candy red" (show_blood="candyred")
    __p__.vr "Burgandy" (show_blood="burgandy")
    __p__.vr "Bronze" (show_blood="bronze")
    __p__.vr "Gold" (show_blood="gold")
    __p__.vr "Lime" (show_blood="lime")
    __p__.vr "Olive" (show_blood="olive")
    __p__.vr "Jade" (show_blood="jade")
    __p__.vr "Teal" (show_blood="teal")
    __p__.vr "Cerulean" (show_blood="cerulean")
    __p__.vr "Indigo" (show_blood="indigo")
    __p__.vr "Purple" (show_blood="purple")
    __p__.vr "Violet" (show_blood="violet")
    __p__.vr "Fuchsia" (show_blood="fuchsia")
    hide vriska

    # Hiveswap colorizing
    show boldir neutral
    bo "Vanilla boldir"
    __p__.bo "Default"
    __p__.bo "Override" (show_color="#0A0")
    __p__.bo "Test" (show_blood="test")
    __p__.bo "Gray" (show_blood="gray")
    __p__.bo "Candy red" (show_blood="candyred")
    bo "Burgandy" (window_background="gui/textbox_rust.png")
    __p__.bo "Burgandy" (show_blood="burgandy")
    bo "Bronze" (window_background="gui/textbox_bronze.png")
    __p__.bo "Bronze" (show_blood="bronze")
    bo "Gold" (window_background="gui/textbox_gold.png")
    __p__.bo "Gold" (show_blood="gold")
    __p__.bo "Lime" (show_blood="lime")
    bo "Olive" (window_background="gui/textbox_olive.png")
    __p__.bo "Olive" (show_blood="olive")
    bo "Jade" (window_background="gui/textbox_jade.png")
    __p__.bo "Jade" (show_blood="jade")
    bo "Teal" (window_background="gui/textbox_teal.png")
    __p__.bo "Teal" (show_blood="teal")
    bo "Cobalt" (window_background="gui/textbox_cobalt.png")
    __p__.bo "Cerulean" (show_blood="cerulean")
    bo "Blue" (window_background="gui/textbox_blue.png")
    __p__.bo "Indigo" (show_blood="indigo")
    bo "Purple" (window_background="gui/textbox_purple.png")
    __p__.bo "Purple" (show_blood="purple")
    __p__.bo "Violet" (show_blood="violet")
    __p__.bo "Fuchsia" (show_blood="fuchsia")
    hide boldir

    # Pesterchum and multilines
    show john neutral
    jo "Vanilla john"
    __p__.jo "Hi! I'm john\nLines are loose"
    __p__.jo "Hi! I'm john, but busy.\nMultiple lines are tight." (show_big=True)
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

    __p___meu2 idle "!!"
    __p___meu2 laugh "!!!" (show_hashtags="#hashtag1")
    __p___meu2 hypno "HONK" (show_chuckle=True)
    __p___meu2 hypno "spoop" (show_chuckle=True, show_hashtags="#HONK")
    hide ob_meulin


    # Different approaches to quirk formatting
    show gamzee neutral

    # Approach 1: Call quirksay
    # Arguments are sayer (character), quirk name, text
    $ quirkSay(gam, "gamzee", "Quirk formatting 1")

    # Approach 2: Define a new sayer
    # Define a new character, given an existing character and a quirk
    # New sayer is reusable!
    $ __p__gamq = quirkSayer(gam, "gamzee")
    __p__gamq "Quirk formatting 2"
    __p__gamq "Quirk formatting 2 forever"

    # Approach 3
    # You can quirk format text without saying it directly
    $ gam(quirkSub("gamzee", "Quirk formatting 3") + " and I guess other stuff")
    hide gamzee

    show vriska neutral1
    __p__.vr "I'm 8riska"
    hide vriska

    show __p___terezi neutral
    # play music "music/fs_BOLDIR.wav" loop
    hide blackcover with dissolve

    # Test dynamic name growth
    $ tztitle = "A"
    __p__.tz "1"
    $ tztitle = "AAAAAAAAAAAA"
    __p__.tz "2"
    $ tztitle = "AAAAAAAAAAAAAAAAAAAAAAAAAAA"
    __p__.tz "3"
    $ tztitle = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    __p__.tz "4"

    # Twitter demo
    __p__.tz neutral "Hey. Hey. Over here."

    "Oh shit. You’re just standing out here with all his mail, he’s going to think you’re trying to rob the place."
    menu:
        "Oh shit. You’re just standing out here with all his mail, he’s going to think you’re trying to rob the place.{fast}"

        "[pick] Play it cool":
            pass
        "[pick] Hide the evidence":
            pass

    show __p___fakemenu
    __p__.tz "UHHHHHHHH"

    show __p___terezi at right1280 with ease
    __p__.tz "*SNIFFFFFFFF*"

    show __p___terezi at left1280 with move
    __p__.tz "TF 1S TH1S TH1NG :?"

    hide __p___terezi
    hide __p___fakemenu

    show vriska neutral4

    # Write dialogue!
    vr neutral3 "Hey. Hey. Over here."
    vr __p___ngreen "8itch."

    hide vriska  # goodbye

    # You can use assets that have already been definied in other pesterquest routes directly!
    show bg gamzeehive
    show gamzee pie1
    gam pie1 "cAn I oFfEr YoU a PiE iN tHeSe TrYiNg TiMeS"
    # Be careful about naming your resources so they don't conflict with other ones. 
    # I help where I can by offering the substitutions like {{package_id}}.

    # Show end card
    call ending pass ("__p___vriskaend", True, True)
    return
