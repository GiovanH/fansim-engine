define tagora = Character(name="TAGORA", kind=hiveswap, image="tagora", window_background="gui/textbox_teal.png", who_outlines=[(4, "#008282")])

image tagora clasp = Image("{{assets}}/sprite/Tagora_clasp.png", ypos=730)
image tagora document = Image("{{assets}}/sprite/Tagora_document.png", ypos=730)
image tagora ew = Image("{{assets}}/sprite/Tagora_ew.png", ypos=730)
image tagora helpful = Image("{{assets}}/sprite/Tagora_helpful.png", ypos=730)
image tagora hollering = Image("{{assets}}/sprite/Tagora_hollering.png", ypos=730)
image tagora judging = Image("{{assets}}/sprite/Tagora_judging.png", ypos=730)
image tagora nervous = Image("{{assets}}/sprite/Tagora_nervous.png", ypos=730)
image tagora neutral = Image("{{assets}}/sprite/Tagora_neutral.png", ypos=730)
image tagora neutral2 = Image("{{assets}}/sprite/Tagora_neutral2.png", ypos=730)

init python:
    quirks["tagora"] = [("(.+)", "<1>\n\n*__________")]
