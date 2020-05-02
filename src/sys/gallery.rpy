python:
    """
    Galleries:
        Freshjamz, the music player
        A renpy gallery that attempts to load every image
        A character browser that loads images matching a character prefix

    Access using the devbox by invoking trickster mode at the main menu.

    The music player scans all files for music and adds songs based on their position in the file tree.
    """


init offset = 1

init 900 python:

    gallery = Gallery()
    gallery.transition = Dissolve(0.1)
    gallery.navigation = True

    gallery_images = get_all_images()

    gallery_buttons = []
    for name, image in sorted(gallery_images):
        buttonname = name[0].split("_")[0] # .rstrip('-0123456789')
        if buttonname not in gallery_buttons:
            gallery_buttons.append(buttonname)
            gallery.button(buttonname)
        gallery.image(image)

# Override
screen _gallery:
    frame:
        xfill True
        yfill True
        background Solid("#222")

        key "viewport_leftarrow" action gallery.Previous()
        key "viewport_rightarrow" action gallery.Next()

        if locked:
            add "#000"
            text _("Image [index] of [count] locked.") align (0.5, 0.5)
        else:
            for d in displayables:
                add d

        if gallery.slideshow:
            timer gallery.slideshow_delay action Return("next") repeat True

        key "game_menu" action gallery.Return()

        if gallery.navigation:
            use gallery_navigation

screen gallery_navigation:
    hbox:
        spacing 20

        style_group "gallery"
        # align (.98, .98)

        if quick_menu:
            textbutton _("prev") action gallery.Previous(unlocked=gallery.unlocked_advance)
            textbutton _("next") action gallery.Next(unlocked=gallery.unlocked_advance)
            textbutton _("slideshow") action gallery.ToggleSlideshow()
            textbutton _("return") action gallery.Return()



screen __p__panel_room:
    tag menu
    use game_menu(_("Click the panels!")):
        # A grid of buttons.
        vpgrid:
            mousewheel True
            scrollbars "vertical"
            cols 3
            xsize 940
            ysize 520
            yfill True

            for buttonname in sorted(gallery_buttons):
                add gallery.make_button(buttonname, Text(buttonname, style="button_text"), xalign=0.5, yalign=0.0, xsize=300)



label __p__sayer_bootstrap2:
    $ renpy.block_rollback()
    $ main_menu = False
    scene whitecover with Dissolve(1.0)
    $ quick_menu = True

    call debug_dump_character(store.__p__sayer, store.__p__sayername)

    # call screen __p__sayer_room
    return


screen __p__sayer_room:
    tag menu
    $ store.__p__sayer = "s"
    $ store.__p__sayername = "s"
    use game_menu_volumes(_("Choose a Character")):
        # A grid of buttons.
        vpgrid:
            mousewheel True
            scrollbars "vertical"
            cols 3
            xsize 940
            yfill True

            for sayername, sayer in sorted(get_all_sayers()):
                if sayername and sayer.image_tag:
                    textbutton ((sayer.image_tag + " (" + sayername + ")") if sayername != sayer.image_tag else sayername) action SetVariable("store.__p__sayer", sayer), SetVariable("store.__p__sayername", sayername), Start("__p__sayer_bootstrap2") xsize 300 ysize 60 yalign 0 xalign 0 text_style "button_text"

init 900 python:

    mr = MusicRoom(fadeout=0.0)

    fse_musicroom_tracks = filter(
        lambda f: f.lower()[-4:] in [".mp3", ".wav", ".ogg", "flac"],
        renpy.list_files(common=False))

    for track in fse_musicroom_tracks:
        mr.add(track)

    def formatSongName(filepath):
        # return filepath
        track_meta = fse_music_data.get(filepath)
        if track_meta:
            return "[[{}] {} – {}".format(
                track_meta.get("album") or track_meta.get("package_id"), 
                track_meta.get("artist"), 
                track_meta.get("title"), 
            )
        else:
            print(filepath, "not in track metadata")
            filename = filepath.split("/")[-1]
            filesub = filepath.split("/")[0].replace("custom_assets_", "")
            ext = filename.split(".")[-1]
            filenamep = ".".join(filename.split(".")[:-1])
            return "[[{}] {}".format(filesub, filenamep)

    def formatSongPrefix(filepath):
        # Stub, override
        return ""

transform __p__fruitBounce(bpm=60):
    yanchor 0
    pause (60.0/bpm)
    yanchor 0.2
    pause (60.0/bpm)
    repeat

