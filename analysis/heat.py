from api import cache_interface as ci
from utils import country
import numpy as np
from analysis import color
import json

factor = 1.15


def heat_index(loc, n):
    data = ci.read(loc)

    data = data[-n-1:-1]
    hif_n = 0
    for daily in data:
        hif = 0
        for hourly in daily['hourly']:
            a = hourly['HeatIndexF']
            if int(a) > hif:
                hif = int(a)
        hif_n += hif
    return np.round(hif_n * factor / n, 1)


def save():
    countries = ci.get_available_countries()
    res = []
    for coun in countries:
        hi = heat_index(coun, 30)
        d = dict()
        d['country'] = country.get_code(coun)
        d['color'] = colormap(hi)
        d['info'] = str(hi)
        res.append(d)
        print(coun)
    with open('saved/heat_geo.json', 'w+') as f:
        json.dump(res, f, indent=4)


def get_geography():
    with open('saved/heat_geo.json', 'r') as f:
        res = json.load(f)
    return res


def get_bubbles():
    return []


def colormap(hi):
    a = 0.5 * np.tanh((hi - 75) * 0.03) + 0.5
    color1 = [230, 101, 91]
    color2 = [85, 158, 230]
    c = color.interpol(color2, color1, a)
    return color.toRGB(*c)
