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

