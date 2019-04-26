from PIL import ImageColor

import random


def parse_color(color):
    '''
    Parse a color string.

    This works very similarly to PIL's ImageColor.getrgb function, however, it
    also generates random colors.

    Args:
        color: An ImageColor string. The string is passed to randomizer()
            before being parsed.

    Returns:
        An RGB color tuple.
    '''

    if type(color) == str:
        color = randomizer(color)
        return ImageColor.getrgb(color)
    else:
        return color


def parse_colors(colors):
    '''
    Parse multiple color strings.

    Args:
        colors: An iterable of colors to parse.

    Returns:
        RGB color tuples for every item in colors.
    '''

    if type(colors) == str:
        return [parse_color(colors)]
    else:
        return [parse_color(color) for color in colors]


def randomizer(string):
    '''
    Generate a random color using a template string.

    The templates are contained within '{}' parentheses and should contain two
    values seperated by a '-' dash. For example, '{0-10}' will be replaced with
    a number between 0 and 10.

    The generated result will be left padded with '0's to match the width of
    the first value. This can be very useful in ensuring creation of valid html
    color codes.

    If the template starts with a '#' hash, then the numbers inside will be
    interpreted as hexadecimal, and the output will be likewise formatted.

    Args:
        string: The color template.

    Returns:
        A randomly generated color string. Note that this string is not
        guaranteed to be valid.
    '''

    paren = string.find('{')
    while paren != -1:
        # find the matching parenthesis
        endparen = string.find('}', paren + 1)
        if endparen == -1:
            raise ValueError('expected closing parenthesis')

        # find the range endpoints
        numbers = string[paren + 1:endparen].split('-')
        if len(numbers) != 2:
            raise ValueError('expected two endpoints')
        start, end = numbers[0], numbers[1]

        if start.startswith('#'):
            # hexidecimal
            pad = len(start) - 1
            start, end = int(start[1:], 16), int(end, 16)
            value = random.randint(start, end)
            value = hex(value)[2:].zfill(pad)
        else:
            # regular decimal
            pad = len(start)
            start, end = int(start), int(end)
            value = random.randint(start, end)
            value = str(value).zfill(pad)

        # replace template with generated value
        string = string[:paren] + value + string[endparen + 1:]

        paren = string.find('{')

    return string
