from .shape import Shape


class Blank(Shape):
    def __init__(self):
        super().__init__(None, None)

    def render(self, draw):
        pass
