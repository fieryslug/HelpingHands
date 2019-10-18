import sys
sys.path.insert(1, '.')
import api.utils as utils
import api.apis as apis
from analysis import weather
import pprint as pprint
import numpy as np

'''
u = weather.do_something()
print(u)
'''

def do_something(sy,ey):
     s = str(sy)+'-10-1'
     e = str(ey)+'-10-1'
     j = utils.make_request_wwo(apis.wwo.historical_local, 'Tanzania', {'date': s ,'enddate': e})
     return j


j = do_something(2008,2018)
list = []
for i in j['data']['weather'][1]['hourly']:
    list.append(int(i['humidity']))

print(np.std(list,axis =0))
for i in j['data']['weather'][1]['hourly']:
    if abs(int(i['humidity']) - np.mean(list,axis =0) > .5*np.std(list,axis=0)):
        print("weird")

     
