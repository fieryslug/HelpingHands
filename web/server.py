from flask import Flask, request, send_from_directory
import web.configs as configs
import api.api_request as utils
from analysis import drought, heat, health
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
        }
    ]
    print(request)
    return json.dumps(res)


@app.route('/api.json', methods=['POST', 'GET'])
def handle_api():

    data = request.json
    print(data)

    with open('cache/datasets/drought.json', 'r') as f:
        s = f.read()
    
    #res = dict()

    #res['title'] = 'Drought'
    #res['info'] = drought.info
    #res['geography'] = drought.get_geography()
    #res['bubble'] = drought.get_bubbles()
    print(s)
    return s


@app.route('/', methods=['GET'])
def handle_get():
    return send_from_directory('templates', 'index.html')


def run_server():
    app.run(host='0.0.0.0', port=configs.PORT, debug=True)
