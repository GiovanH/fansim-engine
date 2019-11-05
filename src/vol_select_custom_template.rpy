screen vol_select_custom():

    use game_menu_volumes(_("Friend Select"), scroll="viewport"):

        default icon = "gui/volumeselect_icon_blank.png"
        default title = "Volume Select"

        default subtitle = "Hover over an icon for info!"
        default author = "Pesterquest Modsuite"

        vbox:
            xpos 10
            ymaximum 5

            if renpy.variant("android") or renpy.variant("ios"):
                spacing 60
            else:
                spacing 20

            # fixed area contains overlapping elements
            fixed:
                image "gui/volumeselect_background.png" xpos 30
                image icon xpos 50 ypos 15
                text title xpos 526 ypos 32 font "verdana.ttf" size 48 xalign 0.5 color "#b4b4b5"
                text subtitle xpos 526 ypos 90 font "verdana.ttf" size 38 xalign 0.5 color "#00baff"
                text author xpos 860 ypos 160 font "verdana.ttf" size 12 xalign 1.0 text_align 1.0 color "#b4b4b5"

            # null space where fixed area is
            null height 155
            hbox:
                xpos 0
                spacing 10

{{}}

                # these buttons will jump to selected volume, and make the volume number/title appear in the fixed area

    text "do what thou whilst shall be the whole of the law" xpos 460 ypos 635 text_align 0.5
