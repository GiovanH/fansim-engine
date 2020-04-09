init offset = 1

define config.name = "Befriendus"
define fse_vol_select_suffix = "New volumes will be released in the future!"
define fse_warnings_prefix = "As a general rule, Befriendus contains adult language, violence, and innuendo. Content warnings for specific routes can be accessed by clicking on the spoiler tags below.\n"

define config.save_directory = "Befriendus"

style fse_volume_select_title:
    font "courbd.ttf" 
    size 48 
    xalign 0.5 
    color "#828282"

style fse_volume_select_subtitle:
    font "courbd.ttf" 
    size 38 
    xalign 0.5 
    color gui.accent_color

style fse_volume_select_author:
    font "courbd.ttf" 
    size 12 
    xalign 1.0 
    text_align 1.0 
    color "#b4b4b5" 

style choice_button_hbox is default:
    properties gui.button_text_properties("choice_button")
    idle_color "#ffffff"
    hover_color "#b4b4b5"

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            button:
                action i.action
                hbox:
                    style_prefix "choice_button"
                    text pick
                    text i.caption 
        # for i in items:
        #     textbutton pick + i.caption action i.action