init python:
    def ResetVolSelectCustom():
        SetScreenVariable("icon", "gui/volumeselect_icon_blank.png"), 
        SetScreenVariable("title", "Volume Select"), 
        SetScreenVariable("subtitle", "Hover over an icon!"),
        SetScreenVariable("author", "Pesterquest Modsuite")


screen vol_select_custom():

    use game_menu_volumes(_("Friend Select")):

        default icon = "gui/volumeselect_icon_blank.png"
        default title = "Volume Select"

        default subtitle = "Hover over an icon for info!"
        default author = "Pesterquest Modsuite"

        # fixed area contains overlapping elements
        fixed:
            image "gui/volumeselect_background.png" xpos 30
            image icon xpos 50 ypos 15
            text title xpos 526 ypos 32 font "verdana.ttf" size 48 xalign 0.5 color "#b4b4b5"
            text subtitle xpos 526 ypos 90 font "verdana.ttf" size 38 xalign 0.5 color "#00baff"
            text author xpos 860 ypos 160 font "verdana.ttf" size 12 xalign 1.0 text_align 1.0 color "#b4b4b5"

        viewport:
            mousewheel True
            scrollbars "vertical"
            ypos 180
            ysize 300
            vbox:
                xpos 10
                ymaximum 5

                if renpy.variant("android") or renpy.variant("ios"):
                    spacing 60
                else:
                    spacing 20

                # Pad top, but not when scrolled
                null height 10
                hbox:
                    xpos 0
                    spacing 10

{{volumes}}

                # these buttons will jump to selected volume, and make the volume number/title appear in the fixed area

    text "do what thou whilst shall be the whole of the law" xpos 460 ypos 635 text_align 0.5
