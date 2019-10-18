import api.params as params
import api.secrets as secrets
import requests


def make_request_nasa(api_name, extra):
    extra['api_key'] = secrets.key_nasa
    r = requests.get('https://api.nasa.gov/{}'.format(api_name), extra)
    return r.content


def make_request_cdo(endpoint):
    headers = {'token': secrets.key_cdo}
    r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/{}'.format(endpoint), headers=headers)
    return r.content


def make_request_wwo(api_name, loc, query):
    query['q'] = loc
    query['key'] = secrets.key_wwo
    query['format'] = 'json'
    r = requests.get('http://api.worldweatheronline.com/premium/v1/{}.ashx'.format(api_name), query)
    print(r.url)
    return r.content
