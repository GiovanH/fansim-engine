                imagebutton idle "custom_assets_{package_id}/volumeselect_{volume_id}_small.png" action Jump("{entrypoint}") hovered[
                    SetScreenVariable("icon", "custom_assets_{package_id}/volumeselect_{volume_id}.png"), 
                    SetScreenVariable("title", "{title}"), 
                    SetScreenVariable("subtitle", "{subtitle}"),
                    SetScreenVariable("author", "{author}")
                ] unhovered[
                    ResetVolSelectCustom()
                ] alt "{subtitle}"