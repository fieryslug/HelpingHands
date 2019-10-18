from utils import time, data_manipulating as dm
from api import api_request, apis
import datetime
import json
from json import JSONDecodeError


def crawl_and_save(loc, date_i, date_f):
    if type(date_i) == str:
        date_i = time.to_date(date_i)
    if type(date_f) == str:
        date_f = time.to_date(date_f)
    delta = datetime.timedelta(30)
    one_day = datetime.timedelta(1)
    res = []
    date = date_i
    enddate = date_i + delta

    while enddate < date_f + delta:
        r = api_request.make_request_wwo(apis.wwo.historical_local, loc, {'date': date, 'enddate': enddate, 'tp': '6'})
        if 'weather' in r['data'].keys():
            d = r['data']['weather']
            for daily in d:
                dm.remove_url(daily)
                k, v = dm.separate(daily)
                res.append(v)
        print(enddate)
        date = enddate + one_day
        enddate = date + delta

    with open('cache/wwo/past-weather/' + loc.lower() + '.json', 'w+') as f:
        json.dump(res, f)
    return res


def read(loc):
    res = []
    with open('cache/wwo/past-weather/' + loc + '.json', 'r') as f:
        r = json.load(f)
    for daily in r:
       res.append(dm.assemble(dm.KEY6, daily))
    return res
