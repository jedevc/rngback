from .generator import main 

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='geometic-background',
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

    args = parser.parse_args()

    main(args.width, args.height, args.columns, args.rows, args.offset,
              args.background, args.foreground, args.variation)
