from constants import earthquake_data
import numpy as np
from analysis import color

def get_bubbles():
    res = []
    for quake in earthquake_data.quakes:
        bubble = dict()
        bubble['name'] = 'quake {}'.format(quake['id'])
        bubble['longitude'] = float(quake['long'])
        bubble['latitude'] = float(quake['lat'])
        bubble['radius'] = calc_radius(float(quake['mag']))
        bubble['color'] = colormap(float(quake['mag']))
        bubble['info'] = 'depth: {}'.format(quake['depth'])
        res.append(bubble)
    return res


def calc_radius(mag):
    r0 = 120
    return r0 * np.log(mag / 6)


def colormap(mag):
    color1 = [255, 218, 0]
    color2 = [255, 0, 0]
    a = np.tanh(1 * (mag - 6))
    c = color.interpol(color1, color2, a)

    return color.toRGB(*c)