init offset = 0

init python:
    def __p__getNvlHistory(max_no=20):
        collection = []
        for i, h in enumerate(reversed(_history_list)):
            show_args = h.__dict__['show_args']
            if show_args.get("nvlmode"):
                collection.append(h)
            else:
                break

            if i > max_no:
                break
        return reversed(collection)

screen __p__fakenvl_say:
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

screen __p__fakenvl_screen(who, what, **kwargs):
    # Creates a "fake NVL" screen by showing recent history items above the current message.
    # Set show_nvlmode=True to enable, False to disable
    # nvlc_spacing defines the space between entries
    # entry_screen sets a custom say screen. It can take a special who_color argument.

    default nvlmode = kwargs.get("nvlmode", False)
    default nvlc_max = kwargs.get("nvlc_max", 20)
    default nvlc_spacing = kwargs.get("nvlc_spacing", 16)
    default entry_screen = kwargs.get("entry_screen", "__p__fakenvl_say")

    window:
        id "window"
        vbox:
            spacing nvlc_spacing
            if nvlmode:
                for h in __p__getNvlHistory(nvlc_max):
                    use expression entry_screen pass (who=h.who, what=h.what, **h.__dict__['show_args'])
            use expression entry_screen pass (who=who, what=what, **kwargs)

define FakeNVLC = Character(
    screen="__p__fakenvl_screen",
    show_nvlmode=True
)