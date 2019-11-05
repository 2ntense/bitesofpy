"""Color class

The following sites were consulted:
    http://www.99colors.net/
    https://www.webucator.com/blog/2015/03/python-color-constants-module/
"""
import os
import string
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
        try:
            self.rgb = COLOR_NAMES[color.upper()]
        except KeyError:
            self.rgb = None

    @classmethod
    def hex2rgb(cls, hex):
        """Class method that converts a hex value into an rgb one"""
        if not isinstance(hex, str) or len(hex) != 7:
            raise ValueError

        if not hex.startswith("#"):
            raise ValueError

        for c in hex[1:]:
            if c not in string.hexdigits:
                raise ValueError

        def spl(s: str) -> list:
            return [s[i] + s[i + 1] for i in range(0, len(s), 2)]

        s = spl(hex[1:])

        return int(s[0], 16), int(s[1], 16), int(s[2], 16)

    @classmethod
    def rgb2hex(cls, rgb):
        """Class method that converts an rgb value into a hex one"""
        if not isinstance(rgb, tuple) or len(rgb) != 3:
            raise ValueError

        for c in rgb:
            if not isinstance(c, int) or not 0 <= c <= 255:
                raise ValueError

        return "#" + "".join([hex(c)[2:] if len(hex(c)[2:]) == 2 else "0" + hex(c)[2:] for c in rgb])

    def __repr__(self):
        """Returns the repl of the object"""
        for k, v in COLOR_NAMES.items():
            if v == self.rgb:
                return f"{__class__.__name__}('{k.lower()}')"
        return ""

    def __str__(self):
        """Returns the string value of the color object"""
        if self.rgb is None:
            return "Unknown"
        return f"({self.rgb[0]}, {self.rgb[1]}, {self.rgb[2]})"
