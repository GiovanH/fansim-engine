init 800 python:
    for name, image in get_images_from_sayer(ja):
        newname = ("dogjade",) + name[1:]

        earkind = "default"
        if name[1] in ["clasp", "clasp2", "clasp3"]:
            earkind = "tinytilt"

        elif name[1]  == "smiley":
            earkind = "perk"

        elif name[1] == "gun":
            earkind = "gun"

        elif name[1] in ["augh", "feral"]:
            earkind = "augh"

        elif name[1] in ["grimace", "growl", "panic", "teary", "shriek"]:
            earkind = "rotate"
        elif name[1] == "cheering":
            earkind = "rotdroop"

        renpy.image(newname,
            Composite(
                (1280, 720), (0, 0), image,
                (0, 0), "{{assets}}/ears_" + earkind + ".png"
            )
        )


define dogja = Character(name="gardenGnostic", kind=pesterchum, what_color='#4ac925', image="dogjade")
