
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

    $ debug_dump_character(rb_squarewave)

    $ debug_dump_character(rb_dirk)

    $ debug_dump_character(ob_aradia)

    $ debug_dump_character(ob_meenah)

    $ debug_dump_character(ob_aranea)

    $ debug_dump_character(ob_dave)

    $ debug_dump_character(ob_kanaya)

    $ debug_dump_character(ob_rose)

    $ debug_dump_character(ob_kankri)

    $ debug_dump_character(ob_karkat)

    $ debug_dump_character(ob_latula)

    $ debug_dump_character(ob_porrim)

    $ debug_dump_character(ob_cronus)

    $ debug_dump_character(ob_kurloz)

    $ debug_dump_character(ob_meulin)

    $ debug_dump_character(ob_mituna)

    $ debug_dump_character(ob_terezi)

    $ debug_dump_character(ob_gamzee)

    $ debug_dump_character(ob_damara)

    $ debug_dump_character(ob_horuss)

    $ debug_dump_character(ob_kanaya2)

    $ debug_dump_character(ob_rufioh)

