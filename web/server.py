from flask import Flask, request
import web.configs as configs
import api.api_request as utils
from analysis import drought, heat, health
import json

app = Flask(__name__)
context = configs.SSL_CONTEXT
path = 'https://cms.nehs.hc.edu.tw:50043'

@app.route('/list.json', methods=['GET', 'POST'])
def handle_list():
    res = [
        {
            'title': 'Drought',
            'src': path + '/api.json?dataset=Drought'
        }
    ]
    print(request)
    return str(res)


@app.route('/api.json', methods=['POST', 'GET'])
def handle_api():

    data = request.json
    print(data)

    with open('cache/datasets/drought.json', 'r') as f:
        s = json.load(f)
    
    res = dict()

    res['title'] = 'Drought'
    res['info'] = drought.info
    #res['geography'] = drought.get_geography()
    #res['bubble'] = drought.get_bubbles()
    return str(s)


@app.route('/', methods=['GET'])
def handle_get():
    return 'hello world'


def run_server():
    app.run(host='0.0.0.0', port=configs.PORT, debug=True, ssl_context=configs.SSL_CONTEXT)
