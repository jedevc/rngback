import math
import random
import colorsys
from PIL import ImageColor

from . import util


class GradientColor:
    def __init__(self, foreground, background, variation):
        self.fgcolors = util.parse_colors(foreground)
        self.bgcolor = util.parse_color(background)

        self.points = []

        try:
            self.hvariation, self.svariation, self.lvariation = variation
        except TypeError:
            self.hvariation = self.svariation = self.lvariation = variation

    def setup(self, width, height):
        for i in range(len(self.fgcolors)):
            x = random.randint(0, width)
            y = random.randint(0, height)
            self.points.append((x, y))

    def foreground(self, shape):
        center = shape.center()

        dists = []
        for point in self.points:
            xdiff = center[0] - point[0]
            ydiff = center[1] - point[1]
            dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
            dists.append(dist)
        total = sum(dists)

        # this is not quite right
        scales = [dist / total for dist in dists]

        hue = lit = sat = 0
        for color, scale in zip(self.fgcolors, scales):
            dh, dl, ds = colorsys.rgb_to_hls(color[0] / 255,
                                             color[1] / 255,
                                             color[2] / 255)
            hue += scale * dh
            lit += scale * dl
            sat += scale * ds

        return self._vary(hue, sat, lit)

    def _vary(self, hue, sat, lit):
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
