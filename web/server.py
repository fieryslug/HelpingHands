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
        }
    ]
    return res


@app.route('/api.json/Drought', methods=['GET'])
def handle_api():

    res = dict()

    res['title'] = 'Drought'
    res['info'] = drought.info
    res['geography'] = drought.get_geography()
    res['bubble'] = drought.get_bubbles()
    return res


@app.route('/', methods=['GET'])
def handle_get():
    return 'hello world'


def run_server():
    app.run(host='0.0.0.0', port=configs.PORT, debug=True, ssl_context=configs.SSL_CONTEXT)
