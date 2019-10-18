import api.utils as utils
import api.apis as apis
import requests

c = utils.make_request_wwo(apis.wwo.local_weather, '41, 23.5', dict())
print(c)

