import random
import colorsys
from PIL import ImageColor

from . import util


class RandomColor:
    def __init__(self, foreground, background, variation):
        self.fgcolors = util.parse_colors(foreground)
        self.bgcolor = util.parse_color(background)

        try:
            self.hvariation, self.svariation, self.lvariation = variation
        except TypeError:
            self.hvariation = self.svariation = self.lvariation = variation

    def foreground(self, shape):
        red, green, blue = random.choice(self.fgcolors)
        hue, lit, sat = colorsys.rgb_to_hls(red / 255, green / 255, blue / 255)

        hue = int(hue * 360)
        hue += random.randint(-self.hvariation / 2, self.hvariation / 2)
        hue = max(0, min(hue, 360))

        sat = int(sat * 100)
        sat += random.randint(-self.svariation / 2, self.svariation / 2)
        sat = max(0, min(sat, 100))

        lit = int(lit * 100)
        lit += random.randint(-self.lvariation / 2, self.lvariation / 2)
        lit = max(0, min(lit, 100))

        return ImageColor.getrgb(f'hsl({hue}, {sat}%, {lit}%)')

    def background(self):
        return self.bgcolor
