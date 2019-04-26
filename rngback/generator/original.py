import random

from .. import shape


class OriginalGenerator:
    def __init__(self, rows, columns, size, scale=1, blanks=True):
        self.size = size
        self.columns = columns
        self.rows = rows

        self.scale = scale

        self.blanks = blanks

    @property
    def width(self):
        return self.size * self.columns

    @property
    def height(self):
        return self.size * self.rows

    def generate(self, seed=None):
        if seed:
            random.seed(seed)
        else:
            random.seed()

        for i in range(self.columns):
            for j in range(self.rows):
                shape = self.make_shape(i, j)
                if shape:
                    yield shape

    def make_shape(self, x, y):
        if self.blanks:
            choice = random.randint(0, 6)
        else:
            choice = random.randint(1, 6)

        if choice == 0:
            return None
        elif choice in [1, 2]:
            sh = shape.Rectangle(x * self.size,
                                 y * self.size,
                                 self.size,
                                 self.size)
        else:
            sh = shape.RightTriangle(x * self.size,
                                     y * self.size,
                                     self.size,
                                     self.size,
                                     random.randint(0, 3))

        sh.scale(self.scale)
        return sh
