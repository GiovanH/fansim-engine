init offset = 0

# Blood helper

init python:
    _hemospectrum = {
        'gray': {
            "hex": "#646464"
        },
        'candyred': {
            "hex": "#FF0000"
        },
        'test': {
            "hex": "#f00"
        },
        'burgandy': {
            "hex": '#a20000'
        },
        'bronze': {
            "hex": '#bb6405'
        },
        'gold': {
            "hex": '#a1a100'
        },
        'lime': {
            "hex": '#84A224'
        },
        'olive': {
            "hex": '#416600'
        },
        'jade': {
            "hex": '#008342'
        },
        'teal': {
            "hex": '#008282'
        },
        'cerulean': {
            "hex": '#005682'
        },
        'indigo': {
            "hex": '#0021cb'
        },
        'purple': {
            "hex": '#2b0057'
        },
        'violet': {
            "hex": '#6a006a'
        },
        'fuchsia': {
            "hex": '#77003c'
        },
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

