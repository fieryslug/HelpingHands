import sys
sys.path.insert(1, '.')
from api import api_request, apis, cache_interface as ci
from utils import data_manipulating as dm, country
from pprint import pprint
from constants.countries import countries
<<<<<<< HEAD
from analysis import drought, heat
=======
from analysis import drought, heat, health, color, uv
>>>>>>> 4b98829d4cafdc02efba7c1b2c6aa037b2d167b8


for country in countries:
    if ci.crawl_and_save(country, '2008-01-01', '2019-09-30') == -1:
        break
