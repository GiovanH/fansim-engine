define azdaja = Character(name="AZDAJA", kind=hiveswap, image="azdaja", window_background="gui/textbox_gold.png", who_outlines=[(4, "#a1a100")])

image azdaja analize = Image("{{assets}}/sprite/Azdaja_analize.png", ypos=730)
image azdaja bragging = Image("{{assets}}/sprite/Azdaja_bragging.png", ypos=730)
image azdaja controlled = Image("{{assets}}/sprite/Azdaja_controlled.png", ypos=730)
image azdaja embarrased = Image("{{assets}}/sprite/Azdaja_embarrased.png", ypos=730)
image azdaja neutral = Image("{{assets}}/sprite/Azdaja_neutral.png", ypos=730)
image azdaja pissed = Image("{{assets}}/sprite/Azdaja_pissed.png", ypos=730)
image azdaja power1 = Image("{{assets}}/sprite/Azdaja_power1.png", ypos=730)
image azdaja power2 = Image("{{assets}}/sprite/Azdaja_power2.png", ypos=730)
image azdaja power3 = Image("{{assets}}/sprite/Azdaja_power3.png", ypos=730)
image azdaja power4 = Image("{{assets}}/sprite/Azdaja_power4.png", ypos=730)
image azdaja sayonara = Image("{{assets}}/sprite/Azdaja_sayonara.png", ypos=730)
image azdaja surprise = Image("{{assets}}/sprite/Azdaja_surprise.png", ypos=730)

init python:
    quirks["azdaja"] = [("(.+)", "||| \g<1> |||")]
