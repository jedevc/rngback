from PIL import ImageColor

import random

def parse_color(color):
    if type(color) == str:
        if color in ['rand', 'random']:
            choice = random_color(range(30, 90), range(40, 70))
            return ImageColor.getrgb(choice)
        else:
            return ImageColor.getrgb(color)
    else:
       return color

def random_color(satrange, lirange):
    hue = random.randint(0, 360)
    sat = random.randint(satrange.start, satrange.stop)
    li = random.randint(lirange.start, lirange.stop)

    return f'hsl({hue}, {sat}%, {li}%)'
