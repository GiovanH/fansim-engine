
# Start of route
label {{package_entrypoint}}_route:

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

    show rb_squarewave idle
    rb_squarewave "squarewave"
    hide rb_squarewave

    show rb_dirk idle
    rb_dirk "dirk"
    hide rb_dirk


    show ob_aradia idle
    ob_aradia happy "aradia_happy"
    ob_aradia happytalk "aradia_happytalk"
    ob_aradia idle "aradia_idle"
    ob_aradia laugh "aradia_laugh"
    ob_aradia point "aradia_point"
    ob_aradia talk "aradia_talk"
    ob_aradia wink "aradia_wink"
    hide ob_aradia

    show ob_meenah idle
    ob_meenah idle "meenah_idle"
    ob_meenah talk "meenah_talk"
    ob_meenah angry "meenah_angry"
    ob_meenah angrytalk "meenah_angrytalk"
    ob_meenah annoyed "meenah_annoyed"
    ob_meenah annoyedtalk "meenah_annoyedtalk"
    ob_meenah creepy "meenah_creepy"
    ob_meenah creepytalk "meenah_creepytalk"
    ob_meenah creepylaugh "meenah_creepylaugh"
    ob_meenah fish "meenah_fish"
    ob_meenah fishtalk "meenah_fishtalk"
    ob_meenah happy "meenah_happy"
    ob_meenah happytalk "meenah_happytalk"
    ob_meenah happier "meenah_happier"
    ob_meenah ohyes "meenah_ohyes"
    ob_meenah wink "meenah_wink"
    ob_meenah wut "meenah_wut"
    ob_meenah wut2 "meenah_wut2"
    ob_meenah idle "meenah_idle"
    ob_meenah talk "meenah_talk"
    ob_meenah angry "meenah_angry"
    ob_meenah angrytalk "meenah_angrytalk"
    ob_meenah annoyed "meenah_annoyed"
    ob_meenah annoyedtalk "meenah_annoyedtalk"
    ob_meenah creepy "meenah_creepy"
    ob_meenah creepytalk "meenah_creepytalk"
    ob_meenah creepylaugh "meenah_creepylaugh"
    ob_meenah fish "meenah_fish"
    ob_meenah fishtalk "meenah_fishtalk"
    ob_meenah happy "meenah_happy"
    ob_meenah happytalk "meenah_happytalk"
    ob_meenah happier "meenah_happier"
    ob_meenah ohyes "meenah_ohyes"
    ob_meenah wink "meenah_wink"
    ob_meenah wut "meenah_wut"
    ob_meenah wut2 "meenah_wut2"
    ob_meenah idle "meenah_idle"
    ob_meenah talk "meenah_talk"
    ob_meenah angry "meenah_angry"
    ob_meenah angrytalk "meenah_angrytalk"
    ob_meenah annoyed "meenah_annoyed"
    ob_meenah annoyedtalk "meenah_annoyedtalk"
    ob_meenah creepy "meenah_creepy"
    ob_meenah creepytalk "meenah_creepytalk"
    ob_meenah creepylaugh "meenah_creepylaugh"
    ob_meenah fish "meenah_fish"
    ob_meenah fishtalk "meenah_fishtalk"
    ob_meenah happy "meenah_happy"
    ob_meenah happytalk "meenah_happytalk"
    ob_meenah happier "meenah_happier"
    ob_meenah ohyes "meenah_ohyes"
    ob_meenah wink "meenah_wink"
    ob_meenah wut "meenah_wut"
    ob_meenah wut2 "meenah_wut2"
    hide ob_meenah

    show ob_aranea idle
    ob_aranea angry "aranea_angry"
    ob_aranea angrytalk "aranea_angrytalk"
    ob_aranea annoyed "aranea_annoyed"
    ob_aranea annoyedtalk "aranea_annoyedtalk"
    ob_aranea facepalm "aranea_facepalm"
    ob_aranea facepalmtalk "aranea_facepalmtalk"
    ob_aranea happier "aranea_happier"
    ob_aranea happy "aranea_happy"
    ob_aranea happytalk "aranea_happytalk"
    ob_aranea idle "aranea_idle"
    ob_aranea mad "aranea_mad"
    ob_aranea madtalk "aranea_madtalk"
    ob_aranea surprised "aranea_surprised"
    ob_aranea talk "aranea_talk"
    ob_aranea think "aranea_think"
    ob_aranea angry "aranea_angry"
    ob_aranea angrytalk "aranea_angrytalk"
    ob_aranea annoyed "aranea_annoyed"
    ob_aranea annoyedtalk "aranea_annoyedtalk"
    ob_aranea facepalm "aranea_facepalm"
    ob_aranea facepalmtalk "aranea_facepalmtalk"
    ob_aranea happier "aranea_happier"
    ob_aranea happy "aranea_happy"
    ob_aranea happytalk "aranea_happytalk"
    ob_aranea idle "aranea_idle"
    ob_aranea mad "aranea_mad"
    ob_aranea madtalk "aranea_madtalk"
    ob_aranea surprised "aranea_surprised"
    ob_aranea talk "aranea_talk"
    ob_aranea think "aranea_think"
    ob_aranea angry "aranea_angry"
    ob_aranea angrytalk "aranea_angrytalk"
    ob_aranea annoyed "aranea_annoyed"
    ob_aranea annoyedtalk "aranea_annoyedtalk"
    ob_aranea facepalm "aranea_facepalm"
    ob_aranea facepalmtalk "aranea_facepalmtalk"
    ob_aranea happier "aranea_happier"
    ob_aranea happy "aranea_happy"
    ob_aranea happytalk "aranea_happytalk"
    ob_aranea idle "aranea_idle"
    ob_aranea mad "aranea_mad"
    ob_aranea madtalk "aranea_madtalk"
    ob_aranea surprised "aranea_surprised"
    ob_aranea talk "aranea_talk"
    ob_aranea think "aranea_think"
    hide ob_aranea

    show ob_dave idle
    ob_dave concern "dave_concern"
    ob_dave huh "dave_huh"
    ob_dave huhtalk "dave_huhtalk"
    ob_dave idle "dave_idle"
    ob_dave mad "dave_mad"
    ob_dave madtalk "dave_madtalk"
    ob_dave smug "dave_smug"
    ob_dave talk "dave_talk"
    ob_dave concern "dave_concern"
    ob_dave huh "dave_huh"
    ob_dave huhtalk "dave_huhtalk"
    ob_dave idle "dave_idle"
    ob_dave mad "dave_mad"
    ob_dave madtalk "dave_madtalk"
    ob_dave smug "dave_smug"
    ob_dave talk "dave_talk"
    hide ob_dave

    show ob_kanaya idle
    ob_kanaya angrytalk "kanaya_angrytalk"
    ob_kanaya bored "kanaya_bored"
    ob_kanaya cry "kanaya_cry"
    ob_kanaya facepalm "kanaya_facepalm"
    ob_kanaya happy "kanaya_happy"
    ob_kanaya happytalk "kanaya_happytalk"
    ob_kanaya idle "kanaya_idle"
    ob_kanaya smirklaugh "kanaya_smirklaugh"
    ob_kanaya smirktalk "kanaya_smirktalk"
    ob_kanaya talk "kanaya_talk"
    ob_kanaya angrytalk "kanaya_angrytalk"
    ob_kanaya bored "kanaya_bored"
    ob_kanaya cry "kanaya_cry"
    ob_kanaya facepalm "kanaya_facepalm"
    ob_kanaya happy "kanaya_happy"
    ob_kanaya happytalk "kanaya_happytalk"
    ob_kanaya idle "kanaya_idle"
    ob_kanaya smirklaugh "kanaya_smirklaugh"
    ob_kanaya smirktalk "kanaya_smirktalk"
    ob_kanaya talk "kanaya_talk"
    hide ob_kanaya

    show ob_rose idle
    ob_rose annoyed "rose_annoyed"
    ob_rose annoyedtalk "rose_annoyedtalk"
    ob_rose concern "rose_concern"
    ob_rose coy "rose_coy"
    ob_rose coytalk "rose_coytalk"
    ob_rose happy "rose_happy"
    ob_rose happytalk "rose_happytalk"
    ob_rose idle "rose_idle"
    ob_rose laugh "rose_laugh"
    ob_rose sad "rose_sad"
    ob_rose talk "rose_talk"
    ob_rose annoyed "rose_annoyed"
    ob_rose annoyedtalk "rose_annoyedtalk"
    ob_rose concern "rose_concern"
    ob_rose coy "rose_coy"
    ob_rose coytalk "rose_coytalk"
    ob_rose happy "rose_happy"
    ob_rose happytalk "rose_happytalk"
    ob_rose idle "rose_idle"
    ob_rose laugh "rose_laugh"
    ob_rose sad "rose_sad"
    ob_rose talk "rose_talk"
    hide ob_rose

    show ob_kankri idle
    ob_kankri glance "kankri_glance"
    ob_kankri idle "kankri_idle"
    ob_kankri rage "kankri_rage"
    ob_kankri talk2 "kankri_talk2"
    ob_kankri talk3 "kankri_talk3"
    ob_kankri talk4 "kankri_talk4"
    ob_kankri talk "kankri_talk"
    ob_kankri pray "kankri_pray"
    ob_kankri glance "kankri_glance"
    ob_kankri idle "kankri_idle"
    ob_kankri rage "kankri_rage"
    ob_kankri talk2 "kankri_talk2"
    ob_kankri talk3 "kankri_talk3"
    ob_kankri talk4 "kankri_talk4"
    ob_kankri talk "kankri_talk"
    ob_kankri pray "kankri_pray"
    ob_kankri glance "kankri_glance"
    ob_kankri idle "kankri_idle"
    ob_kankri rage "kankri_rage"
    ob_kankri talk2 "kankri_talk2"
    ob_kankri talk3 "kankri_talk3"
    ob_kankri talk4 "kankri_talk4"
    ob_kankri talk "kankri_talk"
    ob_kankri whistle "kankri_whistle"
    hide ob_kankri

    show ob_karkat idle
    ob_karkat eyeroll1 "karkat_eyeroll1"
    ob_karkat eyeroll2 "karkat_eyeroll2"
    ob_karkat facepalm "karkat_facepalm"
    ob_karkat horror "karkat_horror"
    ob_karkat idle "karkat_idle"
    ob_karkat shout "karkat_shout"
    ob_karkat sullen "karkat_sullen"
    ob_karkat talk "karkat_talk"
    ob_karkat what "karkat_what"
    ob_karkat yell "karkat_yell"
    ob_karkat eyeroll1 "karkat_eyeroll1"
    ob_karkat eyeroll2 "karkat_eyeroll2"
    ob_karkat facepalm "karkat_facepalm"
    ob_karkat horror "karkat_horror"
    ob_karkat idle "karkat_idle"
    ob_karkat shout "karkat_shout"
    ob_karkat sullen "karkat_sullen"
    ob_karkat talk "karkat_talk"
    ob_karkat what "karkat_what"
    ob_karkat yell "karkat_yell"
    ob_karkat eyeroll1 "karkat_eyeroll1"
    ob_karkat eyeroll2 "karkat_eyeroll2"
    ob_karkat facepalm "karkat_facepalm"
    ob_karkat horror "karkat_horror"
    ob_karkat idle "karkat_idle"
    ob_karkat shout "karkat_shout"
    ob_karkat sullen "karkat_sullen"
    ob_karkat talk "karkat_talk"
    ob_karkat what "karkat_what"
    ob_karkat yell "karkat_yell"
    hide ob_karkat

    show ob_latula idle
    ob_latula angry "latula_angry"
    ob_latula annoyed "latula_annoyed"
    ob_latula annoyedtalk "latula_annoyedtalk"
    ob_latula bored "latula_bored"
    ob_latula happier "latula_happier"
    ob_latula happy "latula_happy"
    ob_latula happytalk "latula_happytalk"
    ob_latula huh "latula_huh"
    ob_latula idle2 "latula_idle2"
    ob_latula idle3 "latula_idle3"
    ob_latula idle "latula_idle"
    ob_latula laugh "latula_laugh"
    ob_latula shades1 "latula_shades1"
    ob_latula shades2 "latula_shades2"
    ob_latula shine "latula_shine"
    ob_latula stunt "latula_stunt"
    ob_latula talk "latula_talk"
    ob_latula tongue "latula_tongue"
    ob_latula angry "latula_angry"
    ob_latula annoyed "latula_annoyed"
    ob_latula annoyedtalk "latula_annoyedtalk"
    ob_latula bored "latula_bored"
    ob_latula happier "latula_happier"
    ob_latula happy "latula_happy"
    ob_latula happytalk "latula_happytalk"
    ob_latula huh "latula_huh"
    ob_latula idle2 "latula_idle2"
    ob_latula idle3 "latula_idle3"
    ob_latula idle "latula_idle"
    ob_latula laugh "latula_laugh"
    ob_latula shades1 "latula_shades1"
    ob_latula shades2 "latula_shades2"
    ob_latula shine "latula_shine"
    ob_latula stunt "latula_stunt"
    ob_latula talk "latula_talk"
    ob_latula tongue "latula_tongue"
    hide ob_latula

    show ob_porrim idle
    ob_porrim angry2 "porrim_angry2"
    ob_porrim angry "porrim_angry"
    ob_porrim angrytalk "porrim_angrytalk"
    ob_porrim annoyed2 "porrim_annoyed2"
    ob_porrim annoyed "porrim_annoyed"
    ob_porrim annoyedtalk "porrim_annoyedtalk"
    ob_porrim happier "porrim_happier"
    ob_porrim happy "porrim_happy"
    ob_porrim happytalk "porrim_happytalk"
    ob_porrim idle "porrim_idle"
    ob_porrim laugh "porrim_laugh"
    ob_porrim light "porrim_light"
    ob_porrim surprise "porrim_surprise"
    ob_porrim surprisetalk "porrim_surprisetalk"
    ob_porrim talk "porrim_talk"
    ob_porrim angry2 "porrim_angry2"
    ob_porrim angry "porrim_angry"
    ob_porrim angrytalk "porrim_angrytalk"
    ob_porrim annoyed2 "porrim_annoyed2"
    ob_porrim annoyed "porrim_annoyed"
    ob_porrim annoyedtalk "porrim_annoyedtalk"
    ob_porrim happier "porrim_happier"
    ob_porrim happy "porrim_happy"
    ob_porrim happytalk "porrim_happytalk"
    ob_porrim idle "porrim_idle"
    ob_porrim laugh "porrim_laugh"
    ob_porrim light "porrim_light"
    ob_porrim surprise "porrim_surprise"
    ob_porrim surprisetalk "porrim_surprisetalk"
    ob_porrim talk "porrim_talk"
    hide ob_porrim

    show ob_cronus idle
    ob_cronus angry "cronus_angry"
    ob_cronus bored "cronus_bored"
    ob_cronus happy "cronus_happy"
    ob_cronus happytalk "cronus_happytalk"
    ob_cronus huh "cronus_huh"
    ob_cronus idle "cronus_idle"
    ob_cronus sad2 "cronus_sad2"
    ob_cronus sad "cronus_sad"
    ob_cronus smug "cronus_smug"
    ob_cronus surprised "cronus_surprised"
    ob_cronus talk "cronus_talk"
    ob_cronus upset2 "cronus_upset2"
    ob_cronus upset "cronus_upset"
    ob_cronus angry "cronus_angry"
    ob_cronus bored "cronus_bored"
    ob_cronus happy "cronus_happy"
    ob_cronus happytalk "cronus_happytalk"
    ob_cronus huh "cronus_huh"
    ob_cronus idle "cronus_idle"
    ob_cronus sad2 "cronus_sad2"
    ob_cronus sad "cronus_sad"
    ob_cronus smug "cronus_smug"
    ob_cronus surprised "cronus_surprised"
    ob_cronus talk "cronus_talk"
    ob_cronus upset2 "cronus_upset2"
    ob_cronus upset "cronus_upset"
    hide ob_cronus

    show ob_kurloz idle
    ob_kurloz angry "kurloz_angry"
    ob_kurloz annoyed "kurloz_annoyed"
    ob_kurloz bye "kurloz_bye"
    ob_kurloz dead "kurloz_dead"
    ob_kurloz finger "kurloz_finger"
    ob_kurloz fist "kurloz_fist"
    ob_kurloz hypno1 "kurloz_hypno1"
    ob_kurloz hypno2 "kurloz_hypno2"
    ob_kurloz idle "kurloz_idle"
    ob_kurloz mime1 "kurloz_mime1"
    ob_kurloz mime2 "kurloz_mime2"
    ob_kurloz mime3 "kurloz_mime3"
    ob_kurloz no "kurloz_no"
    ob_kurloz shrug "kurloz_shrug"
    ob_kurloz smile "kurloz_smile"
    ob_kurloz thumbsup "kurloz_thumbsup"
    ob_kurloz zip "kurloz_zip"
    ob_kurloz angry "kurloz_angry"
    ob_kurloz annoyed "kurloz_annoyed"
    ob_kurloz bye "kurloz_bye"
    ob_kurloz dead "kurloz_dead"
    ob_kurloz finger "kurloz_finger"
    ob_kurloz fist "kurloz_fist"
    ob_kurloz hypno1 "kurloz_hypno1"
    ob_kurloz hypno2 "kurloz_hypno2"
    ob_kurloz idle "kurloz_idle"
    ob_kurloz mime1 "kurloz_mime1"
    ob_kurloz mime2 "kurloz_mime2"
    ob_kurloz mime3 "kurloz_mime3"
    ob_kurloz no "kurloz_no"
    ob_kurloz shrug "kurloz_shrug"
    ob_kurloz smile "kurloz_smile"
    ob_kurloz thumbsup "kurloz_thumbsup"
    ob_kurloz zip "kurloz_zip"
    hide ob_kurloz

    show ob_meulin idle
    ob_meulin dies "meulin_dies"
    ob_meulin happier "meulin_happier"
    ob_meulin happiertalk "meulin_happiertalk"
    ob_meulin happy "meulin_happy"
    ob_meulin hypno "meulin_hypno"
    ob_meulin idle "meulin_idle"
    ob_meulin laugh "meulin_laugh"
    ob_meulin mime1 "meulin_mime1"
    ob_meulin mime2 "meulin_mime2"
    ob_meulin mime3 "meulin_mime3"
    ob_meulin mime4 "meulin_mime4"
    ob_meulin mime5 "meulin_mime5"
    ob_meulin oops "meulin_oops"
    ob_meulin talk2 "meulin_talk2"
    ob_meulin talk "meulin_talk"
    ob_meulin wink "meulin_wink"
    ob_meulin worry "meulin_worry"
    ob_meulin worrytalk "meulin_worrytalk"
    ob_meulin wut "meulin_wut"
    ob_meulin dies "meulin_dies"
    ob_meulin happier "meulin_happier"
    ob_meulin happiertalk "meulin_happiertalk"
    ob_meulin happy "meulin_happy"
    ob_meulin hypno "meulin_hypno"
    ob_meulin idle "meulin_idle"
    ob_meulin laugh "meulin_laugh"
    ob_meulin mime1 "meulin_mime1"
    ob_meulin mime2 "meulin_mime2"
    ob_meulin mime3 "meulin_mime3"
    ob_meulin mime4 "meulin_mime4"
    ob_meulin mime5 "meulin_mime5"
    ob_meulin oops "meulin_oops"
    ob_meulin talk2 "meulin_talk2"
    ob_meulin talk "meulin_talk"
    ob_meulin wink "meulin_wink"
    ob_meulin worry "meulin_worry"
    ob_meulin worrytalk "meulin_worrytalk"
    ob_meulin wut "meulin_wut"
    hide ob_meulin

    show ob_mituna idle
    ob_mituna agitated "mituna_agitated"
    ob_mituna angry2 "mituna_angry2"
    ob_mituna angry "mituna_angry"
    ob_mituna facepalm "mituna_facepalm"
    ob_mituna happy "mituna_happy"
    ob_mituna happytalk "mituna_happytalk"
    ob_mituna idle "mituna_idle"
    ob_mituna laugh "mituna_laugh"
    ob_mituna sad "mituna_sad"
    ob_mituna shine "mituna_shine"
    ob_mituna spaz1 "mituna_spaz1"
    ob_mituna spaz2 "mituna_spaz2"
    ob_mituna talk "mituna_talk"
    ob_mituna fall "mituna_fall"
    ob_mituna agitated "mituna_agitated"
    ob_mituna angry2 "mituna_angry2"
    ob_mituna angry "mituna_angry"
    ob_mituna facepalm "mituna_facepalm"
    ob_mituna happy "mituna_happy"
    ob_mituna happytalk "mituna_happytalk"
    ob_mituna idle "mituna_idle"
    ob_mituna laugh "mituna_laugh"
    ob_mituna sad "mituna_sad"
    ob_mituna shine "mituna_shine"
    ob_mituna spaz1 "mituna_spaz1"
    ob_mituna spaz2 "mituna_spaz2"
    ob_mituna talk "mituna_talk"
    ob_mituna fall "mituna_fall"
    hide ob_mituna

    show ob_terezi idle
    ob_terezi idle "terezi_idle"
    ob_terezi sad "terezi_sad"
    ob_terezi idle "terezi_idle"
    ob_terezi sad "terezi_sad"
    hide ob_terezi

    show ob_gamzee idle
    ob_gamzee idle "gamzee_idle"
    ob_gamzee idle "gamzee_idle"
    hide ob_gamzee

    show ob_damara idle
    ob_damara fiendish "damara_fiendish"
    ob_damara fu1 "damara_fu1"
    ob_damara fu2 "damara_fu2"
    ob_damara fu3 "damara_fu3"
    ob_damara fu4 "damara_fu4"
    ob_damara huh "damara_huh"
    ob_damara huhtalk "damara_huhtalk"
    ob_damara idle "damara_idle"
    ob_damara lewd "damara_lewd"
    ob_damara mean "damara_mean"
    ob_damara meantalk "damara_meantalk"
    ob_damara pissed "damara_pissed"
    ob_damara sad "damara_sad"
    ob_damara sadtalk "damara_sadtalk"
    ob_damara smilemean "damara_smilemean"
    ob_damara smilemeantalk "damara_smilemeantalk"
    ob_damara smile "damara_smile"
    ob_damara smiletalk "damara_smiletalk"
    ob_damara smoke "damara_smoke"
    ob_damara squint "damara_squint"
    ob_damara squinttalk "damara_squinttalk"
    ob_damara talk "damara_talk"
    hide ob_damara

    show ob_horuss idle
    ob_horuss bashful "horuss_bashful"
    ob_horuss crossed2 "horuss_crossed2"
    ob_horuss crossed "horuss_crossed"
    ob_horuss grin "horuss_grin"
    ob_horuss hmm "horuss_hmm"
    ob_horuss hmmtalk "horuss_hmmtalk"
    ob_horuss horsedick blur1 "horuss_horsedick_blur1"
    ob_horuss horsedick blur2 "horuss_horsedick_blur2"
    ob_horuss horsedick blur3 "horuss_horsedick_blur3"
    ob_horuss horsedick "horuss_horsedick"
    ob_horuss idle2 "horuss_idle2"
    ob_horuss idle2talk "horuss_idle2talk"
    ob_horuss idle "horuss_idle"
    ob_horuss laugh "horuss_laugh"
    ob_horuss mad "horuss_mad"
    ob_horuss oops "horuss_oops"
    ob_horuss sad "horuss_sad"
    ob_horuss sadtalk "horuss_sadtalk"
    ob_horuss smile "horuss_smile"
    ob_horuss smiletalk "horuss_smiletalk"
    ob_horuss sweat bashful2 "horuss_sweat_bashful2"
    ob_horuss sweat bashful "horuss_sweat_bashful"
    ob_horuss sweat grin "horuss_sweat_grin"
    ob_horuss sweat idle "horuss_sweat_idle"
    ob_horuss sweat talk "horuss_sweat_talk"
    hide ob_horuss

    show ob_kanaya2 idle
    ob_kanaya2 bored "kanaya2_bored"
    ob_kanaya2 cry "kanaya2_cry"
    ob_kanaya2 facepalm "kanaya2_facepalm"
    ob_kanaya2 happy "kanaya2_happy"
    ob_kanaya2 happytalk "kanaya2_happytalk"
    ob_kanaya2 idle "kanaya2_idle"
    ob_kanaya2 smirklaugh "kanaya2_smirklaugh"
    ob_kanaya2 smirktalk "kanaya2_smirktalk"
    ob_kanaya2 talk "kanaya2_talk"
    hide ob_kanaya2

    show ob_rufioh idle
    ob_rufioh happy "rufioh_happy"
    ob_rufioh happytalk "rufioh_happytalk"
    ob_rufioh idle "rufioh_idle"
    ob_rufioh laugh "rufioh_laugh"
    ob_rufioh no "rufioh_no"
    ob_rufioh notalk "rufioh_notalk"
    ob_rufioh offended "rufioh_offended"
    ob_rufioh offendedtalk "rufioh_offendedtalk"
    ob_rufioh sad "rufioh_sad"
    ob_rufioh sadtalk "rufioh_sadtalk"
    ob_rufioh sheepish "rufioh_sheepish"
    ob_rufioh surprise "rufioh_surprise"
    ob_rufioh surprisetalk "rufioh_surprisetalk"
    ob_rufioh talk "rufioh_talk"
    hide ob_rufioh

