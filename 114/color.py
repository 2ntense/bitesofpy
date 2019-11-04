"""Color class

The following sites were consulted:
    http://www.99colors.net/
    https://www.webucator.com/blog/2015/03/python-color-constants-module/
"""
import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
color_values_module = os.path.join('/tmp', 'color_values.py')
urllib.request.urlretrieve('https://bit.ly/2MSuu4z',
                           color_values_module)
sys.path.append('/tmp')

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.rgb = color
        pass

    @classmethod
    def hex2rgb(cls, hex):
        """Class method that converts a hex value into an rgb one"""
        if not isinstance(hex, str):
            raise TypeError
        if len(hex) != 7:
            raise ValueError

        def spl(s: str) -> list:
            return [s[i] + s[i + 1] for i in range(0, len(s), 2)]

        l = spl(hex[1:])

        return int(l[0], 16), int(l[1], 16), int(l[2], 16)


    @classmethod
    def rgb2hex(cls, rgb):
        """Class method that converts an rgb value into a hex one"""
        if not isinstance(rgb, tuple):
            raise TypeError
        if len(rgb) != 3:
            raise ValueError

        return "#" + "".join([hex(c)[2:] if len(hex(c)[2:]) == 2 else "0" + hex(c)[2:] for c in rgb])

    def __repr__(self):
        """Returns the repl of the object"""
        return f"{__class__.__name__}('{list(self.rgb)[0]}')"

    def __str__(self):
        """Returns the string value of the color object"""
        pass

c = Color({"ALICEBLUE": (240, 248, 255)})
print(c.hex2rgb("#ffffff"))