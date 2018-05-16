import argparse

from PIL import Image, ImageDraw
import random

from . import util
from .color import parse_color

def main():
    '''
    Simple wrapper for the generator that parses command line arguments.
    '''

    parser = argparse.ArgumentParser(prog='rngback',
              description='Randomly generate visually pleasing geometric backgrounds.')
    parser.add_argument('width', type=int, help='image width')
    parser.add_argument('height', type=int, help='image width')
    parser.add_argument('columns', type=int, help='number of columns')
    parser.add_argument('rows', type=int, help='number of rows')

    parser.add_argument('-off', '--offset', default=0, type=int,
              help='individual shape offset')

    parser.add_argument('-bg', '--background', default='white',
              help='background color')
    parser.add_argument('-fg', '--foreground', action='append',
              help='foreground color')
    parser.add_argument('-var', '--variation', default=0, type=int,
              help='foreground color variation amount')

    parser.add_argument('-o', '--output', default='', help='output file')

    args = parser.parse_args()
    if args.foreground is None:
        args.foreground = ['black']

    gen = Generator(args.width, args.height, args.columns, args.rows,
            args.offset, args.background, args.foreground, args.variation)
    gen.generate(args.output)

class Generator:
    '''
    Generator for a random background image.

    Args:
        width: The image width.
        height: The image height.
        columns: The number of shapes to fit along the x-axis.
        rows: The number of shapes to fit along the y-axis.
        offset: The internal offset of each shape.
        background: The colors of the image's background.
        foreground: The color of the shapes in the image.
        variation: The amount to vary the color of the shapes.
    '''

    def __init__(self, width, height, columns, rows,
            offset, background, foreground, variation):
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.cwidth = width / columns
        self.rheight = height / rows

        self.offset = offset

        self.background = parse_color(background)
        self.foreground = [parse_color(fg) for fg in foreground]

        self.variation = variation

    def generate(self, output = None):
        '''
        Generate an image.

        Args:
            output: The location to output the image to.

        Returns:
            The image.
        '''

        img = Image.new('RGB', (self.width, self.height), self.background)

        drw = ImageDraw.Draw(img, 'RGBA')
        for i in range(self.columns):
            for j in range(self.rows):
                poly = self.make_shape(i, j)
                color = self.make_color()
                drw.polygon(poly, fill=color)

        if output:
            img.save(output)
        else:
            img.show()

        return img

    def make_shape(self, *args):
        '''
        Generate the vertices of a randomly chosen shape (rectangle or triangle).

        Args: (see make_square)

        Returns:
            A list of the vertices of the shape.
        '''

        choice = random.randint(0, 4)
        if choice == 0:
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
        Using a base color, generate another random color with the provided
        variation.

        Args:
            rgb: The base color as an RGB tuple.
            variation: The maximum amount to vary the color by.

        Returns:
            The altered color as an RGB tuple.
        '''

        red, green, blue = random.choice(self.foreground)
        lower, upper = -self.variation / 2, self.variation / 2

        red += random.randint(lower, upper)
        red = util.clamp(red, 0, 255)

        blue += random.randint(lower, upper)
        blue = util.clamp(blue, 0, 255)

        green += random.randint(lower, upper)
        green = util.clamp(green, 0, 255)

        return (red, green, blue)
