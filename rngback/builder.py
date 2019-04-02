from PIL import Image, ImageDraw, ImageColor
import random
import colorsys

from . import color


class Builder:
    '''
    Builder for a random background image.

    Args:
        generator: The generator to use.
        background: The color of the image background.
        foreground: The colors of the shapes in the image.
        variation: The amount to vary the color of the shapes.
    '''

    def __init__(self, generator,
                 background='white', foreground='black', variation=0):
        self.generator = generator

        self.background = color.parse_color(background)
        self.foreground = color.parse_colors(foreground)

        try:
            self.hvariation, self.svariation, self.lvariation = variation
        except TypeError:
            self.hvariation = self.svariation = self.lvariation = variation

    def build(self, seed=None):
        '''
        Build an image.

        Args:
            seed: The initial internal state of the random generator.

        Returns:
            The image.
        '''

        img = Image.new('RGB',
                        (self.generator.width, self.generator.height),
                        self.background)
        drw = ImageDraw.Draw(img, 'RGBA')
        for shape in self.generator.generate(seed):
            shape.color = self.make_color()
            shape.render(drw)

        return img

    def make_color(self):
        '''
        Generate a random foreground color using the provided foreground colors
        and variation amounts.

        Returns:
            The altered color as an RGB tuple.
        '''

        red, green, blue = random.choice(self.foreground)
        hue, lit, sat = colorsys.rgb_to_hls(red / 255, green / 255, blue / 255)

        hue = int(hue * 360)
        hue += random.randint(-self.hvariation / 2, self.hvariation / 2)
        hue = max(0, min(hue, 360))

        sat = int(sat * 100)
        sat += random.randint(-self.svariation / 2, self.svariation / 2)
        sat = max(0, min(sat, 100))

        lit = int(lit * 100)
        lit += random.randint(-self.lvariation / 2, self.lvariation / 2)
        lit = max(0, min(lit, 100))

        return ImageColor.getrgb(f'hsl({hue}, {sat}%, {lit}%)')
