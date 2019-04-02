from .rect import Rectangle


class RightTriangle(Rectangle):
    def __init__(self, x, y, width, height, orientation):
        super().__init__(x, y, width, height)

        self.orientation = orientation

    def render(self, draw):
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.width
        y2 = self.y + self.height
        points = [(x1, y1),
                  (x2, y1),
                  (x2, y2),
                  (x1, y2)]
        del points[self.orientation % 4]

        if self.color:
            draw.polygon(points, fill=self.color)
        else:
            draw.polygon(points)
