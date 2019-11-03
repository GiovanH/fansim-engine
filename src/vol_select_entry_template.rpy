                imagebutton idle "custom_assets/volumeselect_{volume_id}_small.png" action Jump("{entrypoint}") hovered[
                    SetScreenVariable("icon", "custom_assets/volumeselect_{volume_id}.png"), 
                    SetScreenVariable("title", "{title}"), 
                    SetScreenVariable("subtitle", "{subtitle}")
                ] unhovered[
                    SetScreenVariable("icon", "gui/volumeselect_icon_blank.png"), 
                    SetScreenVariable("title", "Volume Select"), 
                    SetScreenVariable("subtitle", "Hover over an icon!")
                ] alt "{subtitle}"