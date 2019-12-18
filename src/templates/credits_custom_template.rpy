screen dlc_credits():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"

        vbox:

            spacing 14

{{credits}}

            text "\n\n" text_align 1.0

{{postscript}}
