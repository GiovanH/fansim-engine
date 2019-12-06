init offset 1

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

