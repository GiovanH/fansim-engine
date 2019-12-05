label {{package_entrypoint}}_route:
    $ renpy.block_rollback()
    $ main_menu = False
    show image "gui/game_menu.png"
    window hide
    scene black with Dissolve(1.0)
    show blackcover
    $ quick_menu = True
    scene bg black

    $ debug_dump_character(dogja)
    $ debug_dump_character(ja)
