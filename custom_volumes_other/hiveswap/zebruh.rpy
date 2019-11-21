define zebruh = Character(name="ZEBRUH", kind=hiveswap, image="zebruh", window_background="gui/textbox_blue.png", who_outlines=[(4, "#000056")])

image zebruh disgust = Image("{{assets}}/sprite/zebruh_disgust.png", ypos=730)
image zebruh displeased = Image("{{assets}}/sprite/zebruh_displeased.png", ypos=730)
image zebruh excited = Image("{{assets}}/sprite/zebruh_excited.png", ypos=730)
image zebruh huh = Image("{{assets}}/sprite/zebruh_huh.png", ypos=730)
image zebruh showoff = Image("{{assets}}/sprite/zebruh_showoff.png", ypos=730)
image zebruh stand = Image("{{assets}}/sprite/zebruh_stand.png", ypos=730)
image zebruh talk = Image("{{assets}}/sprite/zebruh_talk.png", ypos=730)
image zebruh upset = Image("{{assets}}/sprite/zebruh_upset.png", ypos=730)
image zebruh wink = Image("{{assets}}/sprite/zebruh_wink.png", ypos=730)

init python:
    quirks["zebruh_hearts"] = [("(.+)", "{image=char heart} \g<1> {image=char heart}")]
    quirks["zebruh_diamonds"] = [("(.+)", "{image=char diamond} \g<1> {image=char diamond}")]
    quirks["zebruh_clubs"] = [("(.+)", "{image=char club} \g<1> {image=char club}")]
    quirks["zebruh_spades"] = [("(.+)", "{image=char spade} \g<1> {image=char spade}")]
