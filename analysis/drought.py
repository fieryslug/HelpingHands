from api import cache_interface as ci
import datetime
from matplotlib import pyplot as plt
from utils import time as times
import time as time

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


def e(loc):
    data = ci.read(loc)
    day = []
    l = []
    for daily in data:
        date = daily['date']
        day.append(time.mktime(times.to_date(date).timetuple()))
        l.append(ee(daily))
    plt.plot(day, l)
    plt.show()
