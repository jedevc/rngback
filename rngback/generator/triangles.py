import math
import random

from .. import shape


class TriangleGenerator:
    def __init__(self, rows, columns, size, scale=1, blanks=True):
        self.shape_width = size
        self.shape_height = size * math.sqrt(3) / 2
        self.columns = columns
        self.rows = rows

        self.scale = scale

        self.blanks = blanks

    @property
    def width(self):
        return int(self.shape_width * self.columns)

    @property
    def height(self):
        return int(self.shape_height * self.rows)

    def generate(self, seed=None):
        if seed:
            random.seed(seed)
        else:
            random.seed()

        direction = True
        for j in range(self.rows):
            for i in range(-1, self.columns * 2 + 1):
                shape = self._make_shape(i / 2, j, direction)
                direction = not direction
                shape.scale(self.scale)
                yield shape

    def _make_shape(self, x, y, direction):
        if self.blanks and random.randint(0, 5) == 0:
            return shape.Blank()
        else:
            return shape.IsoscelesTriangle(x * self.shape_width,
                                           y * self.shape_height,
                                           self.shape_width,
                                           self.shape_height,
                                           direction)
