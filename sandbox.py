import sys
sys.path.insert(1, '.')
from analysis import weather
from pprint import pprint
from gadgets import time
from api import utils, apis

a = utils.make_request_wwo(apis.wwo.local_weather, 'taiwan', dict())
pprint(a['data']['weather'])
