from constants import hospital_data
import numpy as np
from analysis import color


def get_geography():
    res = []
    for c in hospital_data.beds:
        d = dict()
        b = hospital_data.beds[c]
        d['country'] = c
        d['color'] = colormap(b)
        d['info'] = str(b)
        res.append(d)
    return res



def get_bubbles():
    return []


def colormap(u):
    a = np.tanh(u * 0.1)

    color1 = [113, 46, 27]
    color2 = [0, 255, 0]

    c = color.interpol(color1, color2, a)
    return color.toRGB(*c)