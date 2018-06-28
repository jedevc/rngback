from PIL import Image, ImageDraw, ImageColor
import random
import colorsys

from . import color

class Generator:
    '''
    Generator for a random background image.

    Args:
        width: The image width.
        height: The image height.
        columns: The number of shapes to fit along the x-axis.
        rows: The number of shapes to fit along the y-axis.
        offset: The internal offset of each shape.
        background: The color of the image background.
        foreground: The colors of the shapes in the image.
        variation: The amount to vary the color of the shapes.
    '''

    def __init__(self, width, height, columns, rows,
            offset=0, background='white', foreground='black', variation=0):
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.cwidth = width / columns
        self.rheight = height / rows

        self.offset = offset

        self.background = color.parse_color(background)
        self.foreground = color.parse_colors(foreground)

        try:
            self.hvariation, self.svariation, self.lvariation = variation
        except TypeError:
            self.hvariation = self.svariation = self.lvariation = variation

    def generate(self, seed=None):
        '''
        Generate an image.

        Args:
            seed: The initial internal state of the random generator.

        Returns:
            The image.
        '''

        if seed:
            random.seed(seed)
        else:
            random.seed()

        img = Image.new('RGB', (self.width, self.height), self.background)
        drw = ImageDraw.Draw(img, 'RGBA')
        for i in range(self.columns):
            for j in range(self.rows):
                poly = self.make_shape(i, j)
                if poly:
                    color = self.make_color()
                    drw.polygon(poly, fill=color)

        return img

    def make_shape(self, *args):
        '''
        Generate the vertices of a randomly chosen shape (rectangle or triangle).

        Args: (see make_square)

        Returns:
            A list of the vertices of the shape or None for no shape.
        '''

        choice = random.randint(0, 6)
        if choice == 0:
            return None
        elif choice in [1, 2]:
            return self.make_square(*args)
        else:
            return self.make_triangle(*args)

    def make_square(self, x, y):
        '''
        Generate the vertices of a square.

        Args:
            x: The localized x-coordinate of the square to generate.
            y: The localized y-coordinate of the square to generate.

        Returns:
            A list of the vertices of the square.
        '''

        x1 = x * self.cwidth + self.offset
        y1 = y * self.rheight + self.offset
        x2 = (x + 1) * self.cwidth - self.offset
        y2 = (y + 1) * self.rheight - self.offset

        return [(x1, y1),
                (x2, y1),
                (x2, y2),
                (x1, y2)]

    def make_triangle(self, *args):
        '''
        Generate the the vertices a randomly-oriented triangle.

        Args: (see make_square)

        Returns:
            A list of the vertices of the triangle.
        '''

        points = self.make_square(*args)
        points.remove(random.choice(points))
        return points

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
