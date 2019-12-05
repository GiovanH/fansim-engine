
label __package_entrypoint___route:
    # Menu boilerplate: Exit main menu, fade to black
    $ renpy.block_rollback()
    $ main_menu = False
    show image "gui/game_menu.png"
    window hide
    scene black with Dissolve(1.0)
    show blackcover
    $ quick_menu = True
    scene bg alternia4

    $ debug_dump_character(bronya)
    $ debug_dump_character(amisia)
    $ debug_dump_character(charun)
    $ debug_dump_character(mallek)
    $ debug_dump_character(remele)
    $ debug_dump_character(chixie)
    $ debug_dump_character(galekh)
    $ debug_dump_character(polypa)
    $ debug_dump_character(marvus)
    $ debug_dump_character(stelsa)
    $ debug_dump_character(barzum)
    $ debug_dump_character(nikhee)
    $ debug_dump_character(marsti)
    $ debug_dump_character(elwurd)
    $ debug_dump_character(folykl)
    $ debug_dump_character(azdaja)
    $ debug_dump_character(tagora)
    $ debug_dump_character(wanshi)
    $ debug_dump_character(tegiri)
    $ debug_dump_character(tyzias)
    $ debug_dump_character(zebruh)
    $ debug_dump_character(lanque)
    $ debug_dump_character(folyklkuprum)
    $ debug_dump_character(kuprum)
    $ debug_dump_character(lynera)
    $ debug_dump_character(karako)
    $ debug_dump_character(chahut)
    $ debug_dump_character(zebede)
    $ debug_dump_character(skylla)
    $ debug_dump_character(vikare)
    $ debug_dump_character(daraya)
    $ debug_dump_character(cirava)
    $ debug_dump_character(boldir)
    $ debug_dump_character(diemen)
    $ debug_dump_character(konyyl)
    $ debug_dump_character(fozzer)
    $ debug_dump_character(ardata)
    $ debug_dump_character(tirona)
    $ debug_dump_character(baizli)
    call ending pass ("gui/game_menu.png", True, True)
    return
