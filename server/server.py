import json, requests, uuid

from flask import Flask, jsonify, request

from isbn import get_ISBN
from isbn_search import find_book_by_isbn
from oxfod_api import get_lines_from_image
from ssl_paths import CERTIFICATE_PATH, KEY_PATH
from telegram_api import telegram_method_url, telegram_get_file_url

app = Flask(__name__)


def handle_inline_query(query):
    inline_query_id = query['id']
    query = query['query']
    results = [{'type': 'article', 'id': uuid.uuid4(), 'title': 'my_title',
                'input_message_content': {'message_text': 'bot received query : ' + query}}]

    return jsonify(method='answerInlineQuery', inline_query_id=inline_query_id, results=results)


def handle_message(message):
    if 'photo' in message:
        return handle_sent_photo(message)

    chat_id = message['chat']['id']
    return jsonify(method='sendMessage', chat_id=chat_id, text='handling message no photo send')


@app.route("/start", methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        data = json.loads(request.data)

        if 'message' in data:
            message = data['message']
            return handle_message(message)

        if 'inline_query' in data:
            query = data['inline_query']
            return handle_inline_query(query)

    else:
        return jsonify(method='method', param='param')


def handle_sent_photo(message):
    max_photo_info = max(message['photo'], key=lambda x: x['width'])
    file_id = max_photo_info['file_id']
    url = get_file_url(file_id)
    lines = get_lines_from_image(url)
    chat_id = message['chat']['id']
    isbn = get_ISBN(lines)

    if not len(isbn):
        return jsonify(method='sendMessage', chat_id=chat_id, text='ISBN is not detected')

    books = find_book_by_isbn(isbn)

    if len(books):
        return jsonify(method='sendMessage', chat_id=chat_id, text=books[0].to_string())

    return jsonify(method='sendMessage', chat_id=chat_id, text='ISBN: ' + isbn)


@app.route("/")
def hello():
    return "Hello World!"


def get_file_url(file_id):
    url = telegram_method_url('getFile')
    response = requests.get(url, params={'file_id': file_id})
    file_path = response.json()['result']['file_path']
    return telegram_get_file_url(file_path)


context = (CERTIFICATE_PATH, KEY_PATH)

if __name__ == "__main__":
    app.run('0.0.0.0', port=443, ssl_context=context)
