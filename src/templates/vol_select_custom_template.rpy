init python:
    import random
    def ResetVolSelectCustom():
        SetScreenVariable("icon", "gui/volumeselect_icon_blank.png"), 
        SetScreenVariable("title", "Volume Select"), 
        SetScreenVariable("subtitle", "Hover over an icon!"),
        SetScreenVariable("author", "Pesterquest Modsuite")

    # def customVolumeSplash():
    #     splashes = [
    #         "do what thou whilst shall be the whole of the law",
    #         "Pesterquest Modsuite written by your pal {a=https://twitter.com/giovan_h}Gio{/a}"
    #     ]
    #     return random.choice(splashes)


screen vol_select_custom():

    use game_menu_volumes(_("Friend Select")):

        default icon = "gui/volumeselect_icon_blank.png"
        default title = "Volume Select"

        default subtitle = "Hover over an icon for info!"
        default author = "Pesterquest Modsuite"

        default num_custom_volumes = {{num_custom_volumes}}
        default num_cols = 8

        # fixed area contains overlapping elements
        fixed:
            xpos 10
            image "gui/volumeselect_background.png" xpos 30
            image icon xpos 50 ypos 15
            text title xpos 526 ypos 32 font "verdana.ttf" size 48 xalign 0.5 color "#b4b4b5"
            text subtitle xpos 526 ypos 90 font "verdana.ttf" size 38 xalign 0.5 color "#00baff"
            text author xpos 860 ypos 160 font "verdana.ttf" size 12 xalign 1.0 text_align 1.0 color "#b4b4b5"

        viewport:
            mousewheel True
            scrollbars ("vertical" if num_custom_volumes > (num_cols*3) else None)
            ypos 180
            ysize 350

            vbox:
                null height 20
                vpgrid:
                    xpos 10
                    cols num_cols
                    spacing 10

{{volumes}}

                # these buttons will jump to selected volume, and make the volume number/title appear in the fixed area

        text "do what thou whilst shall be the whole of the law" xalign 0.5 text_align 0.5 ypos 540
        # text customVolumeSplash() 
