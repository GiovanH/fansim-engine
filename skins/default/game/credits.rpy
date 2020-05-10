init offset = 1


## About screen ~CHANGES EACH VOLUME~ ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

# screen credits():

#     tag menu

#     ## This use statement includes the game_menu screen inside this one. The
#     ## vbox child is then included inside the viewport inside the game_menu
#     ## screen.
#     use game_menu(_("Credits"), scroll="viewport"):

#         style_prefix "about"

#         vbox:

#             spacing 14

#             text "HOMESTUCK: PESTERQUEST" color gui.accent_color size 48

#             text "EXECUTIVE PRODUCERS" text_align 0.5 color gui.accent_color size 30

#             hbox:
#                 text "ANDREW HUSSIE" text_align 0.0 min_width 440

#             hbox:
#                 text "CINDY DOMINGUEZ" text_align 0.0 min_width 440

#             text "PRODUCER" text_align 0.5 color gui.accent_color size 30

#             hbox:
#                 text "JULIAN DOMINGUEZ" text_align 0.0 min_width 440

#             text "DIRECTOR" text_align 0.5 color gui.accent_color size 30

#             hbox:
#                 text "AYSHA U. FARAH" text_align 0.0 min_width 440

#             text "WRITERS" text_align 0.5 color gui.accent_color size 30

#             text "CHARACTER ARTISTS" text_align 0.5 color gui.accent_color size 30

#             text "BACKGROUND ARTISTS" text_align 0.5 color gui.accent_color size 30

#             hbox:
#                 text "ANDREW HUSSIE" text_align 0.0 min_width 440
#                 text "Prologue" text_align 1.0

#             hbox:
#                 text "XAMAG" text_align 0.0 min_width 440
#                 text "John, Dave" text_align 1.0

#             hbox:
#                 text "COURTNEY BRENDLE" text_align 0.0 min_width 440
#                 text "Rose, Jade, Vriska, Gamzee" text_align 1.0

#             hbox:
#                 text "PHIL GIBSON" text_align 0.0 min_width 440
#                 text "Karkat, Kanaya" text_align 1.0

#             hbox:
#                 text "GINA CHACÓN" text_align 0.0 min_width 440
#                 text "Equius, Terezi" text_align 1.0

#             text "ENDING ILLUSTRATIONS" text_align 0.5 color gui.accent_color size 30

#             text "AUDIO DIRECTOR" text_align 0.5 color gui.accent_color size 30

#             hbox:
#                 text "JAMES ROACH" text_align 0.0 min_width 440

#             text "MUSICIANS" text_align 0.5 color gui.accent_color size 30

#             hbox:
#                 text "JAMES ROACH" text_align 0.0 min_width 440
#                 text "Menu Theme, {i}\"Friendvangelion: Rebuild\"{/i}" text_align 1.0

#             text "GAME DESIGN AND PROGRAMMING" text_align 0.5 color gui.accent_color size 30

#             hbox:
#                 text "MINT CHIPLEAF" text_align 0.0 min_width 440
#                 text "Prologue, Volumes 1, 3, 5, 7" text_align 1.0

#             hbox:
#                 text "DAVID TURNBULL" text_align 0.0 min_width 440
#                 text "Prologue, Volumes 2, 4, 6" text_align 1.0

#             text "\n\n" text_align 1.0

#             text "'Hatch' icons by Carol Liao, provided by {a=https://www.toicon.com/}to [[icon]{/a} under a {a=https://creativecommons.org/licenses/by/4.0/}Creative Commons Attribution 4.0 International License.{/a}"

#             text "Sun image captured by NASA, modified under a {a=https://creativecommons.org/licenses/by/2.0/}Creative Commons Attribution 2.0 Generic license.{/a}"

#             text "Circling fire image by {a=https://pixabay.com/users/mikegi-506967/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1072680}mikegi{/a} from {a=https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1072680}Pixabay{/a}."

#             text "Thank you to {a=https://photomosh.com/}PhotoMosh{/a} for providing an image glitching service."

#             text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


# ## This is redefined in options.rpy to add text to the about screen.
# define gui.about = ""


# style about_label is gui_label
# style about_label_text is gui_label_text
# style about_text is gui_text

# style about_label_text:
#     size gui.label_text_size
