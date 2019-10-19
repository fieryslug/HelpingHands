from api import cache_interface as ci
import datetime
from matplotlib import pyplot as plt
from utils import time as times
import time as time
from constants.countries import country_code



info = 'EEDI index'
colormap = {
    'ED4': '#FF0016',
    'ED3': '#FF5564',
    'ED2': '#FF99A1',
    'ED1': '#FFC8CC',
    'ED0': 'FF2630',
    'Null': '#FFFFFF',
    'EW0': '#C7CDFF',
    'EW1': '#ACB4FF',
    'EW2': '#8588FF',
    'EW3': '#5F5DFF',
    'EW4': '#0829FF'
}

def ee(daily):
    tmax = -100
    tmin = 100
    for hourly in daily['hourly']:
        t = int(hourly['tempC'])
        if t > tmax:
            tmax = t
        if t < tmin:
            tmin = t
    return (tmax - tmin)**0.424 * (int(daily['avgtempC']))


def eddi(loc, test):
    data = ci.read(loc)
    day = []

    l = []
    for daily in data:
        date = daily['date']
        day.append(time.mktime(times.to_date(date).timetuple()))
        l.append(ee(daily))

    l = sorted(l)
    print(l)
    if test <= l[0]:
        return 0
    if test >= l[-1]:
        return 1

    di = 0

    for i in range(len(l)):
        if l[i] >= test:
            di = i
            break

    return di / len(l)


def get_name(eddi):
    if eddi <= 0.02:
        return 'EW4'
    if eddi <= 0.05:
        return 'EW3'
    if eddi <= 0.1:
        return 'EW2'
    if eddi <= 0.2:
        return 'EW1'
    if eddi <= 0.3:
        return 'EW0'
    if eddi <= 0.7:
        return 'Null'
    if eddi <= 0.8:
        return 'ED0'
    if eddi <= 0.9:
        return 'ED1'
    if eddi <= 0.95:
        return 'ED2'
    if eddi <= 0.98:
        return 'ED3'
    return 'ED4'


def recent(loc):
    data = ci.read(loc)
    data = data[-30:-1]
    e = 0
    for daily in data:
        e += ee(daily)
    e /= len(data)
    return get_name(eddi(loc, e))


def get_geography():
    res = []
    countries = ci.get_available_countries()
    for country in countries:
        a = recent(country)
        d = dict()
        d['country'] = country_code[country]
        d['color'] = colormap[a]
        d['info'] = a
        res.append(d)
    return res


def get_bubbles():
    res = []
    return res
