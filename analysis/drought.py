from api import cache_interface as ci
import datetime
from matplotlib import pyplot as plt
from utils import time as times, country as country_util
import time as time
import json


info = 'EEDI index'
colormap = {
    'ED4': '#FF3C00',
    'ED3': '#FF7518',
    'ED2': '#FFC238',
    'ED1': '#F4FF43',
    'ED0': '#B6FF43',
    'Neutral': '#23FF13',
    'EW0': '#5AFF93',
    'EW1': '#61FFD1',
    'EW2': '#50DEFF',
    'EW3': '#2D82FF',
    'EW4': '#221BFF'
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
        return 'Neutral'
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


def calculate_and_save():
    countries = ci.get_available_countries()
    res = []
    for country in countries:
        a = recent(country)
        d = dict()
        d['country'] = country_util.get_code(country)
        d['modal_info'] = "<br><img src='generated/drought/" + country + ".png'>"
        d['color'] = colormap[a]
        d['info'] = a
        d['index'] = a
        plot(country)
        res.append(d)
    with open('saved/drought_geo.json', 'w+') as f:
        json.dump(res, f, indent=4)


def get_geography():
    with open('saved/drought_geo.json', 'r') as f:
        j = json.load(f)
    return j


def get_bubbles():
    res = []
    return res


def plot(loc):
    data = ci.read(loc)
    dates = []
    quan = []
    for daily in data:
        dates.append(datetime.datetime.strptime(daily['date'], '%Y-%m-%d').date())
        e = ee(daily)
        quan.append(e)

    fig, ax = plt.subplots()

    ax.plot(dates, quan, lw=0.3)
    plt.savefig('generated/drought/' + loc + '.png')
