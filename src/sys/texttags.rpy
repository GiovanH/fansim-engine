init python:

    def texttag_nobreak(tag, argument, contents):
        rv = []

        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                text = text.replace(" ", " ")
            rv.append((kind, text))
        return rv

    config.custom_text_tags["nb"] = texttag_nobreak

    def texttag_nobreak_space(tag, argument):
        return [(renpy.TEXT_TEXT, " ")]

    config.self_closing_custom_text_tags["nbsp"] = texttag_nobreak_space

    def texttag_quirk(tag, argument, contents):

        quirklist = [argument]

        rv = []
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                rv.append((kind, quirkSub(quirklist, text)))
            else:
                rv.append((kind, text))
        return rv

    config.custom_text_tags["quirk"] = texttag_quirk

    def texttag_quirked(tag, argument, contents):

        quirked_text = argument
        has_done = False

        rv = []
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                if has_done:
                    raise Exception("Tag {quirked} cannot contain multiple text segments!")
                rv.append((kind, quirkSubManual(text, quirked_text)))
                has_done = True
            else:
                rv.append((kind, text))
        return rv

    config.custom_text_tags["quirked"] = texttag_quirked

    def texttag_cpsmax(tag, argument):
        # Text speed will not be faster than argument
        def _underflow(v):
            return 999 if v == 0 else v
        target_cps = _underflow(int(argument))
        pref_cps = _underflow(renpy.game.preferences.text_cps)
        cps = min(target_cps, pref_cps)
        cps = 0 if cps > 200 else cps
        return [(renpy.TEXT_TAG, "cps=" + str(cps))]

    config.self_closing_custom_text_tags["cps_max"] = texttag_cpsmax

    # def texttag_hemocolor(tag, argument, contents):
    #     return [(renpy.TEXT_TAG, "color=" + hemospectrum(argument),)] + contents + [(renpy.TEXT_TAG, "/color")]

    # config.custom_text_tags["hemocolor"] = texttag_hemocolor

    # This is the wrong way to do this, but the engine won't let me auto-close tags, so here we are.
    # See renpy/text.py:2242
    def texttag_hemocolor_open(tag, argument):
        return [(renpy.TEXT_TAG, "color=" + hemospectrum(argument),)]

    config.self_closing_custom_text_tags["hemocolor"] = texttag_hemocolor_open

    def texttag_hemocolor_close(tag, argument):
        return [(renpy.TEXT_TAG, "/color")]

    config.self_closing_custom_text_tags["/hemocolor"] = texttag_hemocolor_close