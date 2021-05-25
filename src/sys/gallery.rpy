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
    # Initialize image gallery
    # TODO: This misses some graphics, like buttons defined inline, and other screen elements like inline factorscales

    try:
        import json
        with renpy.file("fse_packagelist.json") as fp:
            fse_packagelist = json.load(fp)
    except IOError:
        print("ERROR: GALLERY: Can't find fse packagelist")
        fse_packagelist = []

    debug_image_sort = False
    dprint = print if debug_image_sort else (lambda *args: 0)

    __p__galleries = {}
    # __p__images_in_gal = []

    all_sayer_tags = [sayer.image_tag for sayername, sayer in get_all_sayers() if sayername and sayer.image_tag]

    for name, image in sorted(get_all_images()):
        # if image in __p__images_in_gal:
        #     continue

        dprint(name, image)

        supercat = None
        subcat = None

        if supercat is None:
            for package_id in fse_packagelist:
                if name[0].startswith(package_id):
                    # If this image is a member of a package
                    for sayer_prefix in all_sayer_tags:
                        if name[0].startswith(sayer_prefix):
                            # If this image is also a member of a character
                            sayer_name = sayer_prefix.replace(package_id + "_", "")
                            supercat = sayer_name + " (" + package_id.replace("_" + sayer_name, "") + ")"
                            subcat = " ".join(name).replace(package_id + "_", "")
                            break
                    if supercat is None:
                        # If this image is not also a member of a character
                        supercat = package_id

        if supercat is None:
            # If this image is not a member of a package
            supercat = name[0].split("_")[0]

        if subcat is None:
            subcat = " ".join(name).replace(supercat + "_", "")

        dprint(supercat, subcat, name)

        if (supercat == subcat and not __p__galleries.get(supercat)) or not subcat.strip():
            subcat = supercat
            supercat = "unsorted"

        supercat_gal = __p__galleries.get(supercat)
        if not supercat_gal:
            supercat_gal = Gallery()
            supercat_gal.transition = Dissolve(0.1)
            __p__galleries[supercat] = supercat_gal
        # else:
        #     supercat_gal.navigation = True

        supercat_gal.button(subcat)
        supercat_gal.image(image)
        # __p__images_in_gal.append(image)

style __p__lazy_viewport is viewport:
    xfill False
    yfill False


screen __p__panel_room:
    tag menu
    default active_category = None
    use game_menu(_("Click the panels!")):
        # A grid of buttons.
        vbox:
            label "Package/Character/Category"
            viewport:
                # Better grid, horizontal
                style "__p__lazy_viewport"
                mousewheel True
                scrollbars "horizontal"
                xfill True
                hbox:
                    spacing 10
                    $ from math import ceil
                    # $ print("ceil", len(__p__gal_cat_buttons), int(ceil(len(__p__gal_cat_buttons) / 3.0)))
                    for l in splitIntoLists(sorted(__p__galleries.keys()), int(ceil(len(__p__galleries) / 3.0))):
                        vbox:
                            for cat_btn_name in l:
                                textbutton "[cat_btn_name]" action SetScreenVariable("active_category", cat_btn_name)


            if active_category:
                label _("Displayables")
                frame:
                    padding (8, 8, 8, 8)
                    xfill True
                    yfill True
                    ysize 380
                    viewport:
                        # Better grid, vertical
                        mousewheel True
                        scrollbars "vertical"
                        xfill True
                        yfill True
                        hbox:
                            spacing 4
                            box_wrap True
                            for kv in __p__galleries[active_category].buttons.items():
                                add __p__galleries[active_category].make_button(
                                    kv[0],
                                    Text(kv[0], style="button_text"),
                                    align=(0.0, 0.0), xsize=300
                                )


# Override
screen _gallery:
    frame:
        xfill True
        yfill True
        padding (0, 0, 0, 0)
        background Solid("#222")

        key "viewport_leftarrow" action gallery.Previous()
        key "viewport_rightarrow" action gallery.Next()

        if locked:
            add "#000"
            text _("Image [index] of [count] locked.") align (0.5, 0.5)
        else:
            viewport:
                draggable True
                for d in displayables:
                    add d align (0.5, 0.5)

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

