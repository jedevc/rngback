from PIL import ImageColor

import random

def parse_color(color):
    '''
    Parse a color string.

    This works very similarly to PIL's ImageColor.getrgb function, however, it
    also generates random colors.

    Args:
        color: A string taking one of the following values.
            - ImageColor.getrgb color string
            - "rand" / "random"

    Returns:
        An RGB color tuple.
    '''

    if type(color) == str:
        if color in ['rand', 'random']:
            choice = random_color(range(30, 90), range(40, 70))
            return ImageColor.getrgb(choice)
        else:
            return ImageColor.getrgb(color)
    else:
       return color

def random_color(satrange, lirange):
    '''
    Generate a random color.

    Args:
        satrange: A range of values to generate the saturation value from.
        lirange: A range of values to generate the light value from.

    Returns:
        A randomly generated color as an HSL string.
    '''

    hue = random.randint(0, 360)
    sat = random.randint(satrange.start, satrange.stop)
    li = random.randint(lirange.start, lirange.stop)

    return f'hsl({hue}, {sat}%, {li}%)'
