from .shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def center(self):
        return (self.x + self.width / 2,
                self.y + self.height / 2)

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def scale(self, factor):
        nwidth = self.width * factor
        nheight = self.height * factor
        self.x += (self.width - nwidth) / 2
        self.y += (self.height - nheight) / 2
        self.width = nwidth
        self.height = nheight

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
