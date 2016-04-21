import urllib, json, requests
from telegram_api import telegram_method_url, telegram_get_file_url
from flask import Flask, jsonify, request
from ssl_paths import CERTIFICATE_PATH, KEY_PATH

app = Flask(__name__)


@app.route("/start", methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        data = json.loads(request.data)
        message = data['message']
        max_photo_info = max(message['photo'], key=lambda x: x['width'])
        file_id = max_photo_info['file_id']

        file_name = download_file(file_id)

        chat_id = message['chat']['id']
        return jsonify(method='sendMessage', chat_id=chat_id, text='hey yo')
    else:
        return jsonify(method='method', param='param')


def download_file(file_id):
    url = telegram_method_url('getFile')
    response = requests.get(url, params={'file_id': file_id})
    file_path = response.json()['result']['file_path']
    file_name = file_path.split('/')[-1]
    urllib.urlretrieve(telegram_get_file_url(file_path), file_name)
    return file_name


@app.route("/")
def hello():
    return "Hello World!"


context = (CERTIFICATE_PATH, KEY_PATH)

if __name__ == "__main__":
    app.run('0.0.0.0', port=443, ssl_context=context)
