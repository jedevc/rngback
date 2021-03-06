import argparse

from .generator import Generator


def main():
    '''
    Simple wrapper for the generator that parses command line arguments.
    '''

    # create parser
    name = 'rngback'
    description = 'Randomly generate visually pleasing backgrounds.'
    parser = argparse.ArgumentParser(prog=name, description=description)

    # define arguments
    size = parser.add_argument_group('size')
    size.add_argument('width', type=int, help='image width')
    size.add_argument('height', type=int, help='image width')
    size.add_argument('columns', type=int, help='number of columns')
    size.add_argument('rows', type=int, help='number of rows')

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
    visual.add_argument('--noblanks', action="store_true",
                        help='disable blank generation')
    visual.add_argument('-off', '--offset', default=0, type=int,
                        help='individual shape offset')

    # parse arguments
    args = parser.parse_args()
    if args.foreground is None:
        args.foreground = 'black'
    if args.variation and not args.hue_variation:
        args.hue_variation = args.variation

    variation = (args.hue_variation, args.sat_variation, args.lit_variation)

    # generate background
    gen = Generator(args.width, args.height, args.columns, args.rows,
                    args.offset, args.background, args.foreground,
                    not args.noblanks, variation)
    img = gen.generate(args.seed)

    # save background
    if args.output:
        img.save(args.output)
    else:
        img.show()
