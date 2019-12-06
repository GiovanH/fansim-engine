# this script is copypasted from the first Friendsim so if I left anything weird in here OOPS. MY B
# tip for anyone scoping the files this is what all game dev is like

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init -2 python:
    
    import re

    #Achievements

    # Persistent variable tracking if the user wants to see flashing images or not.

    if persistent.flash is None:

        persistent.flash = True

    if persistent.firstscreen is None:

        persistent.firstscreen = True
        

    # Used for open/close eyes animation

    def eyewarp(x):

        return x**1.33

    def eyewarpaxe(x):

        return 1.0 - (1.0 - x)**0.15

    # Used for sprite overlay colors e.x. zap effect

    def silhouette_matrix (r,g,b,a=1.0):
        return im.matrix((0, 0, 0, 0, r,
                          0, 0, 0, 0, g,
                          0, 0, 0, 0, b,
                          0, 0, 0, a, 0,))
    def silhouette (filename, r,g,b, a = 1.0):
        return im.MatrixColor (Image (filename), silhouette_matrix (r,g,b,a))

define narrator = Character(window_background="gui/textbox_narration.png", what_font='courbd.ttf', what_size=22,  color='#000000', what_color='#000000', what_ypos=26)#, window_ypos= #window_ypos=741)
define op = Character(window_background="gui/textbox_blank.png", what_font='courbd.ttf', what_size=28,  color='#FFFFFF', what_color='#FFFFFF', what_xalign=0.5, what_text_align=0.5)
define fscreen = Character(window_background="gui/textbox_blank.png", what_font='courbd.ttf', what_size=28, color='#FFFFFF', what_color='#FFFFFF', what_xalign=0.5, what_text_align=0.5, what_ypos=-360, what_xsize=1080)

# a bunch of stabby and hurty animation
define stab = Fade(.08, 0.0, .2, color="#FF0000")
define redstab = Fade(0.09, 0.09, 0.15, color="#FF0000")
define pinkflash = Fade(0.05, 0.05, 0.35, color="#ff82d9")
define slowpinkflash = Fade(0.35, 0.35, 0.65, color="#ff82d9")
define bluestab = Fade(0.09, 0.25, 0.25, color="#0000AA")
define olivestab = Fade(0.09, 0.25, 0.25, color="#416600")


define retjump = Fade(.25, 0.25, .25, color="#FFFFFF")
define retjumpslow = Fade(.4, 0.3, .4, color="#FFFFFF")
define retdissolve = Dissolve(.25)

define slowmove = MoveTransition(1.0)

# close/open eyes
define closeeyes = ImageDissolve("eye.png", 0.8, ramplen=128, reverse=True, time_warp=eyewarp)
define openeyes = ImageDissolve("eye.png", 0.8, ramplen=64, time_warp=eyewarp)

image panelscape1 = "images/panelscape1.png"
image panelscape2 = "images/panelscape2.png"
image panelscape3 = "images/panelscape3.png"

image scapewhite = "images/scapewhite.png"

image exception = "images/exception.png"

image bg sky = "images/sky.png"
image bg greensun = "images/greensun.png"

image bg daveroof = "images/dave_roof.png"
image bg jadeatrium = "images/jade_bg_atrium.png"
image bg prospit = "images/jade_bg_prospit.png"

image bg spaceship = "images/background_spaceship.png"
image bg corpsefield = "images/field-2.png"
image bg junkyard = "images/junkyard_final.png"
image bg yourhive = "images/yourhive.png"
image bg undergrowth = "images/bg_undergrowth.png"
image bg outsidenight = "images/bg_outsidenight.png"
image bg outsideday = "images/bg_outsideday.png"
image bg sewer = "images/sewer.png"
image bg forest = "images/forest.png"
image bg cave = "images/Cave.png"
image bg garden = "images/zen_garden.png"
image bg mall = "images/bg_mall3.png"

# misc effects saved from the previous game for reuse

image streetlight = "images/streetlight.png"

image splatter = "images/splatter.png"
image sludge = "images/sludge.png"

image blackcover = "images/blackcover.png"
image whitecover = "images/whitecover.png"
image redcover = "images/redcover.png"

image brownblood = "images/brownblood.png"
image goldblood = "images/goldblood.png"
image oliveblood = "images/oliveblood.png"

image emoji_peace = "images/emoji_peace.png"
image money = "images/cashmoney.png"