image __p__green_gear:
    im.FactorScale("{{assets}}/freshjamz/00830-162.png", 0.5, 0.5, bilinear=False)
    pause 0.25
    im.FactorScale("{{assets}}/freshjamz/00830-164.png", 0.5, 0.5, bilinear=False)
    pause 0.25
    im.FactorScale("{{assets}}/freshjamz/00830-166.png", 0.5, 0.5, bilinear=False)
    pause 0.25
    im.FactorScale("{{assets}}/freshjamz/00830-168.png", 0.5, 0.5, bilinear=False)
    pause 0.25
    repeat

style __p__freshjamz_button_text:
    idle_color "#D0004F"
    selected_color "#FF1C87"
    hover_color "#FF1C87"


style __p__freshjamz_scrollbar:
    base_bar Solid("#FF1C87")
    thumb Solid("#D0004F")
style __p__freshjamz_vscrollbar:
    base_bar Solid("#FF1C87")
    thumb Solid("#D0004F")
style __p__freshjamz_slider:
    base_bar Solid("#FF1C87")
    thumb Solid("#D0004F")
style __p__freshjamz_vslider:
    base_bar Solid("#FF1C87")
    thumb Solid("#D0004F")


screen __p__music_room:
    tag menu
    use game_menu(_(""), yinitial=-40):
        frame:
            style_prefix "__p__freshjamz"
            ypos -100
            background Image("{{assets}}/freshjamz/00830-286.png", xpos=-80)
            vbox:
                spacing 10
                image im.FactorScale("{{assets}}/freshjamz/00830-308.png", 2, 2, bilinear=False) xalign 0.5 # yanchor 0.5 
                
                hbox:
                    xalign 0.5
                    # yanchor 0.5
                    spacing 18
                    imagebutton idle im.FactorScale("{{assets}}/freshjamz/00830-316_idle.png", 2, 2, bilinear=False) action (lambda: renpy.music.set_pause(False, channel='music'))
                    imagebutton idle im.FactorScale("{{assets}}/freshjamz/00830-319_idle.png", 2, 2, bilinear=False) action (lambda: renpy.music.set_pause(True, channel='music'))
                    imagebutton idle im.FactorScale("{{assets}}/freshjamz/00830-322_idle.png", 2, 2, bilinear=False) action mr.Previous()
                    imagebutton idle im.FactorScale("{{assets}}/freshjamz/00830-325_idle.png", 2, 2, bilinear=False) action mr.Next()
                    
                    # bar adjustment ui.adjustment(
                #     range=100,
                #     value=1,
                #     adjustable=True
                # )
                frame:
                    xpos 80
                    ypos 30
                    background "{{assets}}/freshjamz/00830-289.png"
                    # background Solid("#0A0")
                    ysize 330
                    xsize 600
                    right_margin 0
                    # vbox:
                    viewport:
                        xpos 30
                        mousewheel True
                        scrollbars "vertical"
                        # The buttons that play each track.
                        vbox:
                            ymaximum 5
                            # right_padding 16
                            for track in fse_musicroom_tracks:
                                hbox:
                                    text formatSongPrefix(track)
                                    textbutton formatSongName(track) action mr.Play(track) # text_style __p__songitem


            # Critical functionality
            add "__p__green_gear" xpos -200 ypos -20

            # Friends
            add im.FactorScale("{{assets}}/freshjamz/00830-295.png", 2, 2, bilinear=False) xpos -200 ypos 500 at __p__fruitBounce(30)
            add im.FactorScale("{{assets}}/freshjamz/00830-298.png", 2, 2, bilinear=False) xpos -260 ypos 540 at __p__fruitBounce(45)
            add im.FactorScale("{{assets}}/freshjamz/00830-301.png", 2, 2, bilinear=False) xpos -220 ypos 560 at __p__fruitBounce(120)
            add im.FactorScale("{{assets}}/freshjamz/00830-304.png", 2, 2, bilinear=False) xpos -280 ypos 560 at __p__fruitBounce(60)
    frame:
        style_prefix "__p__freshjamz"
        align (1.0, 1.0)
        xoffset -20
        padding (26, 24)
        background Frame(
            im.Crop(
                "{{assets_common}}/openbound_hashbox_round.png",
                (0, 0, 793, 34)
            ),
            left=21, top=21, bottom=1)
        vbox:
            xsize 220
            label _("Music Volume") text_color "#D0004F"
            bar value Preference("music volume")
    # Start the music playing on entry to the music room.
    on "replace" action renpy.music.stop
    # mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action (lambda: renpy.music.set_pause(False, channel='music'))

