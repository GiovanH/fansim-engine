init offset = 0

init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=0.0)

    tracks = filter(
        lambda f: f.lower()[-4:] in [".mp3", ".wav", ".ogg", ".flac"],
        renpy.list_files(common=False))

    for track in tracks:
        mr.add(track, always_unlocked=True)

    def formatSongName(filepath):
        return filepath
        # filename = filepath.split("/")[-1]
        # ext = filename.split(".")[-1]
        # filenamep = ".".join(filename.split(".")[:-1])
        # return "{} ({})".format(filenamep, ext)

    # def saveMusic():
    #     bg_old = renpy.music.get_playing(channel='music')


# screen game_menu_square(title, scroll=None, yinitial=0.0):
#     style_prefix "game_menu"
#     if main_menu:
#         add gui.main_menu_background
#     else:
#         add gui.game_menu_background

#     frame:
#         style "game_menu_outer_frame"

#         hbox:

#             ## Reserve space for the navigation section.
#             frame:
#                 style "game_menu_navigation_frame"

#             frame:
#                 style "game_menu_content_frame"

#                 if scroll == "viewport":

#                     viewport:
#                         yinitial yinitial
#                         scrollbars "vertical"
#                         mousewheel True
#                         draggable True

#                         side_yfill True

#                         vbox:
#                             transclude

#                 elif scroll == "vpgrid":

#                     vpgrid:
#                         cols 1
#                         yinitial yinitial

#                         scrollbars "vertical"
#                         mousewheel True
#                         draggable True

#                         side_yfill True

#                         transclude

#                 else:

#                     transclude

#     use navigation

#     label title

#     if renpy.variant("pc"):

#         textbutton _("Quit Game"):

#             style "return_button"
#             action Quit(confirm=not main_menu)


screen music_room:
    tag menu
    use game_menu(_(""), yinitial=-40):
        frame:
            ypos -40
            background Image("{{assets}}/freshjamz/00830-286.png", xpos=-80, ypos=-80)
            vbox:
                spacing 10
                image "{{assets}}/freshjamz/00830-308.png" yanchor 0.5 xalign 0.5
                
                hbox:
                    xalign 0.5
                    spacing 18
                    imagebutton idle "{{assets}}/freshjamz/00830-316.png" action mr.TogglePlay()
                    imagebutton idle "{{assets}}/freshjamz/00830-319.png" action mr.TogglePlay()
                    imagebutton idle "{{assets}}/freshjamz/00830-322.png" action mr.Previous()
                    imagebutton idle "{{assets}}/freshjamz/00830-325.png" action mr.Next()
                frame:
                    xpos 80
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
                frame:
                    ypos 40
                    xpos 80
                    padding (24, 24)
                    background Frame(
                        im.Crop(
                            "{{assets_common}}/openbound_hashbox_round.png",
                            (243, 0, 793, 55)
                        ),
                        left=21, top=21)
                    # background Solid("#0A0")
                    hbox:
                        vbox:
                            xsize 220
                            label _("Music Volume")
                            bar value Preference("music volume")
                        null width 8
                        vbox:
                            xsize 220
                            label _("Sound Volume")
                            bar value Preference("sound volume")

    # Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
    # on "replaced" action Play("music", bg_old)

