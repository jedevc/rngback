import argparse

from PIL import Image, ImageDraw
import random

from . import util
from .color import parse_color

def main():
    '''
    Simple wrapper for the generate() function that parses command line
    arguments.
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

    generate(args.width, args.height, args.columns, args.rows, args.offset,
              args.background, args.foreground, args.variation, args.output)

def generate(width, height, columns, rows,
             offset, background, foreground, variation,
             output = None):
    '''
    Generates a random background image.

    Args:
        width: The image width.
        height: The image height.
        columns: The number of shapes to fit along the x-axis.
        rows: The number of shapes to fit along the y-axis.
        offset: The internal offset of each shape.
        background: The colors of the image's background.
        foreground: The color of the shapes in the image.
        variation: The amount to vary the color of the shapes.
        output: The output file. Default is to display the image on-screen.
    '''


    cwidth, rheight = width / columns, height / rows

    background = parse_color(background)
    foreground = [parse_color(fg) for fg in foreground]

    img = Image.new('RGB', (width, height), background)

    drw = ImageDraw.Draw(img, 'RGBA')
    for i in range(columns):
        for j in range(rows):
            poly = make_shape(i * cwidth + offset,
                              j * rheight + offset,
                              cwidth - offset * 2,
                              rheight - offset * 2)
            color = make_color(random.choice(foreground), variation)
            drw.polygon(poly, fill=color)

    if output:
        img.save(output)
    else:
        img.show()

def make_shape(*args):
    '''
    Generate the vertices of a randomly chosen shape (rectangle or triangle).

    Args: (see make_rect)

    Returns:
        A list of the vertices of the shape.
    '''

    choice = random.randint(0, 4)
    if choice == 0:
        return make_rect(*args)
    else:
        return make_triangle(*args)

def make_rect(x, y, width, height):
    '''
    Generate the vertices of a rectangle.

    Args:
        x: The x-coordinate of the top-left corner of the rectangle.
        y: The y-coordinate of the top-left corner of the rectangle.
        width: The width of the rectangle.
        height: The height of the rectangle.

    Returns:
        A list of the vertices of the rectangle.
    '''

    points = [(x, y),
              (x + width, y),
              (x + width, y + height),
              (x, y + height)]
    return points

def make_triangle(*args):
    '''
    Generate the the vertices a randomly-oriented triangle.

    Args: (see make_rect)

    Returns:
        A list of the vertices of the triangle.
    '''

    points = make_rect(*args)
    points.remove(random.choice(points))
    return points

def make_color(rgb, variation):
    '''
    Using a base color, generate another random color with the provided
    variation.

    Args:
        rgb: The base color as an RGB tuple.
        variation: The maximum amount to vary the color by.

    Returns:
        The altered color as an RGB tuple.
    '''

    red, green, blue = rgb
    lower, upper = -variation / 2, variation / 2

    red += random.randint(lower, upper)
    red = util.clamp(red, 0, 255)

    blue += random.randint(lower, upper)
    blue = util.clamp(blue, 0, 255)

    green += random.randint(lower, upper)
    green = util.clamp(green, 0, 255)

    return (red, green, blue)
