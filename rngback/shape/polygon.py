from .shape import Shape


class Polygon(Shape):
    def __init__(self, points):
        super().__init__()

        self.points = points

    def render(self, draw):
        if self.color:
            draw.polygon(self.points, fill=self.color)
        else:
            draw.polygon(self.points)
