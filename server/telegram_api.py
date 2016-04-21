from bot_internal import API_KEY

API_URL = "https://api.telegram.org/bot"
FILE_URL = 'https://api.telegram.org/file/bot'


def telegram_method_url(method):
    return API_URL + API_KEY + '/' + method


def telegram_download_file_url(file_id):
    return FILE_URL + API_KEY + '/' + file_id
