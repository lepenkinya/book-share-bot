import json
import requests

from flask import Flask, jsonify, request

from isbn import get_ISBN
from oxfod_api import get_lines_from_image
from ssl_paths import CERTIFICATE_PATH, KEY_PATH
from telegram_api import telegram_method_url, telegram_get_file_url

app = Flask(__name__)


@app.route("/start", methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        data = json.loads(request.data)
        message = data['message']
        max_photo_info = max(message['photo'], key=lambda x: x['width'])
        file_id = max_photo_info['file_id']

        url = get_file_url(file_id)
        lines = get_lines_from_image(url)

        chat_id = message['chat']['id']

        isbn = get_ISBN(lines)
        if not len(isbn):
            return jsonify(method='sendMessage', chat_id=chat_id, text='ISBN is not detected')

        return jsonify(method='sendMessage', chat_id=chat_id, text='ISBN: ' + isbn)
    else:
        return jsonify(method='method', param='param')


def get_file_url(file_id):
    url = telegram_method_url('getFile')
    response = requests.get(url, params={'file_id': file_id})
    file_path = response.json()['result']['file_path']
    return telegram_get_file_url(file_path)


@app.route("/")
def hello():
    return "Hello World!"


context = (CERTIFICATE_PATH, KEY_PATH)

if __name__ == "__main__":
    app.run('0.0.0.0', port=443, ssl_context=context)
