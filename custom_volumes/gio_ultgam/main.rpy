init offset = 2

# Define characters

# Just reminders:

# define gam

# image gamzee neutral1
# image gamzee neutral2
# image gamzee neutral3
# image gamzee neutral4
# image gamzee pie1
# image gamzee pie2
# image gamzee silhouette
# image gamzee sober1
# image gamzee sober2
# image gamzee surprised
# image gamzee talk1
# image gamzee talk2
# image gamzee talk3
# image gamzee talk4
# image gamzee think

# image gamzee2 neutral1

# image bg gamzeehive
# image bg gamzeecracked
# image bg gamzeebeach

# image victory gamzee
# image gameover gamzee1
# image gameover gamzee2

# transform staregrin
# transform gamzeewindowthrow
# transform fadetosilhouette
# transform thumpthumpthump
# transform highanim1
# transform highanim2
# transform clownanim1
# transform clownanim2
# transform clownanim3

# Define other graphics, end cards
image {{package_id}}_endcard = "{{assets}}/gamzee_endcard_goodend.png"

# Start of route
label __package_entrypoint___gio_ultgamv:

    # Menu boilerplate: Exit main menu, fade to black
    $ renpy.block_rollback()
    $ main_menu = False
    show image "gui/game_menu.png"
    window hide
    scene black with Dissolve(1.5)
    show blackcover
    $ quick_menu = True

    # Set the scene, fade in from black
    scene bg gamzeehive
    show gamzee neutral1
    play music "music/miracles.mp3" loop
    hide blackcover with dissolve

    # You can also use assets that have already been definied in other pesterquest routes directly!
    show bg gamzeehive

    show gamzee surprised at lazybounce


    gam think "yOu KnOw, I gOt To ThInKiNg AbOuT mIrAcLeS"
    gam neutral2 "My WiCkEd SiS... tWiStEd BrO? sHiT, mAn, I dOn'T kNoW wHaT yOu MoThErFuCkIn’ ArE"

    show gamzee neutral1

    # "Hey, you barely know what you are either! You laugh, trying to ease some possible misogy{nw}"
    # $ _history_list.pop()
    # "Hey, you barely know what you are either! You laugh, trying to ease some possibly{fast} insensitive overtones, but this dude doesn't notice. Wow, he is out of it."

    "Hey, you barely know what you are either! You laugh, trying to ease some possibly insensitive overtones, but this dude doesn't notice. Wow, he is out of it."

    show gamzee think
    gam "wHaT If sOmE MiRaClEs aRe mEaNt fOr yOu"
    gam "wHaT If mY MiRaClEs"
    gam talk4 "mY PiEs"
    gam neutral3 "tHe vOiCeS"
    gam talk1 "HoW YoU CaN CrOsS YoUr eYeS AnD SeE A ThIrD ThUmB JuSt mOtHeRfUcKiN’ fLoAtInG ThErE WhErE It gOt nO BuSiNeSs tO"
    gam neutral2"ThEy'Re jUsT FoR YoU"

    gam "aNd tHaT'S WhY YoU WaNnA ShArE ThEm, y'KnOw"
    gam talk1 "yOu wAnNa sHoW A NiNjA ThE MaGiC In tHe wOrLd"
    gam talk2 "tHe lItTlE MoThErFuCkInG DeLiGhTs oF JuSt lIvInG"

    gam talk4 "lIkE My bRo kArKaT"
    gam neutral3 "I LoVe tHe dUdE BuT NoNe oF ThIs dOeS It fOr hIm"
    gam talk2 "bUt lIkE"
    gam "He'S HiS OwN WhOlE BuNdLe oF MiRaClEs"
    gam neutral2 "hE'S GoT HiS WhOlE ThInG GoInG FoR HiM. bEiNg lOuD? hAhA, tHaT DuDe"

    show gamzee neutral1 at lazybounce

    "He collapses back and lands on a horn, which has the effect of punctuating his inane thought with a little{nw}"
    play sound "<from 1.75>music/honk_1.wav"
    "He collapses back and lands on a horn, which has the effect of punctuating his inane thought with a little{fast} \"honk\""

    gam neutral2 "nOt aLl mIrAcLeS ArE ThE SaMe aNyWaY"
    gam surprised "ThAt tHuMb tHiNg? lIkE HoLy sHiT DuDe"
    gam talk1 "sOmEbOdY ToLd mE OnCe tHaT LiKe"
    gam "wHaT If wHeN YoU SeE ReD, aNd wHeN I SeE ReD, iT LoOkS DiFfErEnT, bUt wE DoN'T KnOw?"
    gam "wE NeVeR GeT To sEe hOw aLl tHe lItTlE MiRaClEs hApPeN Up iN PeOpLeS HeAdS"

    "You nod along. This all sounds terribly important, if a bit high-concept for you. Your thing is mostly friendship, but you're on board for learning some philosophy from a thrice-baked stonerclown if that keeps you headed toward that sweet pavlovian victory jingle."

    gam "aNd sOmEtImEs yOu gOtTa jUsT Go hOlY ShIt, tWo cAkEs"
    gam "oR PiEs, mAn"
    gam "i jUsT MaKe mY OwN MoThErFuCkInG PiEs nOw"
    gam "mAyBe tHaT'S ThE MoRaL"
    gam "ThAt'S ThE PoT Of gOlD At tHe eNd oF ThE MoThErFuCkInG StOrY RaInBoW. tHe pOt o' cAnDy. tHe pOt pIe. "
    gam "LiKe tHaT ThUmB ThInG'S A MiRaClE I BaKeD MySeLf"
    gam "YoU GoT To sEe a rAiNbOw aNd nOw iT'S TiMe tO BaKe pIeS"

    # Show end card
    call ending pass ("{{package_id}}_endcard", True, True)
    return
