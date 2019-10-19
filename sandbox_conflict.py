import sys
sys.path.insert(1, '.')
from analysis import weather
from pprint import pprint
from utils import time
from api import api_request, apis
import numpy as np

a = api_request.make_request_wwo(apis.wwo.local_weather, 'taiwan', dict())
# pprint(a['data']['weather'])


'''
u = weather.do_something()
print(u)
'''

def do_something(sy,ey):
     s = str(sy)+'-10-1'
     e = str(ey)+'-10-1'
     j = api_request.make_request_wwo(apis.wwo.historical_local, 'Tanzania', {'date': s , 'enddate': e})
     return j


j = do_something(2008,2018)
list = []
mx_h = 0
mn_h = 100
for i in j['data']['weather'][1]['hourly']:
    list.append(int(i['humidity']))
    if mx_h < int(i['humidity']):
        mx_h = int(i['humidity'])
    if mn_h > int(i['humidity']):
        mn_h = int(i['humidity'])


# print(np.std(list,axis =0))
print(str(mx_h)+' '+str(mn_h))
for i in j['data']['weather'][1]['hourly']:
    if abs(int(i['humidity']) - np.mean(list,axis =0) > .5*np.std(list,axis=0)):
        print("weird")

     
