from utils import country
import json
import numpy as np
from analysis import color

info = 'health center density'


def save():
    hl = dict()
    with open('constants/HEALTH_CENTRE_DENSITY.csv', 'r') as f:
        s = f.read()
    k = s.split('\n')
    for kk in k:
        c = kk.split(',')
        print(c[0])
        hl[country.get_code(c[0])] = float(c[3])
        if country.get_code(c[0]) == 'unknown':
            print('!!!' + c[0])

    with open('saved/health.json', 'w+') as f:
        json.dump(hl, f, indent=4)


def get_geography():
    res = []
    with open('saved/health.json', 'r') as f:
        j = json.load(f)
    for coun in j:
        d = dict()
        d['country'] = coun
        d['color'] = colormap(j[coun])
        d['info'] = str(j[coun])
        res.append(d)
    return res


def get_bubbles():
    return []


def colormap(index):
    a = np.tanh(index * 0.2)
    r = int(255 * (1-a))
    g = int(255 * a)

    return color.toRGB(r, g, 0)
