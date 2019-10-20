import sys
sys.path.insert(1, '.')
from api import api_request, apis, cache_interface as ci
from utils import data_manipulating as dm
from pprint import pprint
from constants.countries import countries
from analysis import drought, heat


for country in countries:
    if ci.crawl_and_save(country, '2008-01-01', '2019-09-30') == -1:
        break

