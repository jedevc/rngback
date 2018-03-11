import argparse

from PIL import Image, ImageDraw, ImageColor
import random

from . import util

def main(*args):
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
    parser.add_argument('-fg', '--foreground', default='black',
              help='foreground color')
    parser.add_argument('-var', '--variation', default=0, type=int,
              help='foreground color variation amount')

    parser.add_argument('-o', '--output', default='', help='output file')

    args = parser.parse_args()

    generate(args.width, args.height, args.columns, args.rows, args.offset,
              args.background, args.foreground, args.variation, args.output)

def generate(width, height, columns, rows,
             offset, background, foreground, variation,
             output = None):

    cwidth, rheight = width / columns, height / rows

    foreground = ImageColor.getrgb(foreground)
    background = ImageColor.getrgb(background)

    img = Image.new('RGB', (width, height), background)

    drw = ImageDraw.Draw(img, 'RGBA')
    for i in range(columns):
        for j in range(rows):
            poly = make_shape(i * cwidth + offset,
                              j * rheight + offset,
                              cwidth - offset * 2,
                              rheight - offset * 2)
            color = make_color(foreground, variation)
            drw.polygon(poly, fill=color)

    if output:
        img.save(output)
    else:
        img.show()

def make_shape(*args):
    choice = random.randint(0, 4)
    if choice == 0:
        return make_square(*args)
    else:
        return make_triangle(*args)

def make_square(x, y, width, height):
    points = [(x, y),
              (x + width, y),
              (x + width, y + height),
              (x, y + height)]
    return points

def make_triangle(x, y, width, height):
    points = make_square(x, y, width, height)
    points.remove(random.choice(points))
    return points

def make_color(rgb, variation):
    red, green, blue = rgb
    lower, upper = -variation / 2, variation / 2

    red += random.randint(lower, upper)
    red = util.clamp(red, 0, 255)

    blue += random.randint(lower, upper)
    blue = util.clamp(blue, 0, 255)

    green += random.randint(lower, upper)
    green = util.clamp(green, 0, 255)

    return (red, green, blue)