image text_clubs = "images/text_clubs.png"
image text_spades = "images/text_spades.png"
image text_hearts = "images/text_hearts.png"
image text_diamonds = "images/text_diamonds.png"

image grypealpha = "gui/grype_alpha.png"

image bg alternia = "images/background1.png"
image bg alternia2 = "images/background4.png"
image bg alternia3 = "images/background2.png"
image bg alternia4 = "images/background3.png"

image fog = "images/fog.png"

image zap = "images/zap.png"

image bg black = "images/blackcover.png"

# fail/win images for this volume
image gameover = "images/gameover.png"

transform title:

    "gui/logo-noglitch.png"
    pause 3.0
    "gui/logo-glitch1.png"
    pause 0.04
    "gui/logo-glitch2.png"
    pause 0.04
    "gui/logo-glitch3.png"
    pause 0.04
    "gui/logo-glitch4.png"
    pause 0.04
    "gui/logo-glitch5.png"
    pause 0.04
    "gui/logo-glitch6.png"
    pause 0.04
    "gui/logo-noglitch.png"
    pause 4.0
    "gui/logo-glitch1.png"
    pause 0.04
    "gui/logo-glitch2.png"
    pause 0.06
    "gui/logo-glitch3.png"
    pause 0.17
    "gui/logo-glitch4.png"
    pause 0.03
    "gui/logo-glitch5.png"
    pause 0.04
    "gui/logo-glitch6.png"
    pause 0.04
    repeat

transform titlesun:

    rotate 30 pos (1175, 85) around (2.0, 2.0)
    easeout 16.0 rotate 0 pos (720, -100) around (2.0, 2.0)

transform titleflare:

    additive 1.0
    alpha 0.0
    pause 8.0
    easeout 8.0 alpha 1.0

transform titleclouds:

    alpha 0.9
    additive 1.0

transform floaties1:

    alpha 0.0 align (-0.2, 1.1) rotate -40

    parallel:

       easeout 4 alpha 0.4
       pause 2
       easein 4 alpha 0.0

    parallel:

        linear 10.0 rotate 35 align (0.8, -0.25) knot (0, 1) knot (0, 1)

    pause 28
    repeat


style outlined:
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    color "FFFF00"
    bold True

style friend:
    outlines [ (absolute(2), "#FF00FF", absolute(1), absolute(1)) ]
    color "FFFF00"
    font "courbd.ttf"
    size 72

style choice_button_text:
    color "0000FF"
    font "courbd.ttf"

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
    
    easeout 0.12 ypos 738
    linear 0.12 ypos 730
    pause 0.2
    easeout 0.12 ypos 738
    linear 0.12 ypos 730
    pause 0.8
    repeat
    
## UNCOMMON TRANSFORMS ##

transform middle:

    ypos 730 xpos 640

transform defaultypos:
    ypos 730

transform defaultxpos:
    xpos 640

#Modified left position for sprites with 1280 width
transform left1280:

    ypos 730 xpos 360

transform closeleft1280:
    
    ypos 730 xpos 540
    
transform farleft1280:

    ypos 730 xpos 180

transform halfleft1280:

    ypos 730 xpos 500

#Modified right position for sprites with 1280 width
transform right1280:

    ypos 730 xpos 960
    
transform closeright1280:
    
    ypos 730 xpos 800

transform farright1280:

    ypos 730 xpos 1080

transform halfright1280:

    ypos 730 xpos 780

#Brings the character in closer
transform moveclose:
    ypos 730 zoom 1.0
    easeout 0.6 ypos 815 zoom 1.2

#Moves them back
transform moveaway:
    ypos 815 zoom 1.2
    easeout 0.45 ypos 730 zoom 1.0

transform quickhug:
    ypos 730 xpos 640 zoom 1.0
    easeout 0.7 ypos 640 xpos 320 zoom 1.5
    pause 1.9
    ypos 640 xpos 320 zoom 1.5
    easeout 0.6 ypos 730 xpos 640 zoom 1.0

transform kicking:
    ypos 730
    easeout 0.09 ypos 716 xalign 0.62
    linear 0.09 ypos 730 xalign 0.5
    pause 0.04
    easeout 0.09 ypos 716 xalign 0.62
    linear 0.09 ypos 730 xalign 0.5

transform cornerbounce:
    ypos 734
    easeout 0.12 ypos 720
    linear 0.12 ypos 734

transform slowbounce:
    ypos 730
    easeout 0.15 ypos 720
    linear 0.15 ypos 730

