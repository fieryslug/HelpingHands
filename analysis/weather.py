from api import utils
from api import apis
from matplotlib import pyplot as plt
from pprint import pprint

def draw_temp(loc, date):
    a = utils.make_request_wwo(apis.wwo.historical_local, loc, {'date': date})
    data = a['data']['weather']
    pprint(data)

    for day in data:
        hour = day['hourly']
        t = []
        temp = []
        for h in hour:
            t.append(int(h['time']))
            temp.append(int(h['tempC']))
            plt.scatter(t, temp)
        plt.show()


def r(loc, year_i, year_f):
    a = utils.make_request_wwo(apis.wwo.historical_local, loc, {'date': year_i + '-01-01', 'enddate': year_i + '-03-12'})
    data = a['data']['weather']
    pprint(data)