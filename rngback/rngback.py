import argparse

from . import generator
from .builder import Builder


def main():
    '''
    Simple wrapper for the generator that parses command line arguments.
    '''

    name = 'rngback'
    description = 'Randomly generate visually pleasing backgrounds.'
    parser = argparse.ArgumentParser(prog=name, description=description)

    styles = {
        'original': generator.OriginalGenerator,
        'triangles': generator.TriangleGenerator
    }
    parser.add_argument('style', choices=styles.keys(),
                        help='style of background to create')

    size = parser.add_argument_group('size')
    size.add_argument('size', type=int, help='size of shape')
    size.add_argument('rows', type=int, help='number of rows')
    size.add_argument('columns', type=int, help='number of columns')
    size.add_argument('--width', type=int, help='override width of image')
    size.add_argument('--height', type=int, help='override height of image')

    generation = parser.add_argument_group('generation')
    generation.add_argument('-s', '--seed', help='random generation seed')
    generation.add_argument('-o', '--output', default='', help='output file')

    colors = parser.add_argument_group('colors')
    colors.add_argument('-bg', '--background', default='white',
                        help='background color')
    colors.add_argument('-fg', '--foreground', action='append',
                        help='foreground color')

    variation = parser.add_argument_group('variation')
    variation.add_argument('-var', '--variation', default=0, type=int,
                           help='foreground variation amount (deprecated)')
    variation.add_argument('-hvar', '--hue-variation', default=0, type=int,
                           help='foreground hue variation amount')
    variation.add_argument('-svar', '--sat-variation', default=0, type=int,
                           help='foreground saturation variation amount')
    variation.add_argument('-lvar', '--lit-variation', default=0, type=int,
                           help='foreground lightness variation amount')

    visual = parser.add_argument_group('visual')
    visual.add_argument('--noblanks', action='store_true',
                        help='disable blank generation')
    visual.add_argument('-sc', '--scale', default=1, type=float,
                        help='individual shape scale')

    # additional argument processing
    args = parser.parse_args()
    if args.foreground is None:
        args.foreground = 'black'
    if args.variation and not args.hue_variation:
        args.hue_variation = args.variation

    variation = (args.hue_variation, args.sat_variation, args.lit_variation)

    style = styles[args.style]

    # create builder
    gen = style(args.rows, args.columns,
                args.size,
                args.scale, not args.noblanks)
    builder = Builder(gen, args.width, args.height,
                      args.background, args.foreground,
                      variation)

    # generate background
    img = builder.build(args.seed)
    if args.output:
        img.save(args.output)
    else:
        img.show()
