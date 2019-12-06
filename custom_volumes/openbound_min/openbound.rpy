init offset = 1

# ../custom_volumes_other/openbound\aradia.rpy
define ob_aradia = Character(name="Aradia", show_color="#a10000", kind=openbound, image="ob_aradia")
image ob_aradia happy = Image("{{assets}}/dialogs/aradia_happy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aradia happytalk = Image("{{assets}}/dialogs/aradia_happytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aradia idle = Image("{{assets}}/dialogs/aradia_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aradia laugh = Image("{{assets}}/dialogs/aradia_laugh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aradia point = Image("{{assets}}/dialogs/aradia_point.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aradia talk = Image("{{assets}}/dialogs/aradia_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aradia wink = Image("{{assets}}/dialogs/aradia_wink.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aradia happytalk:
    Image("{{assets}}/dialogs/aradia_happytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/aradia_happytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_aradia talk:
    Image("{{assets}}/dialogs/aradia_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/aradia_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\aranea.rpy
define ob_aranea = Character(name="ARANEA", show_color="#005682", kind=openbound, image="ob_aranea")
image ob_aranea angry = Image("{{assets}}/dialogs/aranea/aranea_angry.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea angrytalk = Image("{{assets}}/dialogs/aranea/aranea_angrytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea annoyed = Image("{{assets}}/dialogs/aranea/aranea_annoyed.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea annoyedtalk = Image("{{assets}}/dialogs/aranea/aranea_annoyedtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea facepalm = Image("{{assets}}/dialogs/aranea/aranea_facepalm.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea facepalmtalk = Image("{{assets}}/dialogs/aranea/aranea_facepalmtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea happier = Image("{{assets}}/dialogs/aranea/aranea_happier.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea happy = Image("{{assets}}/dialogs/aranea/aranea_happy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea happytalk = Image("{{assets}}/dialogs/aranea/aranea_happytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea idle = Image("{{assets}}/dialogs/aranea/aranea_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea mad = Image("{{assets}}/dialogs/aranea/aranea_mad.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea madtalk = Image("{{assets}}/dialogs/aranea/aranea_madtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea surprised = Image("{{assets}}/dialogs/aranea/aranea_surprised.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea talk = Image("{{assets}}/dialogs/aranea/aranea_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea think = Image("{{assets}}/dialogs/aranea/aranea_think.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_aranea angrytalk:
    Image("{{assets}}/dialogs/aranea/aranea_angrytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/aranea/aranea_angrytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_aranea annoyedtalk:
    Image("{{assets}}/dialogs/aranea/aranea_annoyedtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/aranea/aranea_annoyedtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_aranea facepalmtalk:
    Image("{{assets}}/dialogs/aranea/aranea_facepalmtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/aranea/aranea_facepalmtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_aranea happier:
    Image("{{assets}}/dialogs/aranea/aranea_happier-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/aranea/aranea_happier-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_aranea happytalk:
    Image("{{assets}}/dialogs/aranea/aranea_happytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/aranea/aranea_happytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_aranea madtalk:
    Image("{{assets}}/dialogs/aranea/aranea_madtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/aranea/aranea_madtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_aranea talk:
    Image("{{assets}}/dialogs/aranea/aranea_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/aranea/aranea_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\cronus.rpy
define ob_cronus = Character(name="CRONUS", show_color="#6a006a", kind=openbound, image="ob_cronus")
image ob_cronus angry = Image("{{assets}}/dialogs/cronus/cronus_angry.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_cronus bored = Image("{{assets}}/dialogs/cronus/cronus_bored.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_cronus happy = Image("{{assets}}/dialogs/cronus/cronus_happy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_cronus happytalk = Image("{{assets}}/dialogs/cronus/cronus_happytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_cronus huh = Image("{{assets}}/dialogs/cronus/cronus_huh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_cronus idle = Image("{{assets}}/dialogs/cronus/cronus_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_cronus sad2 = Image("{{assets}}/dialogs/cronus/cronus_sad2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_cronus sad = Image("{{assets}}/dialogs/cronus/cronus_sad.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_cronus smug = Image("{{assets}}/dialogs/cronus/cronus_smug.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_cronus surprised = Image("{{assets}}/dialogs/cronus/cronus_surprised.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_cronus talk = Image("{{assets}}/dialogs/cronus/cronus_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_cronus upset2 = Image("{{assets}}/dialogs/cronus/cronus_upset2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_cronus upset = Image("{{assets}}/dialogs/cronus/cronus_upset.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_cronus angry:
    Image("{{assets}}/dialogs/cronus/cronus_angry-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/cronus/cronus_angry-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_cronus bored:
    Image("{{assets}}/dialogs/cronus/cronus_bored-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/cronus/cronus_bored-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_cronus happytalk:
    Image("{{assets}}/dialogs/cronus/cronus_happytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/cronus/cronus_happytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_cronus sad2:
    Image("{{assets}}/dialogs/cronus/cronus_sad2-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/cronus/cronus_sad2-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_cronus talk:
    Image("{{assets}}/dialogs/cronus/cronus_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/cronus/cronus_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
# ../custom_volumes_other/openbound\damara.rpy
define ob_damara = Character(name="DAMARA", show_color="#a10000", kind=openbound, image="ob_damara")
image ob_damara fiendish = Image("{{assets}}/dialogs/damara/damara_fiendish.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara fu1 = Image("{{assets}}/dialogs/damara/damara_fu1.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara fu2 = Image("{{assets}}/dialogs/damara/damara_fu2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara fu3 = Image("{{assets}}/dialogs/damara/damara_fu3.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara fu4 = Image("{{assets}}/dialogs/damara/damara_fu4.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara huh = Image("{{assets}}/dialogs/damara/damara_huh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara huhtalk = Image("{{assets}}/dialogs/damara/damara_huhtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara idle = Image("{{assets}}/dialogs/damara/damara_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara lewd = Image("{{assets}}/dialogs/damara/damara_lewd.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara mean = Image("{{assets}}/dialogs/damara/damara_mean.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara meantalk = Image("{{assets}}/dialogs/damara/damara_meantalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara pissed = Image("{{assets}}/dialogs/damara/damara_pissed.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara sad = Image("{{assets}}/dialogs/damara/damara_sad.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara sadtalk = Image("{{assets}}/dialogs/damara/damara_sadtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara smilemean = Image("{{assets}}/dialogs/damara/damara_smilemean.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara smilemeantalk = Image("{{assets}}/dialogs/damara/damara_smilemeantalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara smile = Image("{{assets}}/dialogs/damara/damara_smile.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara smiletalk = Image("{{assets}}/dialogs/damara/damara_smiletalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara smoke = Image("{{assets}}/dialogs/damara/damara_smoke.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara squint = Image("{{assets}}/dialogs/damara/damara_squint.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara squinttalk = Image("{{assets}}/dialogs/damara/damara_squinttalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara talk = Image("{{assets}}/dialogs/damara/damara_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_damara huhtalk:
    Image("{{assets}}/dialogs/damara/damara_huhtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/damara/damara_huhtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_damara lewd:
    Image("{{assets}}/dialogs/damara/damara_lewd-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/damara/damara_lewd-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_damara meantalk:
    Image("{{assets}}/dialogs/damara/damara_meantalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/damara/damara_meantalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_damara sadtalk:
    Image("{{assets}}/dialogs/damara/damara_sadtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/damara/damara_sadtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_damara smilemeantalk:
    Image("{{assets}}/dialogs/damara/damara_smilemeantalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/damara/damara_smilemeantalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_damara smiletalk:
    Image("{{assets}}/dialogs/damara/damara_smiletalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/damara/damara_smiletalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_damara smoke:
    Image("{{assets}}/dialogs/damara/damara_smoke-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/damara/damara_smoke-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_damara squinttalk:
    Image("{{assets}}/dialogs/damara/damara_squinttalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/damara/damara_squinttalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_damara talk:
    Image("{{assets}}/dialogs/damara/damara_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/damara/damara_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\dave.rpy
define ob_dave = Character(name="DAVE", show_color="#e00707", kind=openbound, image="ob_dave")
image ob_dave concern = Image("{{assets}}/dialogs/dave/dave_concern.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_dave huh = Image("{{assets}}/dialogs/dave/dave_huh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_dave huhtalk = Image("{{assets}}/dialogs/dave/dave_huhtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_dave idle = Image("{{assets}}/dialogs/dave/dave_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_dave mad = Image("{{assets}}/dialogs/dave/dave_mad.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_dave madtalk = Image("{{assets}}/dialogs/dave/dave_madtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_dave smug = Image("{{assets}}/dialogs/dave/dave_smug.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_dave talk = Image("{{assets}}/dialogs/dave/dave_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_dave concern:
    Image("{{assets}}/dialogs/dave/dave_concern-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/dave/dave_concern-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_dave huhtalk:
    Image("{{assets}}/dialogs/dave/dave_huhtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/dave/dave_huhtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_dave madtalk:
    Image("{{assets}}/dialogs/dave/dave_madtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/dave/dave_madtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_dave smug:
    Image("{{assets}}/dialogs/dave/dave_smug-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/dave/dave_smug-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_dave talk:
    Image("{{assets}}/dialogs/dave/dave_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/dave/dave_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\gamzee.rpy
define ob_gamzee = Character(name="GAMZEE", show_color="#2b0057", kind=openbound, image="ob_gamzee")
image ob_gamzee idle = Image("{{assets}}/dialogs/gamzee/gamzee_idle.png", yoffset=-197, xanchor=240, yalign=1.0)

# ../custom_volumes_other/openbound\horuss.rpy
define ob_horuss = Character(name="HORUSS", show_color="#000056", kind=openbound, image="ob_horuss")
image ob_horuss bashful = Image("{{assets}}/dialogs/horuss/horuss_bashful.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss crossed2 = Image("{{assets}}/dialogs/horuss/horuss_crossed2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss crossed = Image("{{assets}}/dialogs/horuss/horuss_crossed.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss grin = Image("{{assets}}/dialogs/horuss/horuss_grin.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss hmm = Image("{{assets}}/dialogs/horuss/horuss_hmm.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss hmmtalk = Image("{{assets}}/dialogs/horuss/horuss_hmmtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss horsedick blur1 = Image("{{assets}}/dialogs/horuss/horuss_horsedick_blur1.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss horsedick blur2 = Image("{{assets}}/dialogs/horuss/horuss_horsedick_blur2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss horsedick blur3 = Image("{{assets}}/dialogs/horuss/horuss_horsedick_blur3.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss horsedick = Image("{{assets}}/dialogs/horuss/horuss_horsedick.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss idle2 = Image("{{assets}}/dialogs/horuss/horuss_idle2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss idle2talk = Image("{{assets}}/dialogs/horuss/horuss_idle2talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss idle = Image("{{assets}}/dialogs/horuss/horuss_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss laugh = Image("{{assets}}/dialogs/horuss/horuss_laugh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss mad = Image("{{assets}}/dialogs/horuss/horuss_mad.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss oops = Image("{{assets}}/dialogs/horuss/horuss_oops.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss sad = Image("{{assets}}/dialogs/horuss/horuss_sad.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss sadtalk = Image("{{assets}}/dialogs/horuss/horuss_sadtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss smile = Image("{{assets}}/dialogs/horuss/horuss_smile.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss smiletalk = Image("{{assets}}/dialogs/horuss/horuss_smiletalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss sweat bashful2 = Image("{{assets}}/dialogs/horuss/horuss_sweat_bashful2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss sweat bashful = Image("{{assets}}/dialogs/horuss/horuss_sweat_bashful.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss sweat grin = Image("{{assets}}/dialogs/horuss/horuss_sweat_grin.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss sweat idle = Image("{{assets}}/dialogs/horuss/horuss_sweat_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss sweat talk = Image("{{assets}}/dialogs/horuss/horuss_sweat_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_horuss bashful:
    Image("{{assets}}/dialogs/horuss/horuss_bashful-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_bashful-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss crossed2:
    Image("{{assets}}/dialogs/horuss/horuss_crossed2-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_crossed2-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss crossed:
    Image("{{assets}}/dialogs/horuss/horuss_crossed-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_crossed-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss hmmtalk:
    Image("{{assets}}/dialogs/horuss/horuss_hmmtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_hmmtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss horsedick blur1:
    Image("{{assets}}/dialogs/horuss/horuss_horsedick_blur1-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_horsedick_blur1-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss horsedick blur2:
    Image("{{assets}}/dialogs/horuss/horuss_horsedick_blur2-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_horsedick_blur2-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss horsedick blur3:
    Image("{{assets}}/dialogs/horuss/horuss_horsedick_blur3-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_horsedick_blur3-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss idle2talk:
    Image("{{assets}}/dialogs/horuss/horuss_idle2talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_idle2talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss laugh:
    Image("{{assets}}/dialogs/horuss/horuss_laugh-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_laugh-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss sadtalk:
    Image("{{assets}}/dialogs/horuss/horuss_sadtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_sadtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss smiletalk:
    Image("{{assets}}/dialogs/horuss/horuss_smiletalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_smiletalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss sweat bashful2:
    Image("{{assets}}/dialogs/horuss/horuss_sweat_bashful2-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_sweat_bashful2-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss sweat bashful:
    Image("{{assets}}/dialogs/horuss/horuss_sweat_bashful-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_sweat_bashful-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss sweat grin:
    Image("{{assets}}/dialogs/horuss/horuss_sweat_grin-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_sweat_grin-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss sweat idle:
    Image("{{assets}}/dialogs/horuss/horuss_sweat_idle-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_sweat_idle-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_horuss sweat talk:
    Image("{{assets}}/dialogs/horuss/horuss_sweat_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/horuss/horuss_sweat_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\kanaya.rpy
define ob_kanaya = Character(name="KANAYA", show_color="#008141", kind=openbound, image="ob_kanaya")
image ob_kanaya angrytalk = Image("{{assets}}/dialogs/kanaya/kanaya_angrytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya bored = Image("{{assets}}/dialogs/kanaya/kanaya_bored.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya cry = Image("{{assets}}/dialogs/kanaya/kanaya_cry.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya facepalm = Image("{{assets}}/dialogs/kanaya/kanaya_facepalm.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya happy = Image("{{assets}}/dialogs/kanaya/kanaya_happy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya happytalk = Image("{{assets}}/dialogs/kanaya/kanaya_happytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya idle = Image("{{assets}}/dialogs/kanaya/kanaya_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya smirklaugh = Image("{{assets}}/dialogs/kanaya/kanaya_smirklaugh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya smirktalk = Image("{{assets}}/dialogs/kanaya/kanaya_smirktalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya talk = Image("{{assets}}/dialogs/kanaya/kanaya_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya angrytalk:
    Image("{{assets}}/dialogs/kanaya/kanaya_angrytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya_angrytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kanaya bored:
    Image("{{assets}}/dialogs/kanaya/kanaya_bored-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya_bored-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kanaya cry:
    Image("{{assets}}/dialogs/kanaya/kanaya_cry-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya_cry-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kanaya facepalm:
    Image("{{assets}}/dialogs/kanaya/kanaya_facepalm-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya_facepalm-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kanaya happytalk:
    Image("{{assets}}/dialogs/kanaya/kanaya_happytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya_happytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kanaya smirklaugh:
    Image("{{assets}}/dialogs/kanaya/kanaya_smirklaugh-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya_smirklaugh-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kanaya smirktalk:
    Image("{{assets}}/dialogs/kanaya/kanaya_smirktalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya_smirktalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kanaya talk:
    Image("{{assets}}/dialogs/kanaya/kanaya_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\kanaya2.rpy
define ob_kanaya2 = Character(name="KANAYA", show_color="#008141", kind=openbound, image="ob_kanaya2")
image ob_kanaya2 bored = Image("{{assets}}/dialogs/kanaya/kanaya2_bored.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya2 cry = Image("{{assets}}/dialogs/kanaya/kanaya2_cry.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya2 facepalm = Image("{{assets}}/dialogs/kanaya/kanaya2_facepalm.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya2 happy = Image("{{assets}}/dialogs/kanaya/kanaya2_happy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya2 happytalk = Image("{{assets}}/dialogs/kanaya/kanaya2_happytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya2 idle = Image("{{assets}}/dialogs/kanaya/kanaya2_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya2 smirklaugh = Image("{{assets}}/dialogs/kanaya/kanaya2_smirklaugh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya2 smirktalk = Image("{{assets}}/dialogs/kanaya/kanaya2_smirktalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya2 talk = Image("{{assets}}/dialogs/kanaya/kanaya2_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kanaya2 bored:
    Image("{{assets}}/dialogs/kanaya/kanaya2_bored-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya2_bored-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kanaya2 cry:
    Image("{{assets}}/dialogs/kanaya/kanaya2_cry-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya2_cry-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kanaya2 facepalm:
    Image("{{assets}}/dialogs/kanaya/kanaya2_facepalm-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya2_facepalm-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kanaya2 happytalk:
    Image("{{assets}}/dialogs/kanaya/kanaya2_happytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya2_happytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kanaya2 smirklaugh:
    Image("{{assets}}/dialogs/kanaya/kanaya2_smirklaugh-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya2_smirklaugh-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kanaya2 smirktalk:
    Image("{{assets}}/dialogs/kanaya/kanaya2_smirktalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya2_smirktalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kanaya2 talk:
    Image("{{assets}}/dialogs/kanaya/kanaya2_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kanaya/kanaya2_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\kankri.rpy
define ob_kankri = Character(name="KANKRI", show_color="#ff0000", kind=openbound, image="ob_kankri")
image ob_kankri glance = Image("{{assets}}/dialogs/kankri/kankri_glance.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kankri idle = Image("{{assets}}/dialogs/kankri/kankri_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kankri rage = Image("{{assets}}/dialogs/kankri/kankri_rage.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kankri talk2 = Image("{{assets}}/dialogs/kankri/kankri_talk2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kankri talk3 = Image("{{assets}}/dialogs/kankri/kankri_talk3.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kankri talk4 = Image("{{assets}}/dialogs/kankri/kankri_talk4.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kankri talk = Image("{{assets}}/dialogs/kankri/kankri_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kankri pray = Image("{{assets}}/dialogs/kankri/kankri_pray.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_kankri rage:
    Image("{{assets}}/dialogs/kankri/kankri_rage-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kankri/kankri_rage-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kankri talk2:
    Image("{{assets}}/dialogs/kankri/kankri_talk2-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kankri/kankri_talk2-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kankri talk3:
    Image("{{assets}}/dialogs/kankri/kankri_talk3-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kankri/kankri_talk3-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kankri talk4:
    Image("{{assets}}/dialogs/kankri/kankri_talk4-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kankri/kankri_talk4-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_kankri talk:
    Image("{{assets}}/dialogs/kankri/kankri_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kankri/kankri_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\karkat.rpy
define ob_karkat = Character(name="KARKAT", show_color="#626262", kind=openbound, image="ob_karkat")
image ob_karkat eyeroll1 = Image("{{assets}}/dialogs/karkat/karkat_eyeroll1.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_karkat eyeroll2 = Image("{{assets}}/dialogs/karkat/karkat_eyeroll2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_karkat facepalm = Image("{{assets}}/dialogs/karkat/karkat_facepalm.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_karkat horror = Image("{{assets}}/dialogs/karkat/karkat_horror.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_karkat idle = Image("{{assets}}/dialogs/karkat/karkat_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_karkat shout = Image("{{assets}}/dialogs/karkat/karkat_shout.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_karkat sullen = Image("{{assets}}/dialogs/karkat/karkat_sullen.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_karkat talk = Image("{{assets}}/dialogs/karkat/karkat_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_karkat what = Image("{{assets}}/dialogs/karkat/karkat_what.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_karkat yell = Image("{{assets}}/dialogs/karkat/karkat_yell.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_karkat facepalm:
    Image("{{assets}}/dialogs/karkat/karkat_facepalm-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/karkat/karkat_facepalm-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_karkat shout:
    Image("{{assets}}/dialogs/karkat/karkat_shout-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/karkat/karkat_shout-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_karkat talk:
    Image("{{assets}}/dialogs/karkat/karkat_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/karkat/karkat_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_karkat yell:
    Image("{{assets}}/dialogs/karkat/karkat_yell-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/karkat/karkat_yell-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\kurloz.rpy
image ob_kurloz angry = Image("{{assets}}/dialogs/kurloz/kurloz_angry.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz annoyed = Image("{{assets}}/dialogs/kurloz/kurloz_annoyed.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz bye = Image("{{assets}}/dialogs/kurloz/kurloz_bye.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz dead = Image("{{assets}}/dialogs/kurloz/kurloz_dead.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz finger = Image("{{assets}}/dialogs/kurloz/kurloz_finger.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz fist = Image("{{assets}}/dialogs/kurloz/kurloz_fist.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz hypno1 = Image("{{assets}}/dialogs/kurloz/kurloz_hypno1.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz hypno2 = Image("{{assets}}/dialogs/kurloz/kurloz_hypno2.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz idle = Image("{{assets}}/dialogs/kurloz/kurloz_idle.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz mime1 = Image("{{assets}}/dialogs/kurloz/kurloz_mime1.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz mime2 = Image("{{assets}}/dialogs/kurloz/kurloz_mime2.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz mime3 = Image("{{assets}}/dialogs/kurloz/kurloz_mime3.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz no = Image("{{assets}}/dialogs/kurloz/kurloz_no.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz shrug = Image("{{assets}}/dialogs/kurloz/kurloz_shrug.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz smile = Image("{{assets}}/dialogs/kurloz/kurloz_smile.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz thumbsup = Image("{{assets}}/dialogs/kurloz/kurloz_thumbsup.png", yoffset=-197, xalign=0.5, yalign=1.0)
image ob_kurloz zip = Image("{{assets}}/dialogs/kurloz/kurloz_zip.png", yoffset=-197, xalign=0.5, yalign=1.0)
define ob_kurloz = Character(name="KURLOZ", show_color="#2b0057", kind=openbound, image="ob_kurloz")
image ob_kurloz dead:
    Image("{{assets}}/dialogs/kurloz/kurloz_dead-0.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_dead-1.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    repeat
image ob_kurloz fist:
    Image("{{assets}}/dialogs/kurloz/kurloz_fist-0.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_fist-1.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    repeat
image ob_kurloz hypno1:
    Image("{{assets}}/dialogs/kurloz/kurloz_hypno1-0.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_hypno1-1.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_hypno1-2.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_hypno1-3.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    repeat
image ob_kurloz hypno2:
    Image("{{assets}}/dialogs/kurloz/kurloz_hypno2-0.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_hypno2-1.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_hypno2-2.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_hypno2-3.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    repeat
image ob_kurloz mime1:
    Image("{{assets}}/dialogs/kurloz/kurloz_mime1-0.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime1-1.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime1-2.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime1-3.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime1-4.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime1-5.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime1-6.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime1-7.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    repeat
image ob_kurloz mime2:
    Image("{{assets}}/dialogs/kurloz/kurloz_mime2-0.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime2-1.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime2-2.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime2-3.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime2-4.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime2-5.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime2-6.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime2-7.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    repeat
image ob_kurloz mime3:
    Image("{{assets}}/dialogs/kurloz/kurloz_mime3-0.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime3-1.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime3-2.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime3-3.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime3-4.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime3-5.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime3-6.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_mime3-7.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    repeat
image ob_kurloz no:
    Image("{{assets}}/dialogs/kurloz/kurloz_no-0.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_no-1.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    repeat
image ob_kurloz thumbsup:
    Image("{{assets}}/dialogs/kurloz/kurloz_thumbsup-0.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_thumbsup-1.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    repeat
image ob_kurloz zip:
    Image("{{assets}}/dialogs/kurloz/kurloz_zip-0.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_zip-1.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/kurloz/kurloz_zip-2.png", yoffset=-197, xalign=0.5, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\latula.rpy
define ob_latula = Character(name="LATULA", show_color="#008282", kind=openbound, image="ob_latula")
image ob_latula angry = Image("{{assets}}/dialogs/latula/latula_angry.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula annoyed = Image("{{assets}}/dialogs/latula/latula_annoyed.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula annoyedtalk = Image("{{assets}}/dialogs/latula/latula_annoyedtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula bored = Image("{{assets}}/dialogs/latula/latula_bored.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula happier = Image("{{assets}}/dialogs/latula/latula_happier.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula happy = Image("{{assets}}/dialogs/latula/latula_happy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula happytalk = Image("{{assets}}/dialogs/latula/latula_happytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula huh = Image("{{assets}}/dialogs/latula/latula_huh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula idle2 = Image("{{assets}}/dialogs/latula/latula_idle2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula idle3 = Image("{{assets}}/dialogs/latula/latula_idle3.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula idle = Image("{{assets}}/dialogs/latula/latula_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula laugh = Image("{{assets}}/dialogs/latula/latula_laugh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula shades1 = Image("{{assets}}/dialogs/latula/latula_shades1.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula shades2 = Image("{{assets}}/dialogs/latula/latula_shades2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula shine = Image("{{assets}}/dialogs/latula/latula_shine.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula stunt = Image("{{assets}}/dialogs/latula/latula_stunt.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula talk = Image("{{assets}}/dialogs/latula/latula_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula tongue = Image("{{assets}}/dialogs/latula/latula_tongue.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_latula angry:
    Image("{{assets}}/dialogs/latula/latula_angry-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/latula/latula_angry-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_latula annoyedtalk:
    Image("{{assets}}/dialogs/latula/latula_annoyedtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/latula/latula_annoyedtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_latula bored:
    Image("{{assets}}/dialogs/latula/latula_bored-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/latula/latula_bored-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_latula happytalk:
    Image("{{assets}}/dialogs/latula/latula_happytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/latula/latula_happytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_latula laugh:
    Image("{{assets}}/dialogs/latula/latula_laugh-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/latula/latula_laugh-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_latula shine:
    Image("{{assets}}/dialogs/latula/latula_shine-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/latula/latula_shine-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/latula/latula_shine-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_latula stunt:
    Image("{{assets}}/dialogs/latula/latula_stunt-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/latula/latula_stunt-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_latula talk:
    Image("{{assets}}/dialogs/latula/latula_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/latula/latula_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\meenah.rpy
define ob_meenah = Character(name="MEENAH", show_color="#77003c", kind=openbound, image="ob_meenah")
image ob_meenah idle = Image("{{assets}}/dialogs/meenah/meenah_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah talk = Image("{{assets}}/dialogs/meenah/meenah_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah angry = Image("{{assets}}/dialogs/meenah/meenah_angry.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah angrytalk = Image("{{assets}}/dialogs/meenah/meenah_angrytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah annoyed = Image("{{assets}}/dialogs/meenah/meenah_annoyed.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah annoyedtalk = Image("{{assets}}/dialogs/meenah/meenah_annoyedtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah creepy = Image("{{assets}}/dialogs/meenah/meenah_creepy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah creepytalk = Image("{{assets}}/dialogs/meenah/meenah_creepytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah creepylaugh = Image("{{assets}}/dialogs/meenah/meenah_creepylaugh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah fish = Image("{{assets}}/dialogs/meenah/meenah_fish.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah fishtalk = Image("{{assets}}/dialogs/meenah/meenah_fishtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah happy = Image("{{assets}}/dialogs/meenah/meenah_happy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah happytalk = Image("{{assets}}/dialogs/meenah/meenah_happytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah happier = Image("{{assets}}/dialogs/meenah/meenah_happier.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah ohyes = Image("{{assets}}/dialogs/meenah/meenah_ohyes.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah wink = Image("{{assets}}/dialogs/meenah/meenah_wink.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah wut = Image("{{assets}}/dialogs/meenah/meenah_wut.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah wut2 = Image("{{assets}}/dialogs/meenah/meenah_wut2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meenah talk:
    Image("{{assets}}/dialogs/meenah/meenah_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meenah/meenah_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meenah angrytalk:
    Image("{{assets}}/dialogs/meenah/meenah_angrytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meenah/meenah_angrytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meenah annoyedtalk:
    Image("{{assets}}/dialogs/meenah/meenah_annoyedtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meenah/meenah_annoyedtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meenah creepytalk:
    Image("{{assets}}/dialogs/meenah/meenah_creepytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meenah/meenah_creepytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meenah creepylaugh:
    Image("{{assets}}/dialogs/meenah/meenah_creepylaugh-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meenah/meenah_creepylaugh-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meenah fishtalk:
    Image("{{assets}}/dialogs/meenah/meenah_fishtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meenah/meenah_fishtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meenah happytalk:
    Image("{{assets}}/dialogs/meenah/meenah_happytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meenah/meenah_happytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meenah wink:
    Image("{{assets}}/dialogs/meenah/meenah_wink-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meenah/meenah_wink-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\memes.rpy
image ob_kurmeme1:
    Image("{{assets}}/interface/backgrounds/kurmeme1-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-11.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-12.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-13.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-14.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-15.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-16.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-17.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-18.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-19.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme1-20.png")
    pause 0.1
    repeat
image ob_kurmeme2:
    Image("{{assets}}/interface/backgrounds/kurmeme2-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-11.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-12.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-13.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-14.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-15.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-16.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-17.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-18.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-19.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-20.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-21.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-22.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-23.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-24.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-25.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-26.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-27.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-28.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme2-29.png")
    pause 0.1
    repeat
image ob_kurmeme3:
    Image("{{assets}}/interface/backgrounds/kurmeme3-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme3-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme3-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme3-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme3-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme3-5.png")
    pause 0.1
    repeat
image ob_kurmeme4:
    Image("{{assets}}/interface/backgrounds/kurmeme4-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme4-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme4-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme4-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme4-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme4-5.png")
    pause 0.1
    repeat
image ob_kurmeme5:
    Image("{{assets}}/interface/backgrounds/kurmeme5-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme5-1.png")
    pause 0.1
    repeat
image ob_kurmeme6:
    Image("{{assets}}/interface/backgrounds/kurmeme6-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme6-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme6-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme6-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme6-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme6-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme6-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme6-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme6-8.png")
    pause 0.1
    repeat
image ob_kurmeme7:
    Image("{{assets}}/interface/backgrounds/kurmeme7-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-11.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-12.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-13.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-14.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-15.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-16.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-17.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-18.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme7-19.png")
    pause 0.1
    repeat
image ob_kurmeme8:
    Image("{{assets}}/interface/backgrounds/kurmeme8-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-11.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-12.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-13.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-14.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-15.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-16.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-17.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-18.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-19.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-20.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-21.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-22.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-23.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-24.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-25.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-26.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-27.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-28.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-29.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-30.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-31.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-32.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-33.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-34.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme8-35.png")
    pause 0.1
    repeat
image ob_kurmeme9:
    Image("{{assets}}/interface/backgrounds/kurmeme9-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-11.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-12.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-13.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-14.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-15.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-16.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-17.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-18.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-19.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-20.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-21.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-22.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-23.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-24.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-25.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-26.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-27.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-28.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-29.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-30.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-31.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-32.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-33.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-34.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/kurmeme9-35.png")
    pause 0.1
    repeat
image ob_meenahmeme:
    Image("{{assets}}/interface/backgrounds/meenahmeme-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-11.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-12.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-13.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-14.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-15.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-16.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-17.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-18.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meenahmeme-19.png")
    pause 0.1
    repeat
image ob_meme1:
    Image("{{assets}}/interface/backgrounds/meme1-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme1-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme1-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme1-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme1-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme1-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme1-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme1-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme1-8.png")
    pause 0.1
    repeat
image ob_meme2:
    Image("{{assets}}/interface/backgrounds/meme2-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme2-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme2-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme2-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme2-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme2-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme2-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme2-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme2-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme2-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme2-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme2-11.png")
    pause 0.1
    repeat
image ob_meme3:
    Image("{{assets}}/interface/backgrounds/meme3-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme3-1.png")
    pause 0.1
    repeat
image ob_meme4:
    Image("{{assets}}/interface/backgrounds/meme4-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme4-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme4-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme4-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme4-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme4-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme4-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme4-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme4-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme4-9.png")
    pause 0.1
    repeat
image ob_meme5:
    Image("{{assets}}/interface/backgrounds/meme5-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-11.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-12.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-13.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-14.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme5-15.png")
    pause 0.1
    repeat
image ob_meme6:
    Image("{{assets}}/interface/backgrounds/meme6-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-11.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-12.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-13.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-14.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-15.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-16.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-17.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-18.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-19.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-20.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-21.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-22.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-23.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-24.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-25.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-26.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme6-27.png")
    pause 0.1
    repeat
image ob_meme7:
    Image("{{assets}}/interface/backgrounds/meme7-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-11.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-12.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-13.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-14.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-15.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-16.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-17.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-18.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-19.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-20.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-21.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-22.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme7-23.png")
    pause 0.1
    repeat
image ob_meme8:
    Image("{{assets}}/interface/backgrounds/meme8-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-11.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-12.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-13.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-14.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-15.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-16.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme8-17.png")
    pause 0.1
    repeat
image ob_meme9:
    Image("{{assets}}/interface/backgrounds/meme9-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-11.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-12.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-13.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-14.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-15.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-16.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-17.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-18.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-19.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-20.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-21.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-22.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme9-23.png")
    pause 0.1
    repeat
image ob_meme10:
    Image("{{assets}}/interface/backgrounds/meme10-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme10-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme10-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme10-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme10-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme10-5.png")
    pause 0.1
    repeat
image ob_meme11:
    Image("{{assets}}/interface/backgrounds/meme11-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme11-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme11-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme11-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme11-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme11-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme11-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme11-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme11-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme11-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme11-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme11-11.png")
    pause 0.1
    repeat
image ob_meme12:
    Image("{{assets}}/interface/backgrounds/meme12-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-11.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-12.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-13.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-14.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-15.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-16.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-17.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-18.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme12-19.png")
    pause 0.1
    repeat
image ob_meme13:
    Image("{{assets}}/interface/backgrounds/meme13-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme13-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme13-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme13-3.png")
    pause 0.1
    repeat
image ob_meme14:
    Image("{{assets}}/interface/backgrounds/meme14-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme14-1.png")
    pause 0.1
    repeat
image ob_meme15:
    Image("{{assets}}/interface/backgrounds/meme15-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme15-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme15-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme15-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme15-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme15-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme15-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme15-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme15-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme15-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme15-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme15-11.png")
    pause 0.1
    repeat
image ob_meme16:
    Image("{{assets}}/interface/backgrounds/meme16-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-11.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-12.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-13.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-14.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme16-15.png")
    pause 0.1
    repeat
image ob_meme17:
    Image("{{assets}}/interface/backgrounds/meme17-0.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-1.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-2.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-3.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-4.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-5.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-6.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-7.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-8.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-9.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-10.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-11.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-12.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-13.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-14.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-15.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-16.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-17.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-18.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-19.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-20.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-21.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-22.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-23.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-24.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-25.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-26.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-27.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-28.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-29.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-30.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-31.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-32.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-33.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-34.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-35.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-36.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-37.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-38.png")
    pause 0.1
    Image("{{assets}}/interface/backgrounds/meme17-39.png")
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\meulin.rpy
define ob_meulin = Character(name="MEULIN", show_color="#416600", kind=openbound, image="ob_meulin")
image ob_meulin dies = Image("{{assets}}/dialogs/meulin/meulin_dies.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin happier = Image("{{assets}}/dialogs/meulin/meulin_happier.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin happiertalk = Image("{{assets}}/dialogs/meulin/meulin_happiertalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin happy = Image("{{assets}}/dialogs/meulin/meulin_happy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin hypno = Image("{{assets}}/dialogs/meulin/meulin_hypno.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin idle = Image("{{assets}}/dialogs/meulin/meulin_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin laugh = Image("{{assets}}/dialogs/meulin/meulin_laugh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin mime1 = Image("{{assets}}/dialogs/meulin/meulin_mime1.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin mime2 = Image("{{assets}}/dialogs/meulin/meulin_mime2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin mime3 = Image("{{assets}}/dialogs/meulin/meulin_mime3.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin mime4 = Image("{{assets}}/dialogs/meulin/meulin_mime4.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin mime5 = Image("{{assets}}/dialogs/meulin/meulin_mime5.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin oops = Image("{{assets}}/dialogs/meulin/meulin_oops.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin talk2 = Image("{{assets}}/dialogs/meulin/meulin_talk2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin talk = Image("{{assets}}/dialogs/meulin/meulin_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin wink = Image("{{assets}}/dialogs/meulin/meulin_wink.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin worry = Image("{{assets}}/dialogs/meulin/meulin_worry.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin worrytalk = Image("{{assets}}/dialogs/meulin/meulin_worrytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin wut = Image("{{assets}}/dialogs/meulin/meulin_wut.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_meulin happiertalk:
    Image("{{assets}}/dialogs/meulin/meulin_happiertalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_happiertalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meulin happy:
    Image("{{assets}}/dialogs/meulin/meulin_happy-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_happy-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meulin hypno:
    Image("{{assets}}/dialogs/meulin/meulin_hypno-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_hypno-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_hypno-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_hypno-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meulin laugh:
    Image("{{assets}}/dialogs/meulin/meulin_laugh-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_laugh-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meulin mime1:
    Image("{{assets}}/dialogs/meulin/meulin_mime1-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime1-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime1-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime1-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime1-4.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime1-5.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime1-6.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime1-7.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meulin mime2:
    Image("{{assets}}/dialogs/meulin/meulin_mime2-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime2-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime2-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime2-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime2-4.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime2-5.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime2-6.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime2-7.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meulin mime3:
    Image("{{assets}}/dialogs/meulin/meulin_mime3-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime3-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime3-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime3-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime3-4.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime3-5.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime3-6.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime3-7.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meulin mime4:
    Image("{{assets}}/dialogs/meulin/meulin_mime4-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime4-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime4-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime4-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime4-4.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime4-5.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime4-6.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime4-7.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meulin mime5:
    Image("{{assets}}/dialogs/meulin/meulin_mime5-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime5-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime5-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime5-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime5-4.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime5-5.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime5-6.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_mime5-7.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meulin talk2:
    Image("{{assets}}/dialogs/meulin/meulin_talk2-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_talk2-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meulin talk:
    Image("{{assets}}/dialogs/meulin/meulin_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_meulin worrytalk:
    Image("{{assets}}/dialogs/meulin/meulin_worrytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/meulin/meulin_worrytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\mituna.rpy
define ob_mituna = Character(name="MITUNA", show_color="#a1a100", kind=openbound, image="ob_mituna")
image ob_mituna agitated = Image("{{assets}}/dialogs/mituna/mituna_agitated.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_mituna angry2 = Image("{{assets}}/dialogs/mituna/mituna_angry2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_mituna angry = Image("{{assets}}/dialogs/mituna/mituna_angry.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_mituna facepalm = Image("{{assets}}/dialogs/mituna/mituna_facepalm.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_mituna happy = Image("{{assets}}/dialogs/mituna/mituna_happy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_mituna happytalk = Image("{{assets}}/dialogs/mituna/mituna_happytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_mituna idle = Image("{{assets}}/dialogs/mituna/mituna_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_mituna laugh = Image("{{assets}}/dialogs/mituna/mituna_laugh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_mituna sad = Image("{{assets}}/dialogs/mituna/mituna_sad.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_mituna shine = Image("{{assets}}/dialogs/mituna/mituna_shine.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_mituna spaz1 = Image("{{assets}}/dialogs/mituna/mituna_spaz1.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_mituna spaz2 = Image("{{assets}}/dialogs/mituna/mituna_spaz2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_mituna talk = Image("{{assets}}/dialogs/mituna/mituna_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_mituna fall = Image("{{assets}}/dialogs/mituna/mituna_fall.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_mituna agitated:
    Image("{{assets}}/dialogs/mituna/mituna_agitated-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_agitated-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_agitated-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_agitated-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_mituna angry2:
    Image("{{assets}}/dialogs/mituna/mituna_angry2-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_angry2-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_angry2-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_angry2-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_mituna angry:
    Image("{{assets}}/dialogs/mituna/mituna_angry-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_angry-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_angry-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_angry-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_mituna happytalk:
    Image("{{assets}}/dialogs/mituna/mituna_happytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_happytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_mituna laugh:
    Image("{{assets}}/dialogs/mituna/mituna_laugh-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_laugh-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_laugh-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_laugh-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_mituna shine:
    Image("{{assets}}/dialogs/mituna/mituna_shine-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_shine-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_shine-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_shine-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_mituna spaz1:
    Image("{{assets}}/dialogs/mituna/mituna_spaz1-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz1-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz1-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz1-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz1-4.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz1-5.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz1-6.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz1-7.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_mituna spaz2:
    Image("{{assets}}/dialogs/mituna/mituna_spaz2-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz2-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz2-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz2-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz2-4.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz2-5.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz2-6.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz2-7.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz2-8.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz2-9.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz2-10.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz2-11.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz2-12.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_spaz2-13.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_mituna talk:
    Image("{{assets}}/dialogs/mituna/mituna_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_mituna fall:
    Image("{{assets}}/dialogs/mituna/mituna_fall-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_fall-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_fall-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/mituna/mituna_fall-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\openbound.rpy

# Start of route
label __package_entrypoint___route:

    # Menu boilerplate: Exit main menu, fade to black
    $ renpy.block_rollback()
    $ main_menu = False
    show image "gui/game_menu.png"
    window hide
    scene black with Dissolve(1.0)
    show blackcover
    $ quick_menu = True

    # Set the scene, fade in from black
    scene bg alternia4
    play music "music/WORST_END.wav" loop
    hide blackcover with dissolve

    show ob_meulin idle
    ob_meulin "!!!"
    show ob_meulin mime2 at left1280 with ease
    
    show ob_kurmeme1 onlayer overlay
    ob_meulin "ob_kurmeme1"
    hide ob_kurmeme1

    show ob_kurmeme2 onlayer overlay
    ob_meulin "ob_kurmeme2"
    hide ob_kurmeme2

    show ob_kurmeme3 onlayer overlay
    ob_meulin "ob_kurmeme3"
    hide ob_kurmeme3

    show ob_kurmeme4 onlayer overlay
    ob_meulin "ob_kurmeme4"
    hide ob_kurmeme4

    show ob_kurmeme5 onlayer overlay
    ob_meulin "ob_kurmeme5"
    hide ob_kurmeme5

    show ob_kurmeme6 onlayer overlay
    ob_meulin "ob_kurmeme6"
    hide ob_kurmeme6

    show ob_kurmeme7 onlayer overlay
    ob_meulin "ob_kurmeme7"
    hide ob_kurmeme7

    show ob_kurmeme8 onlayer overlay
    ob_meulin "ob_kurmeme8"
    hide ob_kurmeme8

    show ob_kurmeme9 onlayer overlay
    ob_meulin "ob_kurmeme9"
    hide ob_kurmeme9

    show ob_meenahmeme onlayer overlay
    ob_meulin "ob_meenahmeme"
    hide ob_meenahmeme

    show ob_meme1 onlayer overlay
    ob_meulin "ob_meme1"
    hide ob_meme1

    show ob_meme2 onlayer overlay
    ob_meulin "ob_meme2"
    hide ob_meme2

    show ob_meme3 onlayer overlay
    ob_meulin "ob_meme3"
    hide ob_meme3

    show ob_meme4 onlayer overlay
    ob_meulin "ob_meme4"
    hide ob_meme4

    show ob_meme5 onlayer overlay
    ob_meulin "ob_meme5"
    hide ob_meme5

    show ob_meme6 onlayer overlay
    ob_meulin "ob_meme6"
    hide ob_meme6

    show ob_meme7 onlayer overlay
    ob_meulin "ob_meme7"
    hide ob_meme7

    show ob_meme8 onlayer overlay
    ob_meulin "ob_meme8"
    hide ob_meme8

    show ob_meme9 onlayer overlay
    ob_meulin "ob_meme9"
    hide ob_meme9

    show ob_meme10 onlayer overlay
    ob_meulin "ob_meme10"
    hide ob_meme10

    show ob_meme11 onlayer overlay
    ob_meulin "ob_meme11"
    hide ob_meme11

    show ob_meme12 onlayer overlay
    ob_meulin "ob_meme12"
    hide ob_meme12

    show ob_meme13 onlayer overlay
    ob_meulin "ob_meme13"
    hide ob_meme13

    show ob_meme14 onlayer overlay
    ob_meulin "ob_meme14"
    hide ob_meme14

    show ob_meme15 onlayer overlay
    ob_meulin "ob_meme15"
    hide ob_meme15

    show ob_meme16 onlayer overlay
    ob_meulin "ob_meme16"
    hide ob_meme16

    show ob_meme17 onlayer overlay
    ob_meulin "ob_meme17"
    hide ob_meme17

    show ob_kurmeme1 onlayer overlay
    ob_meulin "ob_kurmeme1"
    hide ob_kurmeme1

    show ob_kurmeme2 onlayer overlay
    ob_meulin "ob_kurmeme2"
    hide ob_kurmeme2

    show ob_kurmeme3 onlayer overlay
    ob_meulin "ob_kurmeme3"
    hide ob_kurmeme3

    show ob_kurmeme4 onlayer overlay
    ob_meulin "ob_kurmeme4"
    hide ob_kurmeme4

    show ob_kurmeme5 onlayer overlay
    ob_meulin "ob_kurmeme5"
    hide ob_kurmeme5

    show ob_kurmeme6 onlayer overlay
    ob_meulin "ob_kurmeme6"
    hide ob_kurmeme6

    show ob_kurmeme7 onlayer overlay
    ob_meulin "ob_kurmeme7"
    hide ob_kurmeme7

    show ob_kurmeme8 onlayer overlay
    ob_meulin "ob_kurmeme8"
    hide ob_kurmeme8

    show ob_kurmeme9 onlayer overlay
    ob_meulin "ob_kurmeme9"
    hide ob_kurmeme9

    hide ob_meulin

    call debug_dump_character(rb_squarewave)

    call debug_dump_character(rb_dirk)

    call debug_dump_character(ob_aradia)

    call debug_dump_character(ob_meenah)

    call debug_dump_character(ob_aranea)

    call debug_dump_character(ob_dave)

    call debug_dump_character(ob_kanaya)

    call debug_dump_character(ob_rose)

    call debug_dump_character(ob_kankri)

    call debug_dump_character(ob_karkat)

    call debug_dump_character(ob_latula)

    call debug_dump_character(ob_porrim)

    call debug_dump_character(ob_cronus)

    call debug_dump_character(ob_kurloz)

    call debug_dump_character(ob_meulin)

    call debug_dump_character(ob_mituna)

    call debug_dump_character(ob_terezi)

    call debug_dump_character(ob_gamzee)

    call debug_dump_character(ob_damara)

    call debug_dump_character(ob_horuss)

    call debug_dump_character(ob_kanaya2)

    call debug_dump_character(ob_rufioh)


# ../custom_volumes_other/openbound\porrim.rpy
define ob_porrim = Character(name="PORRIM", show_color="#008141", kind=openbound, image="ob_porrim")
image ob_porrim angry2 = Image("{{assets}}/dialogs/porrim/porrim_angry2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim angry = Image("{{assets}}/dialogs/porrim/porrim_angry.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim angrytalk = Image("{{assets}}/dialogs/porrim/porrim_angrytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim annoyed2 = Image("{{assets}}/dialogs/porrim/porrim_annoyed2.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim annoyed = Image("{{assets}}/dialogs/porrim/porrim_annoyed.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim annoyedtalk = Image("{{assets}}/dialogs/porrim/porrim_annoyedtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim happier = Image("{{assets}}/dialogs/porrim/porrim_happier.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim happy = Image("{{assets}}/dialogs/porrim/porrim_happy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim happytalk = Image("{{assets}}/dialogs/porrim/porrim_happytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim idle = Image("{{assets}}/dialogs/porrim/porrim_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim laugh = Image("{{assets}}/dialogs/porrim/porrim_laugh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim light = Image("{{assets}}/dialogs/porrim/porrim_light.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim surprise = Image("{{assets}}/dialogs/porrim/porrim_surprise.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim surprisetalk = Image("{{assets}}/dialogs/porrim/porrim_surprisetalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim talk = Image("{{assets}}/dialogs/porrim/porrim_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_porrim angry2:
    Image("{{assets}}/dialogs/porrim/porrim_angry2-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/porrim/porrim_angry2-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_porrim angrytalk:
    Image("{{assets}}/dialogs/porrim/porrim_angrytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/porrim/porrim_angrytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_porrim annoyed2:
    Image("{{assets}}/dialogs/porrim/porrim_annoyed2-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/porrim/porrim_annoyed2-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_porrim annoyedtalk:
    Image("{{assets}}/dialogs/porrim/porrim_annoyedtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/porrim/porrim_annoyedtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_porrim happytalk:
    Image("{{assets}}/dialogs/porrim/porrim_happytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/porrim/porrim_happytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_porrim laugh:
    Image("{{assets}}/dialogs/porrim/porrim_laugh-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/porrim/porrim_laugh-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_porrim surprisetalk:
    Image("{{assets}}/dialogs/porrim/porrim_surprisetalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/porrim/porrim_surprisetalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_porrim talk:
    Image("{{assets}}/dialogs/porrim/porrim_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/porrim/porrim_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\rapoff.rpy
define rb_dirk = Character("DIRK", kind=pesterchum, what_color="#f2a400", image="rb_dirk")
image rb_dirk idle = im.FactorScale("{{assets}}/rapoff/dirk.png", width=2, bilinear=False, yoffset=-177, xanchor=240, yalign=1.0)

define rb_squarewave = Character(kind=narrator, what_color="#000000", image="rb_squarewave")
image rb_squarewave idle:
    im.FactorScale("{{assets}}/rapoff/squarewave_1.png", width=2, bilinear=False, yoffset=-177,  xanchor=240, yalign=1.0)
    pause 0.1
    im.FactorScale("{{assets}}/rapoff/squarewave_2.png", width=2, bilinear=False, yoffset=-177,  xanchor=240, yalign=1.0)
    pause 0.1
    im.FactorScale("{{assets}}/rapoff/squarewave_3.png", width=2, bilinear=False, yoffset=-177,  xanchor=240, yalign=1.0)
    pause 0.1
    im.FactorScale("{{assets}}/rapoff/squarewave_4.png", width=2, bilinear=False, yoffset=-177,  xanchor=240, yalign=1.0)
    pause 0.1
    im.FactorScale("{{assets}}/rapoff/squarewave_5.png", width=2, bilinear=False, yoffset=-177,  xanchor=240, yalign=1.0)
    pause 0.1
    im.FactorScale("{{assets}}/rapoff/squarewave_6.png", width=2, bilinear=False, yoffset=-177,  xanchor=240, yalign=1.0)
    pause 0.1
    repeat


# ../custom_volumes_other/openbound\rose.rpy
define ob_rose = Character(name="ROSE", show_color="#b536da", kind=openbound, image="ob_rose")
image ob_rose annoyed = Image("{{assets}}/dialogs/rose/rose_annoyed.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rose annoyedtalk = Image("{{assets}}/dialogs/rose/rose_annoyedtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rose concern = Image("{{assets}}/dialogs/rose/rose_concern.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rose coy = Image("{{assets}}/dialogs/rose/rose_coy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rose coytalk = Image("{{assets}}/dialogs/rose/rose_coytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rose happy = Image("{{assets}}/dialogs/rose/rose_happy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rose happytalk = Image("{{assets}}/dialogs/rose/rose_happytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rose idle = Image("{{assets}}/dialogs/rose/rose_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rose laugh = Image("{{assets}}/dialogs/rose/rose_laugh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rose sad = Image("{{assets}}/dialogs/rose/rose_sad.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rose talk = Image("{{assets}}/dialogs/rose/rose_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rose annoyed:
    Image("{{assets}}/dialogs/rose/rose_annoyed-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rose/rose_annoyed-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rose/rose_annoyed-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rose/rose_annoyed-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_rose annoyedtalk:
    Image("{{assets}}/dialogs/rose/rose_annoyedtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rose/rose_annoyedtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_rose concern:
    Image("{{assets}}/dialogs/rose/rose_concern-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rose/rose_concern-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_rose coytalk:
    Image("{{assets}}/dialogs/rose/rose_coytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rose/rose_coytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_rose happytalk:
    Image("{{assets}}/dialogs/rose/rose_happytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rose/rose_happytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_rose idle:
    Image("{{assets}}/dialogs/rose/rose_idle-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rose/rose_idle-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rose/rose_idle-2.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rose/rose_idle-3.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_rose laugh:
    Image("{{assets}}/dialogs/rose/rose_laugh-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rose/rose_laugh-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_rose talk:
    Image("{{assets}}/dialogs/rose/rose_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rose/rose_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\rufioh.rpy
define ob_rufioh = Character(name="RUFIOH", show_color="#000000", kind=openbound, image="ob_rufioh")
image ob_rufioh happy = Image("{{assets}}/dialogs/rufioh/rufioh_happy.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rufioh happytalk = Image("{{assets}}/dialogs/rufioh/rufioh_happytalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rufioh idle = Image("{{assets}}/dialogs/rufioh/rufioh_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rufioh laugh = Image("{{assets}}/dialogs/rufioh/rufioh_laugh.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rufioh no = Image("{{assets}}/dialogs/rufioh/rufioh_no.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rufioh notalk = Image("{{assets}}/dialogs/rufioh/rufioh_notalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rufioh offended = Image("{{assets}}/dialogs/rufioh/rufioh_offended.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rufioh offendedtalk = Image("{{assets}}/dialogs/rufioh/rufioh_offendedtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rufioh sad = Image("{{assets}}/dialogs/rufioh/rufioh_sad.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rufioh sadtalk = Image("{{assets}}/dialogs/rufioh/rufioh_sadtalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rufioh sheepish = Image("{{assets}}/dialogs/rufioh/rufioh_sheepish.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rufioh surprise = Image("{{assets}}/dialogs/rufioh/rufioh_surprise.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rufioh surprisetalk = Image("{{assets}}/dialogs/rufioh/rufioh_surprisetalk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rufioh talk = Image("{{assets}}/dialogs/rufioh/rufioh_talk.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_rufioh happytalk:
    Image("{{assets}}/dialogs/rufioh/rufioh_happytalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rufioh/rufioh_happytalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_rufioh laugh:
    Image("{{assets}}/dialogs/rufioh/rufioh_laugh-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rufioh/rufioh_laugh-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_rufioh notalk:
    Image("{{assets}}/dialogs/rufioh/rufioh_notalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rufioh/rufioh_notalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_rufioh offendedtalk:
    Image("{{assets}}/dialogs/rufioh/rufioh_offendedtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rufioh/rufioh_offendedtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_rufioh sadtalk:
    Image("{{assets}}/dialogs/rufioh/rufioh_sadtalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rufioh/rufioh_sadtalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_rufioh sheepish:
    Image("{{assets}}/dialogs/rufioh/rufioh_sheepish-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rufioh/rufioh_sheepish-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_rufioh surprisetalk:
    Image("{{assets}}/dialogs/rufioh/rufioh_surprisetalk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rufioh/rufioh_surprisetalk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat
image ob_rufioh talk:
    Image("{{assets}}/dialogs/rufioh/rufioh_talk-0.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    Image("{{assets}}/dialogs/rufioh/rufioh_talk-1.png", yoffset=-197, xanchor=240, yalign=1.0)
    pause 0.1
    repeat

# ../custom_volumes_other/openbound\terezi.rpy
define ob_terezi = Character(name="TEREZI", show_color="#008282", kind=openbound, image="ob_terezi")
image ob_terezi idle = Image("{{assets}}/dialogs/terezi/terezi_idle.png", yoffset=-197, xanchor=240, yalign=1.0)
image ob_terezi sad = Image("{{assets}}/dialogs/terezi/terezi_sad.png", yoffset=-197, xanchor=240, yalign=1.0)

