from api import utils
from api import apis

def do_something():
    j = utils.make_request_wwo(apis.wwo.local_weather, 'London', {'date': '2010-10-9'})
    return j