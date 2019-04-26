from PIL import Image, ImageDraw

from . import color


class Builder:
    '''
    Builder for a random background image.

    Args:
        generator: The generator to use.
        width: The overriden image width
        height: The overriden image height
        background: The color of the image background.
        foreground: The colors of the shapes in the image.
        variation: The amount to vary the color of the shapes.
    '''

    def __init__(self, generator, width=None, height=None,
                 background='white', foreground='black', variation=0):
        self.generator = generator

        self.width = width or generator.width
        self.height = height or generator.height

        self.colors = color.RandomColor(foreground, background, variation)

    def build(self, seed=None):
        '''
        Build an image.

        Args:
            seed: The initial internal state of the random generator.

        Returns:
            The image.
        '''

        img = Image.new('RGB',
                        (self.width, self.height),
                        self.colors.background())
        drw = ImageDraw.Draw(img, 'RGBA')
        for shape in self.generator.generate(seed):
            shape.translate((self.width - self.generator.width) / 2,
                            (self.height - self.generator.height) / 2)
            shape.color = self.colors.foreground(shape)
            shape.render(drw)

        return img
