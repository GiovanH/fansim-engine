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

        print("quirkify=", contents, "with quirklist", quirklist)
        rv = []
        for kind, text in contents:
            print("tag: kind=", kind, "text=", text)
            if kind == renpy.TEXT_TEXT:
                rv += renpy.text.textsupport.tokenize(quirkSub(quirklist, text))
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
