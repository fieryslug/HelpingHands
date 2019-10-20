from api import cache_interface as ci
from utils import country
import numpy as np
import json
from analysis import color

def save():
    countries = ci.get_available_countries()
    res = dict()
    for cn in countries:
        print('{} -> {}'.format(cn, country.get_code(cn)))
        data = ci.read(cn)
        data = data[-61:-1]
        uv0 = 0
        for daily in data:
            uv = int(daily['uvIndex'])
            uv0 += uv
        uv0 = uv0 / 60

        res[country.get_code(cn)] = np.round(uv0, 1)
    with open('saved/uv_geo.json', 'w+') as f:
        json.dump(res, f, indent=4)


def get_geography():
    with open('saved/uv_geo.json', 'r') as f:
        r = json.load(f)
    res = []
    for c in r:
        u = dict()
        u['country'] = c
        u['color'] = colormap(r[c])
        u['info'] = str(r[c])
        res.append(u)
    return res


def get_bubbles():
    return []


def colormap(uv):
    a = 0.5 * np.tanh((uv - 5) * 0.3) + 0.5
    color1 = [122, 200, 92]
    color2 = [200, 76, 81]
    c = color.interpol(color1, color2, a)
    return color.toRGB(*c)
