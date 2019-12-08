
init offset = -1

## Content warning screen ~CHANGES EACH VOLUME~ ################################################################
##
## This screen lists content warnings per volume
##
screen content_warnings():

    tag menu

    use game_menu(_("Help"), scroll="viewport"):

        default warningoffset = 42

        hbox:
            text "As a general rule, Pesterquest contains adult language, violence, and innuendo. Content warnings for specific routes can be accessed by clicking on the route title."

        hbox:
            textbutton "Edit"
