import sys
sys.path.insert(1, '.')
from api import api_request, apis, cache_interface as ci
from utils import data_manipulating as dm, country
from pprint import pprint
from constants.countries import countries
from analysis import drought, heat, health, color, uv

drought.calculate_and_save()