transform slowbouncing:
    ypos 730
    linear 0.13 ypos 725
    linear 0.13 ypos 730
    repeat

transform slowerbounce:
    ypos 730
    easeout 0.1 ypos 724
    linear 0.1 ypos 730

transform slowerbouncing:
    ypos 730
    easein 0.3 ypos 724
    linear 0.3 ypos 730
    repeat

transform pausebouncing:
    ypos 730
    linear 0.1 ypos 720
    linear 0.1 ypos 730
    pause 0.5
    repeat

transform brush:
    xpos 640
    linear 0.1 xpos 635
    linear 0.1 xpos 640

transform brushright:
    xpos 640
    linear 0.1 xpos 645
    linear 0.1 xpos 640

transform leanin:
    ypos 730
    easein 0.2 zoom 1.05 ypos 750

transform leanout:
    ypos 750
    easein 0.2 zoom 1.0 ypos 730

#Sets zoom/position back to default
transform defaultzoom:
    easeout 0.1 zoom 1 ypos 730

transform typing:
    ypos 730
    linear 0.18 ypos 733
    linear 0.17 ypos 730
    pause(0.1)
    linear 0.12  ypos 732
    linear 0.12 ypos 730
    linear 0.14  ypos 732
    linear 0.13 ypos 730
    ypos 730
    repeat

transform search:
    ypos 730
    easeout 0.16 ypos 742
    linear 0.16 ypos 730
    pause 0.3
    easeout 0.12 ypos 742
    linear 0.12 ypos 730
    pause 0.06
    easeout 0.12 ypos 742
    linear 0.12 ypos 730
    pause 0.8
    easeout 0.1 ypos 742
    linear 0.1 ypos 730
    pause 0.4
    easeout 0.12 ypos 742
    linear 0.12 ypos 730
    pause 0.2
    repeat

transform searcharound:
    xpos 640
    easeout 0.32 xpos 580
    easeout 0.3 xpos 700
    easeout 0.28 xpos 620
    easeout 0.26 xpos 690
    easeout 0.2 xpos 640
    xpos 640

transform gesture:
    ypos 730 xpos 640
    easeout 0.15 xpos 620
    easeout 0.15 xpos 660
    easeout 0.1 xpos 640
    xpos 640

transform holdingup:
    easein 0.60 zoom 1.6 ypos 700
    easeout 0.45 zoom 2.2 ypos 1250

transform setdown:
    easein 0.45 zoom 1.6 ypos 825
    easeout 0.60 zoom 1.0 ypos 730

transform dungeon:
    ypos 734
    linear 0.5 xalign -0.12 zoom 0.75

transform bloodoverlay:
    zoom 1.25 rotate 65 yalign 0.42 xalign 0.48

transform sweepleft:
    linear 0.66 xalign -1.50

transform sweepright:
    linear 0.66 xalign 2.00

transform hugincoming:

    easeout 0.66 zoom 1.15
    pause 0.25
    easeout 0.66 zoom 1.0

transform hug:

    ypos 730
    easeout 1 zoom 1.75 ypos 1000

transform endhug:

    easein 0.33 zoom 1.0 ypos 730

transform closeup:
    easein 1.5 zoom 1.75 ypos 1025

transform dogzoom1:
    easein 0.5 zoom 1.9 ypos 1075

transform dogzoom2:
    easein 0.5 zoom 2.05 ypos 1125

transform dogzoom3:
    easein 0.5 zoom 2.20 ypos 1175

transform dogzoom4:
    easein 0.5 zoom 2.35 ypos 1225

transform dogzoom5:
    easein 0.5 zoom 2.5 ypos 1275

transform dogzoom6:
    easein 0.5 zoom 2.65 ypos 1325

transform dogunzoom:
    easeout 0.1 zoom 1.0 ypos 730

transform dogchoke:

    yalign 1.0 ypos 730
    easeout 0.15 ypos 760
    pause 0.2
    linear 0.03 ypos 756
    linear 0.03 ypos 760
    linear 0.03 ypos 756
    linear 0.03 ypos 760
    linear 0.03 ypos 756
    easein 0.35 ypos 770
    pause 0.15
    linear 0.08 ypos 740
    easein 0.1 ypos 730
    pause 0.3
    repeat

transform diemendies:

    linear 0.04 ypos 730
    easeout 0.8 ypos 500
    pause 0.1
    linear 0.08 rotate 180
    easein 0.35 ypos 1640

