from .shape import Shape


class Blank(Shape):
    def __init__(self):
        super().__init__()

    def render(self, draw):
        pass
