define amisia = Character(name="AMISIA", kind=hiveswap, image="amisia", window_background="gui/textbox_blue.png", who_outlines=[(4, "#000056")])

image amisia axe = Image("{{assets}}/sprite/amisia_axe.png", ypos=730)
image amisia blur2 = Image("{{assets}}/sprite/amisia_blur2.png", ypos=730)
image amisia confess = Image("{{assets}}/sprite/amisia_confess.png", ypos=730)
image amisia doubt = Image("{{assets}}/sprite/amisia_doubt.png", ypos=730)
image amisia frame = Image("{{assets}}/sprite/amisia_frame.png", ypos=730)
image amisia growl = Image("{{assets}}/sprite/amisia_growl.png", ypos=730)
image amisia hairpull = Image("{{assets}}/sprite/amisia_hairpull.png", ypos=730)
image amisia hop = Image("{{assets}}/sprite/amisia_hop.png", ypos=730)
image amisia nya = Image("{{assets}}/sprite/amisia_nya.png", ypos=730)
image amisia ponder = Image("{{assets}}/sprite/amisia_ponder.png", ypos=730)
image amisia smile = Image("{{assets}}/sprite/amisia_smile.png", ypos=730)
image amisia smile2 = Image("{{assets}}/sprite/amisia_smile2.png", ypos=730)
image amisia smug = Image("{{assets}}/sprite/amisia_smug.png", ypos=730)

init python:
    quirks["amisia"] = [("u", "uu")]
