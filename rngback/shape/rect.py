from .shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, draw):
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.width
        y2 = self.y + self.height
        points = [(x1, y1),
                  (x2, y1),
                  (x2, y2),
                  (x1, y2)]

        if self.color:
            draw.polygon(points, fill=self.color)
        else:
            draw.polygon(points)


class Square(Rectangle):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
