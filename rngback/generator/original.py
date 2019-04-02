import random

from .. import shape


class OriginalGenerator:
    def __init__(self, width, height, columns, rows, scale=1, blanks=True):
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.cwidth = width / columns
        self.rheight = height / rows

        self.scale = scale

        self.blanks = blanks

    def generate(self, seed=None):
        if seed:
            random.seed(seed)
        else:
            random.seed()

        for i in range(self.columns):
            for j in range(self.rows):
                shape = self.make_shape(i, j)
                shape.scale(self.scale)
                yield shape

    def make_shape(self, x, y):
        if self.blanks:
            choice = random.randint(0, 6)
        else:
            choice = random.randint(1, 6)

        if choice == 0:
            return shape.Blank()
        elif choice in [1, 2]:
            return shape.Rectangle(x * self.cwidth,
                                   y * self.rheight,
                                   self.cwidth,
                                   self.rheight)
        else:
            return shape.RightTriangle(x * self.cwidth,
                                       y * self.rheight,
                                       self.cwidth,
                                       self.rheight,
                                       random.randint(0, 3))
