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

    You can use HemospectrumStore["colorname"] = {"hex": "#000000"} in your code
    to define new blood colors. 

    The predefined FSE templates (trolian, hiveswap, openbound, etc)
    use show_blood to color the textbox and dialogue.

    hemospectrum(color) where color is the name of a blood color
    returns the hexadecimal color code for that color.

    doTint(displayable, color, cap) where color is the name of a blood color
    will tint all channels of a displayable (the color white) to the blood color given.
    This is how textboxes are colored.
    """


init offset = 0

# Blood helper

init python:
    HemospectrumStore = {
        'gray': "#646464",
        'candyred': "#FF0000",
        'test': "#f00",
        'burgundy': '#a20000',
        'burgundy_fs': '#6f210e',
        'bronze': '#bb6405',
        'bronze_fs': '#a25200',
        'gold': '#a1a100',
        'lime': '#84A224',
        'olive': '#416600',
        'jade': '#008342',
        'teal': '#008282',
        'cerulean': '#005682',
        'indigo': '#0021CB',
        'indigo_fs': '#000058',
        'purple': '#2b0057',
        'violet': '#6a006a',
        'fuchsia': '#77003c',
    }
    hemoalias = {
        "grey": "gray",  # i HATE
        "rust": "burgundy",
        "blue": "indigo",
        "cobalt": "cerulean"
    }
    
    def hemospectrum(color):
        """Returns the hexadecimal color code for the color passed.
        If color is a hexadecimal color code, it is returned unmodified.
        Otherwise, if the color is the name of a blood hue registered in 
        HemospectrumStore, that color code is returned.
        """
        if color[0] == "#":
            return color
        try:
            return HemospectrumStore[color]
        except KeyError:
            return HemospectrumStore[hemoalias[color]]

    def doTint(displayable, hex, cap=255):
        """Returns a tinted version of the displayable.
        Tints a white displayable to the color given, where cap controls the intensity of the color
        This is used to create blood and text color based graphics and effects.
        
        example: doTint(displayable, "#AA0000", 200) will map the color white with an intensity of 200 to AA0000, with other colors being adjusted proportionately.
        """
        return im.MatrixColor(
                displayable,
                im.matrix.tint(
                    *map(lambda c: c/float(cap), hex_to_rgb(hex))
                )
            )

