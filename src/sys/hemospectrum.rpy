python:
    """
    Hemospectrum tools

    These allow you to automatically manage blood coloring
    and textboxes.

    Examples:

    define __p__.vr = Character(
        name="arachnidsGrip", kind=trollian, 
        show_blood="cerulean", image="vriska")
    define __p__.bo = Character(
        name="BOLDIR", kind=hiveswap, 
        image="boldir", show_blood="olive")

    You can use _hemospectrum["colorname"] = {"hex": "#000000"} in your code
    to define new blood colors. 

    The predefined FSE templates (trolian, hiveswap, openbound, etc)
    use show_blood to color the textbox and dialogue.

    hemospectrum(color) where color is the name of a blood color
    returns the hexadecimal color code for that color.

    doTint(displayable, color, cap) where color is the name of a blood color
    will tint all channels of a displayable (the color white) to the blood color given.
    This is how textboxes are colored.

    hex_to_rgb may be useful to advanced users, and is publicly exposed.
    """


init offset = 0

# Blood helper

init python:
    _hemospectrum = {
        'gray': "#646464",
        'candyred': "#FF0000",
        'test': "#f00",
        'burgandy': '#a20000',
        'bronze': '#bb6405',
        'gold': '#a1a100',
        'lime': '#84A224',
        'olive': '#416600',
        'jade': '#008342',
        'teal': '#008282',
        'cerulean': '#005682',
        'indigo': '#0021cb',
        'purple': '#2b0057',
        'violet': '#6a006a',
        'fuchsia': '#77003c',
    }
    hemoalias = {
        "grey": "gray",  # i HATE
        "rust": "burgandy",
        "blue": "indigo",
        "cobalt": "cerulean"
    }

    def hex_to_rgb(hex):
        hex = hex.lstrip('#')
        if len(hex) == 3:
            hex = "".join(c + c for c in hex)
        hlen = len(hex)
        return tuple(
            int(hex[i:i+hlen/3], 16)
            for i in range(0, hlen, hlen/3)
        )
    
    def hemospectrum(color):
        if color[0] == "#":
            return color
        try:
            return _hemospectrum[color]
        except KeyError:
            return _hemospectrum[hemoalias[color]]

    def doTint(displayable, hex, cap=255):
        """Tints a white displayable to the color given, where cap controls the intensity of the color
        This is used to create blood and text color based graphics and effects.
        
        example: doTint(displayable, "#AA0000", 200) will map the color white with an intensity of 200 to AA0000, with other colors being adjusted proportionately.
        """
        return im.MatrixColor(
                displayable,
                im.matrix.tint(
                    *map(lambda c: c/float(cap), hex_to_rgb(hex))
                )
            )

