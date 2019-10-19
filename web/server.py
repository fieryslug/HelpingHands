from flask import Flask, request
import web.configs as configs
import api.api_request as utils
from analysis import drought, heat, health


app = Flask(__name__)
context = configs.SSL_CONTEXT

@app.route('/list.json', methods=['GET', 'POST'])
def handle_list():
    res = [
        {
            'title': 'Drought',
            'src': '/api.json?dataset=Drought'
        },
        {
            'title': 'HealthCenterDensity',
            'src': '/api.json?dataset=HealthCenterDensity'
        }
    ]
    return res

@app.route('/api.json', methods=['POST'])
def handle_api():
    data = request.json
    theme = data['dataset']

    res = dict()

    if theme == 'Drought':
        res['title'] = 'Drought'
        res['info'] = drought.info
        res['geography'] = drought.get_geography()
        res['bubble'] = drought.get_bubbles()
        return res

    if theme == 'HealthCenterDensity':
        res['title'] = 'health center density'
        res['info'] = health.info
        res['geography'] = health.get_geography()
        res['bubble'] = health.get_bubbles()

    return 'error!'


@app.route('/', methods=['GET'])
def handle_get():
    return 'hello world'


def run_server():
    app.run(host='0.0.0.0', port=configs.PORT, debug=True, ssl_context=configs.SSL_CONTEXT)
