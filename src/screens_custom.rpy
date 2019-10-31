screen vol_select_custom():

    use game_menu_volumes(_("Friend Select"), scroll="viewport"):

        default icon = "gui/volumeselect_icon_blank.png"
        default title = "Volume Select"

        default subtitle = "Hover over an icon for info!"

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

            # null space where fixed area is
            null height 155
            hbox:
                xpos 0
                spacing 10

                # these buttons will jump to selected volume, and make the volume number/title appear in the fixed area
                imagebutton auto "assets_custom/volumeselect_iconsmall1_%s.png" action Jump("volume_vriska_custom") hovered[
                    SetScreenVariable("icon", "assets_custom/volumeselect_icon1_idle.png"), 
                    SetScreenVariable("title", "Volume 1"), 
                    SetScreenVariable("subtitle", "\"you know what it be\"")
                ] unhovered[
                    SetScreenVariable("icon", "gui/volumeselect_icon_blank.png"), 
                    SetScreenVariable("title", "Volume Select"), 
                    SetScreenVariable("subtitle", "Hover over an icon!")
                ] alt "you know what it be"

    text "do what thou whilst shall be the whole of the law" xpos 460 ypos 635 text_align 0.5
