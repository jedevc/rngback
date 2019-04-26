import math
from .shape import Shape


class Polygon(Shape):
    def __init__(self, points):
        super().__init__()

        self.points = points

    def scale(self, factor):
        center = (0, 0)
        for point in self.points:
            center = (center[0] + point[0],
                      center[1] + point[1])
        center = (center[0] / len(self.points),
                  center[1] / len(self.points))

        npoints = []
        for point in self.points:
            xdiff = point[0] - center[0]
            ydiff = point[1] - center[1]
            dist = math.sqrt(xdiff ** 2 + ydiff ** 2)

            angle = math.atan2(ydiff, xdiff)

            npoint = (center[0] + math.cos(angle) * dist * factor,
                      center[1] + math.sin(angle) * dist * factor)
            npoints.append(npoint)

        self.points = npoints

    def render(self, draw):
        if self.color:
            draw.polygon(self.points, fill=self.color)
        else:
            draw.polygon(self.points)
