from .shape import Shape


class RightTriangle(Shape):
    def __init__(self, x, y, width, height, orientation):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.orientation = orientation

        x1 = self.x
        y1 = self.y
        x2 = self.x + self.width
        y2 = self.y + self.height
        self.points = [(x1, y1),
                       (x2, y1),
                       (x2, y2),
                       (x1, y2)]

        del self.points[orientation % 4]

    def render(self, draw):
        if self.color:
            draw.polygon(self.points, fill=self.color)
        else:
            draw.polygon(self.points)
