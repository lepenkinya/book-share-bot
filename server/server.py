import json
from flask import Flask, jsonify, request
from ssl_paths import CERTIFICATE_PATH, KEY_PATH

app = Flask(__name__)


@app.route("/start", methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        data = json.loads(request.data)
        message = data['message']
        chat_id = message['chat']['id']
        return jsonify(method='sendMessage', chat_id=chat_id, text='hey yo')
    else:
        return jsonify(method='method', param='param')


@app.route("/")
def hello():
    return "Hello World!"


context = (CERTIFICATE_PATH, KEY_PATH)

if __name__ == "__main__":
    app.run('0.0.0.0', port=443, ssl_context=context)
