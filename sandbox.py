import sys
sys.path.insert(1, '.')
from api import api_request, apis, cache_interface
from utils import data_manipulating as dm
from pprint import pprint

r = api_request.make_request_wwo(apis.wwo.historical_local, 'taiwan', {'date': '2010-10-20', 'enddate': '2010-10-24'})
pprint(r)