transform dogagony:
    xalign 0.5 ypos 730
    easein 0.25 xalign 0.45 ypos 740
    easeout 0.25 xalign 0.55 ypos 750
    easeout 0.25 xalign 0.45 ypos 760
    easeout 0.25 xalign 0.55 ypos 770
    easeout 0.25 xalign 0.45 ypos 780
    easeout 0.25 xalign 0.55 ypos 790
    easeout 0.25 xalign 0.45 ypos 800
    easein 0.25 xalign 0.5 ypos 810

transform rumbling:

    ypos 730
    linear 0.1 ypos 728
    linear 0.1 ypos 732
    repeat

transform sludgeanim:

    ypos 730
    easein 0.4 ypos 775
    pause 0.2
    easein 0.4 ypos 730
    pause 0.2
    repeat

transform drownanim:

    ypos 730
    easein 0.45 ypos 775
    pause 0.25
    easein 0.35 ypos 730
    pause 0.25
    repeat

transform sludgebegone:

    linear 1.8 ypos 1440

transform goatpet:
    ypos 730 xpos 360
    easeout 0.2 xpos 340 ypos 734
    easeout 0.2 xpos 360 ypos 730

transform lookaround:

    xalign 0.5
    linear 0.6 xalign 0.0
    pause 1.2
    linear 0.3 xalign 0.5
    pause 1.2
    linear 0.3 xalign 1.0
    pause 1.2
    linear 0.6 xalign 0.5

transform entranceleft:
    yalign 1.0
    xpos -1000
    linear 1.2 xpos 0

transform entranceright:
    yalign 1.0
    xpos 1000
    linear 1.2 xpos 0

transform menumove:

    xpos 20

    on hover:
        linear .25 xpos 50

    on idle:
        linear .25 xpos 20

transform wiggle:

    rotate 0
    ypos -400

    on hover:
        linear .1 rotate -2
        linear .1 rotate 0
        linear .1 rotate 2
        linear .1 rotate 0

transform offscreenleft:
    ypos 730 xpos -500

transform offscreenright:
    ypos 730 xpos 1600

transform offscreenleftflipped:
    xzoom -1.0 ypos 730 xpos -500

transform offscreenrightflipped:
    xzoom -1.0 ypos 730 xpos 1500

# Volume 1 Transforms
transform readerseated:
    ypos 790 xpos 780

transform readerstand:
    ypos 790 xpos 780
    linear 0.02 ypos 730 xpos 780

transform fenestrate:
    ypos 730 xpos 640
    linear 0.25 ypos 730 xpos -500

transform johnreveal:
    ypos 730
    linear 0.08 ypos 740
    "john happy"
    ypos 730

transform lemonface:
    ypos 730
    linear 0.4 ypos 728
    "john displeased"
    linear 0.16 ypos 735

transform shortsigh:
    ypos 730
    easein 0.3 ypos 735
    easeout 0.4 ypos 730

transform delayedno:
    ypos 730
    pause(1.0)
    "john notcrazy"
    easeout 0.12 ypos 716
    linear 0.12 ypos 730

transform delayedshocked:
    ypos 730
    "john neutral"
    pause(1.0)
    "john shocked"
    easeout 0.12 ypos 716
    linear 0.12 ypos 730

transform delayedum:
    ypos 730
    "john shocked"
    pause(1.0)
    "john blankstare"

transform shrug:
    ypos 730
    easeout 0.12 ypos 724
    linear 0.12 ypos 730

transform betweentwojohns:
    ypos 730 xpos 870

transform fenceoffbottomleft:
    ypos 1500 xpos 450

transform fenceoffbottomright:
    ypos 1500 xpos 800

transform fencecrouchleft:
    ypos 1500 xpos 450
    ease 0.7 ypos 950 xpos 450

transform fencecrouchright:
    ypos 1500 xpos 800
    ease 0.8 ypos 850 xpos 800

transform fencebackpat:
    ypos 850 xpos 800
    linear 0.2 xpos 790
    linear 0.2 xpos 800
    linear 0.18 xpos 790
    linear 0.18 xpos 800

transform fenceheadshake:
    ypos 850 xpos 800
    easeout 0.09 xpos 805
    ease 0.14 xpos 797
    easeout 0.08 xpos 800

transform fencebow:
    ypos 850 xpos 800
    ease 0.3 ypos 866
    pause 0.6
    ease 0.3 ypos 850

transform fencezap:
    ease 0.3 xpos 680 ypos 850

