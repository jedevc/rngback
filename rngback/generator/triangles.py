import math
import random

from .. import shape


class TriangleGenerator:
    def __init__(self, width, height, columns, rows, scale=1, blanks=True):
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.cwidth = width / columns
        # self.rheight = height / rows
        self.rheight = self.cwidth * math.sqrt(3) / 2

        self.scale = scale

        self.blanks = blanks

    def generate(self, seed=None):
        if seed:
            random.seed(seed)
        else:
            random.seed()

        direction = True
        for j in range(self.rows):
            for i in range(-1, self.columns * 2):
                shape = self.make_shape(i / 2, j, direction)
                direction = not direction
                shape.scale(self.scale)
                yield shape

    def make_shape(self, x, y, direction):
        if self.blanks and random.randint(0, 5) == 0:
            return shape.Blank()
        else:
            return shape.IsoscelesTriangle(x * self.cwidth,
                                           y * self.rheight,
                                           self.cwidth,
                                           self.rheight,
                                           direction)
