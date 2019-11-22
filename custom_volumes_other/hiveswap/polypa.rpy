define polypa = Character(name="POLYPA", kind=hiveswap, image="polypa", window_background="gui/textbox_olive.png", who_outlines=[(4, "#416600")])

image polypa dejected = Image("{{assets}}/sprite/polypa_dejected.png", ypos=730)
image polypa hoodie_intro = Image("{{assets}}/sprite/polypa_hoodie_intro.png", ypos=730)
image polypa hoodie_pissed = Image("{{assets}}/sprite/polypa_hoodie_pissed.png", ypos=730)
image polypa neutral = Image("{{assets}}/sprite/polypa_neutral.png", ypos=730)
image polypa pleased = Image("{{assets}}/sprite/polypa_pleased.png", ypos=730)
image polypa scuffle = Image("{{assets}}/sprite/polypa_scuffle.png", ypos=730)
image polypa serious = Image("{{assets}}/sprite/polypa_serious.png", ypos=730)
image polypa shocked = Image("{{assets}}/sprite/polypa_shocked.png", ypos=730)
image polypa shooshpap = Image("{{assets}}/sprite/polypa_shooshpap.png", ypos=730)

init python:
    quirks["polypa"] = [("(.+)", "<1> *|")]
