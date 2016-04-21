from bot_internal import API_KEY

API_URL = "https://api.telegram.org/bot"
FILE_URL = 'https://api.telegram.org/file/bot'


def telegram_method_url(method):
    return API_URL + API_KEY + '/' + method


def telegram_get_file_url(file_url):
    return FILE_URL + API_KEY + '/' + file_url
