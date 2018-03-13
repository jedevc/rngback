from PIL import ImageColor

import random

def parse_color(color):
    if type(color) == str:
        if color in ['rand', 'random']:
            choice = random.choice(random_colors)
            return ImageColor.getrgb(choice)
        else:
            return ImageColor.getrgb(color)
    else:
       return color

random_colors=["Aqua", "Aquamarine", "Blue", "BlueViolet", "Brown",
        "BurlyWood", "CadetBlue", "Chartreuse", "Chocolate", "Coral",
        "CornflowerBlue", "Crimson", "Cyan", "DarkBlue", "DarkCyan",
        "DarkGoldenRod", "DarkGreen", "DarkKhaki", "DarkMagenta",
        "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon",
        "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGrey", "DarkTurquoise",
        "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGrey", "DodgerBlue",
        "FireBrick", "ForestGreen", "Fuchsia", "Gold", "GoldenRod", "Grey",
        "Green", "GreenYellow", "HotPink", "IndianRed", "Indigo", "Khaki",
        "LawnGreen", "LightBlue", "LightCoral", "LightGrey", "LightGreen",
        "LightPink", "LightSalmon", "LightSeaGreen", "LightSkyBlue",
        "LightSlateGrey", "LightSteelBlue", "Lime", "LimeGreen", "Magenta",
        "Maroon", "MediumAquaMarine", "MediumBlue", "MediumOrchid",
        "MediumPurple", "MediumSeaGreen", "MediumSlateBlue",
        "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed",
        "MidnightBlue", "Navy", "Olive", "OliveDrab", "Orange", "OrangeRed",
        "Orchid", "PaleGreen", "PaleTurquoise", "PaleVioletRed", "Peru",
        "Pink", "Plum", "PowderBlue", "Purple", "RebeccaPurple", "Red",
        "RosyBrown", "RoyalBlue", "SaddleBrown", "Salmon", "SandyBrown",
        "SeaGreen", "Sienna", "Silver", "SkyBlue", "SlateBlue", "SlateGray",
        "SlateGrey", "SpringGreen", "SteelBlue", "Tan", "Teal", "Thistle",
        "Tomato", "Turquoise", "Violet", "Wheat", "Yellow", "YellowGreen"]
