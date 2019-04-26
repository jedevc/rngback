import math
import random

from .. import shape


class TriangleGenerator:
    def __init__(self, width, height, size, scale=1, blanks=True):
        self.width = width
        self.height = height
        self.size = size
        self.hsize = size * math.sqrt(3) / 2
        self.columns = width // self.size + 1
        self.rows = height // int(self.hsize) + 1

        print(self.hsize)
        print(self.rows)
        self.scale = scale

        self.blanks = blanks

    def generate(self, seed=None):
        if seed:
            random.seed(seed)
        else:
            random.seed()

        direction = True
        for j in range(self.rows):
            for i in range(-1, self.columns * 2 + 1):
                shape = self.make_shape(i / 2, j, direction)
                direction = not direction
                shape.scale(self.scale)
                yield shape

    def make_shape(self, x, y, direction):
        if self.blanks and random.randint(0, 5) == 0:
            return shape.Blank()
        else:
            return shape.IsoscelesTriangle(x * self.size + (self.width - self.columns * self.size) / 2,
                                           y * self.hsize + (self.height - self.rows * self.hsize) / 2,
                                           self.size,
                                           self.hsize,
                                           direction)