transform johnzap1:
    xpos 700 ypos 420 zoom 0.5

transform johnzap2:
    xpos 700 ypos 450 zoom 0.5

transform johnzap3:
    xpos 675 ypos 550 zoom 0.5
# transform right1280zap:
#     ypos 730 xpos 960 alpha 0.0

# transform right1280unzap:
#     ypos 730 xpos 960 alpha 1.0

transform houseshaking:
    xpos 636 ypos 724
    pause 0.08
    xpos 641 ypos 718
    pause 0.08
    xpos 644 ypos 721
    pause 0.08
    xpos 639 ypos 730
    pause 0.08
    xpos 643 ypos 719
    pause 0.08
    xpos 635 ypos 723
    pause 0.08
    xpos 640 ypos 714
    pause 0.08
    xpos 637 ypos 720
    pause 0.08
    xpos 647 ypos 717
    pause 0.08
    repeat

transform houseshakingslow:
    xpos 636 ypos 724
    pause 0.2
    xpos 641 ypos 718
    pause 0.2
    xpos 644 ypos 721
    pause 0.2
    xpos 639 ypos 730
    pause 0.2
    xpos 643 ypos 719
    pause 0.2
    xpos 635 ypos 723
    pause 0.2
    xpos 640 ypos 714
    pause 0.2
    xpos 637 ypos 720
    pause 0.2
    xpos 647 ypos 717
    pause 0.2
    repeat

transform scapeshift1:
    alpha 0.0

    block:

        easein 4 alpha 0.4
        easeout 4 alpha 0.0
        pause 4
        repeat

transform scapeshift2:
    alpha 0.0
    pause 4

    block:

        easein 4 alpha 0.4
        easeout 4 alpha 0.0
        pause 4
        repeat

transform scapeshift3:
    alpha 0.0
    pause 8

    block:

        easein 4 alpha 0.4
        easeout 4 alpha 0.0
        pause 4
        repeat

transform scapewhiteshift:

    alpha 0.0
    easein 3 alpha 1
    block:

        easein 1.5 alpha 0.6
        easein 1.5 alpha 1
        repeat

transform canonflash:

    "bg sky"
    pause 0.075
    "bg rosebedroom"
    pause 0.075
    "bg johnfyard"
    pause 0.075
    "bg johnroom"
    pause 0.075
    "bg corpsefield"
    pause 0.075
    "bg jadeatrium"
    pause 0.075
    "bg yourhive"
    pause 0.075
    "bg prospit"
    pause 0.075
    "bg daveroof"
    pause 0.075
    "bg roseraining"
    pause 0.075
    "bg junkyard"
    pause 0.075
    "bg johnbyard"
    pause 0.075
    "bg spaceship"
    pause 0.075
    "bg greensun"

python:

    import os
    import os.path

# Game start

label help:

    call screen help

    return

label splashscreen:

    if persistent.firstscreen:

        scene black

        fscreen "Pesterquest contains spoilers for Homestuck, The Homestuck Epilogues, and Hiveswap: Friendsim. You do not need to have read The Homestuck Epilogues or Hiveswap: Friendsim to enjoy the game, but you may miss occasional references.\n\n\nPesterquest contains flashing lights and similar imagery. You may disable these animations in the options menu.\n\n\nPesterquest contains mature content and sensitive themes. For detailed content warnings, consult the {a=call:content_warnings}\"Warnings\"{/a} menu."

        $ persistent.firstscreen = False

    return

label start:

    $ achievement.sync()

    # This is used to easily add a formatted '>' to the start of choices in menus.
    $ pick = "{color=#000000}>{/color}"

    $ quick_menu = False

    jump start2

label start2:

    # Stop main menu music, or any other music playing, and transition to volume select.
    stop music fadeout 1.5

    show image "gui/main_menu.png"

    window hide

    scene black with Dissolve(1.5)

    $ main_menu = True

    call screen vol_select() with Dissolve(1.0)

    return


label ending(card="blackcover", win=True, fadetoblack=True):

    if fadetoblack:

        scene black with Dissolve (0.5)

    $ renpy.pause(0.5)

    $ quick_menu = False

    if win:

        play music "music/victory_jingle.mp3" fadeout 1.0 noloop

    else:

        play music "music/game_over.mp3" fadeout 1.0 noloop

    scene expression card with Dissolve(1.0)

    $ renpy.pause()

    stop music fadeout 1.0

    scene black with Dissolve(1.0)

    return
