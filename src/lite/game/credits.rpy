
## About screen ~CHANGES EACH VOLUME~ ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"

        vbox:

            spacing 14

            text "HOMESTUCK: PESTERQUEST" color gui.accent_color size 48

            text "EXECUTIVE PRODUCERS" text_align 0.5 color gui.accent_color size 30

            hbox:
                text "ANDREW HUSSIE" text_align 0.0 min_width 440

            hbox:
                text "CINDY DOMINGUEZ" text_align 0.0 min_width 440

            text "PRODUCER" text_align 0.5 color gui.accent_color size 30

            hbox:
                text "JULIAN DOMINGUEZ" text_align 0.0 min_width 440

            text "DIRECTOR" text_align 0.5 color gui.accent_color size 30

            hbox:
                text "AYSHA U. FARAH" text_align 0.0 min_width 440

            text "WRITERS" text_align 0.5 color gui.accent_color size 30

            hbox:
                text "AYSHA U. FARAH" text_align 0.0 min_width 440
                text "Prologue, Rose, Karkat, Gamzee" text_align 1.0

            hbox:
                text "ANDREW HUSSIE" text_align 0.0 min_width 440
                text "John" text_align 1.0

            hbox:
                text "JAMES ROACH" text_align 0.0 min_width 440
                text "Dave" text_align 1.0

            hbox:
                text "DAVID TURNBULL" text_align 0.0 min_width 440
                text "Jade" text_align 1.0

            hbox:
                text "MAGDALENA CLARK" text_align 0.0 min_width 440
                text "Kanaya" text_align 1.0

            hbox:
                text "KATE MITCHELL" text_align 0.0 min_width 440
                text "Vriska" text_align 1.0

            hbox:
                text "LALO HUNT" text_align 0.0 min_width 440
                text "Equius" text_align 1.0

            hbox:
                text "SARAH ZEDIG" text_align 0.0 min_width 440
                text "Terezi" text_align 1.0

            text "CHARACTER ARTISTS" text_align 0.5 color gui.accent_color size 30

            hbox:
                text "KIM QUACH" text_align 0.0 min_width 440
                text "John" text_align 1.0

            hbox:
                text "BREYA RIVERA" text_align 0.0 min_width 440
                text "Rose, Jade" text_align 1.0

            hbox:
                text "GINA CHACÓN" text_align 0.0 min_width 440
                text "Dave, Karkat, Kanaya" text_align 1.0

            hbox:
                text "HAVEN DANIELS-TAYLOR" text_align 0.0 min_width 440
                text "Gamzee, Vriska" text_align 1.0

            hbox:
                text "XAMAG" text_align 0.0 min_width 440
                text "Equius, Terezi" text_align 1.0

            text "BACKGROUND ARTISTS" text_align 0.5 color gui.accent_color size 30

            hbox:
                text "ANDREW HUSSIE" text_align 0.0 min_width 440
                text "Prologue" text_align 1.0

            hbox:
                text "XAMAG" text_align 0.0 min_width 440
                text "John, Dave" text_align 1.0

            hbox:
                text "COURTNEY BRENDLE" text_align 0.0 min_width 440
                text "Rose, Jade, Vriska, Gamzee" text_align 1.0

            hbox:
                text "PHIL GIBSON" text_align 0.0 min_width 440
                text "Karkat, Kanaya" text_align 1.0

            hbox:
                text "GINA CHACÓN" text_align 0.0 min_width 440
                text "Equius, Terezi" text_align 1.0

            text "ENDING ILLUSTRATIONS" text_align 0.5 color gui.accent_color size 30

            hbox:
                text "XAMAG" text_align 0.0 min_width 440
                text "John, Dave" text_align 1.0

            hbox:
                text "COURTNEY BRENDLE" text_align 0.0 min_width 440
                text "Rose, Jade, Vriska, Gamzee" text_align 1.0

            hbox:
                text "PHIL GIBSON" text_align 0.0 min_width 440
                text "Karkat, Kanaya" text_align 1.0

            hbox:
                text "GINA CHACÓN" text_align 0.0 min_width 440
                text "Equius, Terezi" text_align 1.0

            text "UI DESIGNER" text_align 0.5 color gui.accent_color size 30

            hbox:
                text "DAVID TURNBULL" text_align 0.0 min_width 440

            text "AUDIO DIRECTOR" text_align 0.5 color gui.accent_color size 30

            hbox:
                text "JAMES ROACH" text_align 0.0 min_width 440

            text "MUSICIANS" text_align 0.5 color gui.accent_color size 30

            hbox:
                text "JAMES ROACH" text_align 0.0 min_width 440
                text "Menu Theme, {i}\"Friendvangelion: Rebuild\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "Prologue Theme, {i}\"WORST END\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "John's Theme, {i}\"sometimes i call andrew hussie ‘andy’ and so far he hasn’t corrected me\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "Rose's Theme, {i}\"please support {a=https://www.thetrevorproject.org/}The Trevor Project{/a}\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "Dave Route Prelude, {i}\"2chords\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "Dave's Theme, {i}\"ill probably just name this one something normal oh no wait oh jeez aw beans\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "Dave's Ending Theme, {i}\"24/7 lo fi anime beats to question your sexuality to\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "Jade's Theme, {i}\"JAMES ROACH (FEAT. SPEAK-N-SAY) - CAREFREE VICTORY (REMIX)\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "Karkat's Theme, {i}\"CRUSTacean\"{/i}" text_align 1.0

            hbox: 
                text "" text_align 0.0 min_width 440
                text "Terezi's Theme, " text_align 1.0
                add "gui/qr.png"

            hbox:
                text "TOBY FOX" text_align 0.0 min_width 440
                text "Kanaya's Theme, {i}\"Darling Kanaya\"{/i}" text_align 1.0

            hbox:
                text "TOBY FOX" text_align 0.0 min_width 440
                text "Gamzee's Theme, {i}\"mIrAcLeS\"{/i}" text_align 1.0

            hbox:
                text "MARK HADLEY" text_align 0.0 min_width 440
                text "Gamzee's Theme 2, {i}\"Midnight Calliope\"{/i}" text_align 1.0

            hbox:
                text "YAN \"NUCLEOSE\" RODRIGUEZ" text_align 0.0 min_width 440
                text "Vriska's Theme, {i}\"Superego\"{/i}" text_align 1.0

            hbox:
                text "Paul Tuttle Starr" text_align 0.0 min_width 440
                text "Equius' Theme, {i}\"Indigo Heir\"{/i}" text_align 1.0

            text "GAME DESIGN AND PROGRAMMING" text_align 0.5 color gui.accent_color size 30

            hbox:
                text "MINT CHIPLEAF" text_align 0.0 min_width 440
                text "Prologue, Volumes 1, 3, 5, 7" text_align 1.0

            hbox:
                text "DAVID TURNBULL" text_align 0.0 min_width 440
                text "Prologue, Volumes 2, 4, 6" text_align 1.0

            text "\n\n" text_align 1.0

            text "'Hatch' icons by Carol Liao, provided by {a=https://www.toicon.com/}to [[icon]{/a} under a {a=https://creativecommons.org/licenses/by/4.0/}Creative Commons Attribution 4.0 International License.{/a}"

            text "Sun image captured by NASA, modified under a {a=https://creativecommons.org/licenses/by/2.0/}Creative Commons Attribution 2.0 Generic license.{/a}"

            text "Circling fire image by {a=https://pixabay.com/users/mikegi-506967/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1072680}mikegi{/a} from {a=https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1072680}Pixabay{/a}."

            text "Thank you to {a=https://photomosh.com/}PhotoMosh{/a} for providing an image glitching service."

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

