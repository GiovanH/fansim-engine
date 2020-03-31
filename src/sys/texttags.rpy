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