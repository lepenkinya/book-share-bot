from flask import Flask
from flask import request

from config import CERTIFICATE_PATH
from config import KEY_PATH

app = Flask(__name__)


@app.route("/start", methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        return "POST"
    else:
        return "GET"


@app.route("/")
def hello():
    return "Hello World!"


context = (CERTIFICATE_PATH, KEY_PATH)

if __name__ == "__main__":
    app.run('0.0.0.0', port=443, ssl_context=context)
