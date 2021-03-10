from cryptography.fernet import Fernet
from datetime import datetime
from random import randint
from PIL import Image

def color_bounds(colour, bound):
    upper_bounds = []
    lower_bounds = []
    for value in colour:
        upper = value + bound
        lower = value - bound
        while upper > 255:
            upper -= 1
        while lower < 0:
            lower += 1
        upper_bounds.append(upper)
        lower_bounds.append(lower)
    upper_bounds = tuple(upper_bounds)
    lower_bounds = tuple(lower_bounds)

    return (upper_bounds, lower_bounds)

def rcolour():
    r = randint(50, 205)
    g = randint(50, 205)
    b = randint(50, 205)
    return (r, g, b)

def colourscheme(bounds):
    middle = rcolour()
    return color_bounds(middle, bounds)

def getstates(y, colours, pixels):
    states = [0] * EXTRA
    for x in range(WIDTH):
        states.append(colours.index(pixels[x, y]))
    return states + [1] * EXTRA

def genrule(text):
    rule = []
    for char in text:
        chars = bin(char)[2:]
        while len(chars) < 3:
            chars = "0" + chars
        rule += [int(char) for char in chars]
    return rule

def checkrule(x, rule, states):
    value = ""
    for i in range(LENGTH):
        value += str(states[x + i])
    value = int(value)
    for i in range(len(RULES)):
        if value == RULES[i]:
            while i >= len(rule): i -= len(rule)
            return rule[i]

HEIGHT = 800
WIDTH = 400
CLASS = 3
LENGTH = CLASS * 2
EXTRA = round(LENGTH / 2)
STATES = [0] * (WIDTH + LENGTH)

RULES = []
for i in range(2**LENGTH-1, -1, -1):
    RULES.append(int(bin(i)[2:]))

def gen(name, text):

    if not text:
        text = Fernet.generate_key()

    #text = b"3SOfiET56SPDi_aqPEIIDM0-lPuMq-Nhp6GDW091k5A="
    #text = b"fcKHK2fLsegGAqLrpa7JZouTtd59EghKffZZuBdwJVg="
    #text = b"vaM7ELMyAyfWkD8mxwTrdg5iRT3xhLYWVSgCP9BSkBo="
    #text = b"IuxhNWOw-KRfLSMMweQxngcSfutFDbBV77-7AHPtXOU="
    
    states = STATES
    rule = genrule(text)
    #colours = [(0,0,0), (255,255,255)]
    #colours = [(255,3,3), (255,153,153)]
    colours = colourscheme(80)

    start = datetime.now()
    img = Image.new("RGB", (WIDTH, HEIGHT), color=(0,0,0))
    pixels = img.load()

    for y in range(HEIGHT):
        for x in range(WIDTH):
            pixels[x, y] = colours[checkrule(x, rule, states)]
        states = getstates(y, colours, pixels)

    img.crop((0, 400, 400, 800)).save(f"{name}.png")

    return str(text)[2:-1]
