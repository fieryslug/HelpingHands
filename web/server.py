from flask import Flask, request
import configs

import api.utils as utils

app = Flask(__name__)
context = configs.SSL_CONTEXT

@app.route('/', methods=['POST'])
def handle_post():
    data = request.json
    return 'hello world'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=configs.PORT, debug=True, ssl_context=configs.SSL_CONTEXT)
