import argparse

from .generator import Generator

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

    parser.add_argument('-hvar', '--hue-variation', default=0, type=int,
              help='foreground hue variation amount')
    parser.add_argument('-svar', '--sat-variation', default=0, type=int,
              help='foreground saturation variation amount')
    parser.add_argument('-lvar', '--lit-variation', default=0, type=int,
              help='foreground lightness variation amount')

    parser.add_argument('-s', '--seed', help='random generation seed')

    parser.add_argument('-o', '--output', default='', help='output file')

    args = parser.parse_args()
    if args.foreground is None:
        args.foreground = 'black'

    variation = (args.hue_variation, args.sat_variation, args.lit_variation)

    gen = Generator(args.width, args.height, args.columns, args.rows,
            args.offset, args.background, args.foreground, variation)
    img = gen.generate(args.seed)

    if args.output:
        img.save(args.output)
    else:
        img.show()
