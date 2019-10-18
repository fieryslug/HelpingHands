import api.utils as utils
import api.apis as apis
import requests

#c = utils.make_request_cdo('data', {'datasetid': 'GSOM', 'locationid': 'ZIP:28801', 'units': 'standard', 'startdate': '2010-05-01', 'enddate': '2010-05-01'})
c = utils.make_request_wwo(apis.wwo.local_weather, 'London', {'date': '2019-10-19'})
print(c)