image !greenscreen = Solid("#0A0")

label __p__sayer_bootstrap2:
    $ renpy.block_rollback()
    $ main_menu = False
    scene __p__greenscreen with Dissolve(1.0)
    $ quick_menu = True

    $ print("Sayer is", store.__p__sayername, "(", store.__p__sayer, ")")
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
                    $ label = (((sayer.name or sayername) + " (" + sayername.replace(sayer.image_tag, '') + ")") if sayername != sayer.image_tag else (sayer.name or sayername))
                    textbutton label action SetVariable("store.__p__sayer", sayer), SetVariable("store.__p__sayername", sayername), Start("__p__sayer_bootstrap2") xsize 300 ysize 60 yalign 0 xalign 0 text_style "button_text"

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
    # size 20
    # yalign 0.0


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

style __p__freshjamz_prefix:
    ypos 6 # i don't know why, no. button padding + ???


screen __p__music_room:
    tag menu
    # use game_menu(_(""), yinitial=-40):
    style_prefix "__p__freshjamz"

    add "gui/main_menu.png"

    frame:
        xpos 200
        background Image("{{assets}}/freshjamz/00830-286.png", xpos=-80)
        vbox:
            spacing 10
            image "{{assets}}/freshjamz/00830-308.png" xalign 0.5 xoffset -30 # yanchor 0.5 
            
            hbox:
                xalign 0.5
                # yanchor 0.5
                spacing 18
                imagebutton auto "{{assets}}/freshjamz/play_%s.png" action (lambda: renpy.music.set_pause(False, channel='music')) 
                imagebutton auto "{{assets}}/freshjamz/pause_%s.png" action (lambda: renpy.music.set_pause(True, channel='music'))
                imagebutton auto "{{assets}}/freshjamz/prev_%s.png" action mr.Previous()
                imagebutton auto "{{assets}}/freshjamz/next_%s.png" action mr.Next()
                imagebutton auto "{{assets}}/freshjamz/single_%s.png" action mr.ToggleSingleTrack() selected mr.single_track
                imagebutton auto "{{assets}}/freshjamz/shuffle_%s.png" action mr.ToggleShuffle() selected mr.shuffle
                
                # bar adjustment ui.adjustment(
            #     range=100,
            #     value=1,
            #     adjustable=True
            # )
            frame:
                xpos 80
                ypos 20
                background Frame("{{assets}}/freshjamz/00830-289.png", 100, 100)
                # background Solid("#0A0")
                ysize 330
                xsize 700
                right_padding 100
                top_padding 10
                # vbox:
                viewport id "vp":
                    xpos 60
                    mousewheel True
                    # The buttons that play each track.
                    vbox:
                        ymaximum 5
                        # right_padding 16
                        for track in fse_musicroom_tracks:
                            hbox:
                                text formatSongPrefix(track) style "__p__freshjamz_prefix"
                                textbutton formatSongName(track) action mr.Play(track) # text_style __p__songitem

                vbar value YScrollValue("vp") xpos 30

    # Critical functionality
    add "__p__green_gear" xpos -0 ypos -0

    # Friends
    fixed:
        xpos 1200
        ypos 500
        add im.FactorScale("{{assets}}/freshjamz/00830-295.png", 2, 2, bilinear=False) xpos -0 ypos 0 at __p__fruitBounce(30)
        add im.FactorScale("{{assets}}/freshjamz/00830-298.png", 2, 2, bilinear=False) xpos -60 ypos 40 at __p__fruitBounce(45)
        add im.FactorScale("{{assets}}/freshjamz/00830-301.png", 2, 2, bilinear=False) xpos -20 ypos 60 at __p__fruitBounce(120)
        add im.FactorScale("{{assets}}/freshjamz/00830-304.png", 2, 2, bilinear=False) xpos -80 ypos 60 at __p__fruitBounce(60)

    frame:
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

    key "game_menu" action Return()

