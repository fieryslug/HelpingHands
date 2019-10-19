from flask import Flask, request, send_from_directory
import web.configs as configs
import api.api_request as utils
from analysis import drought, heat, health, hospital
import json
from pprint import pprint

app = Flask(__name__)

context = configs.SSL_CONTEXT
path = 'https://cms.nehs.hc.edu.tw:50043'


@app.route('/list.json', methods=['GET', 'POST'])
def handle_list():
    res = [
        {
            'title': 'Drought',
            'src': '/api.json?dataset=Drought'
        },
        {
            'title': 'Health Center Density',
            'src': '/api.json?dataset=HealthCenterDensity'
        },
        {
            'title': 'Heat Index',
            'src': '/api.json?dataset=HeatIndex'
        },
        {
            'title': 'Hospitals',
            'src': '/api.json?dataset=Hospital'
        }
    ]
    print(request)
    return json.dumps(res)


@app.route('/api.json', methods=['POST', 'GET'])
def handle_api():

    res = dict()
    dataset = request.args.get('dataset')
    if dataset == 'Drought':
        res['title'] = 'Drought'
        res['info'] = 'EEDI'
        res['geography'] = drought.get_geography()
        res['bubbles'] = drought.get_bubbles()
    if dataset == 'HealthCenterDensity':
        res['title'] = 'Health center density'
        res['info'] = 'density of health centers'
        res['geography'] = health.get_geography()
        res['bubbles'] = health.get_bubbles()
    if dataset == 'HeatIndex':
        res['title'] = 'Heat index'
        res['info'] = 'heat index'
        res['geography'] = heat.get_geography()
        res['bubbles'] = heat.get_bubbles()
    if dataset == 'Hospital':
        res['title'] = 'Hospital'
        res['info'] = 'hospitals'
        res['geography'] = hospital.get_geography()
        res['bubbles'] = hospital.get_bubbles()
    print(res)
    return json.dumps(res)


@app.route('/', methods=['GET'])
def handle_get():
    return send_from_directory('templates', 'index.html')


def run_server():
    app.run(host='0.0.0.0', port=configs.PORT, debug=True)
