init offset = 0

init python:

    gallery = Gallery()
    gallery.transition = Dissolve(0.1)
    gallery.navigation = True

    gallery_images = filter(
        lambda f: f.lower()[-4:] in [".png"],
        renpy.list_files(common=False))

    gallery_buttons = []
    for imagepath in sorted(gallery_images):
        filesub = imagepath.split("/")[0].replace("custom_assets_", "")
        if filesub not in gallery_buttons:
            gallery_buttons.append(filesub)
            gallery.button(filesub)
        gallery.image(imagepath)

# Override
screen _gallery:

    frame:
        xfill True
        yfill True
        background Solid("#222")

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

screen panel_room:
    tag menu
    use game_menu(_("Click the panels!"), yinitial=-40):
        # Ensure this replaces the main menu.

        # A grid of buttons.
        vpgrid:
            cols 2
            spacing 5
            draggable True
            mousewheel True
            scrollbars "vertical"
            side_xalign 0.5

            xfill True
            yfill True
            # add gallery.make_button("all", "{{assets}}/freshjamz/00830-316.png", xalign=0.5, yalign=0.5)
            for buttonname in gallery_buttons:
                add gallery.make_button(buttonname, Text(buttonname, style="button_text"), xalign=0.5, yalign=0.5)


init python:

    mr = MusicRoom(fadeout=0.0)

    tracks = filter(
        lambda f: f.lower()[-4:] in [".mp3", ".wav", ".ogg", "flac"],
        renpy.list_files(common=False))

    for track in tracks:
        mr.add(track, always_unlocked=True)

    # def getSongDuration(filepath, sacrifice_channel="sound"):
    #     # prev_volume = renpy.music.set_volume(volume, delay=0, channel=sacrifice_channel)
    #     renpy.music.play(filepath, channel=sacrifice_channel)
    #     duration = renpy.music.get_duration(channel=sacrifice_channel)
    #     renpy.music.stop(channel=sacrifice_channel)
    #     return duration

    def formatSongName(filepath):
        # return filepath
        filename = filepath.split("/")[-1]
        filesub = filepath.split("/")[0].replace("custom_assets_", "")
        ext = filename.split(".")[-1]
        filenamep = ".".join(filename.split(".")[:-1])
        return "[{}] {} ({})".format(filesub, filenamep, ext)


screen music_room:
    tag menu
    use game_menu(_(""), yinitial=-40):
        frame:
            ypos -100
            background Image("{{assets}}/freshjamz/00830-286.png", xpos=-80)
            vbox:
                spacing 10
                image im.FactorScale("{{assets}}/freshjamz/00830-308.png", 2, 2, bilinear=False) xalign 0.5 # yanchor 0.5 
                
                hbox:
                    xalign 0.5
                    # yanchor 0.5
                    spacing 18
                    imagebutton idle im.FactorScale("{{assets}}/freshjamz/00830-316.png", 2, 2, bilinear=False) action (lambda: renpy.music.set_pause(False, channel='music'))
                    imagebutton idle im.FactorScale("{{assets}}/freshjamz/00830-319.png", 2, 2, bilinear=False) action (lambda: renpy.music.set_pause(True, channel='music'))
                    imagebutton idle im.FactorScale("{{assets}}/freshjamz/00830-322.png", 2, 2, bilinear=False) action mr.Previous()
                    imagebutton idle im.FactorScale("{{assets}}/freshjamz/00830-325.png", 2, 2, bilinear=False) action mr.Next()
                    frame:
                        padding (24, 24)
                        background Frame(
                            im.Crop(
                                "{{assets_common}}/openbound_hashbox_round.png",
                                (243, 0, 793, 55)
                            ),
                            left=21, top=21)
                        vbox:
                            xsize 220
                            label _("Music Volume")
                            bar value Preference("music volume")
                    # bar adjustment ui.adjustment(
                #     range=100,
                #     value=1,
                #     adjustable=True
                # )
                frame:
                    xpos 80
                    ypos 0
                    background "{{assets}}/freshjamz/00830-289.png"
                    # background Solid("#0A0")
                    ysize 320
                    xsize 600
                    vbox:
                        viewport:
                            xpos 20
                            mousewheel True
                            scrollbars "vertical"
                            # The buttons that play each track.
                            vbox:
                                ymaximum 5
                                for track in tracks:
                                    hbox:
                                        text "\t"
                                        textbutton formatSongName(track) action mr.Play(track) text_idle_color "#D0004F" text_selected_color "#FF1C87" text_hover_color "#FF1C87"


    # Start the music playing on entry to the music room.
    on "replace" action renpy.music.stop
    # mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action (lambda: renpy.music.set_pause(False, channel='music'))

