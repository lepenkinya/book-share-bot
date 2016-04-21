import requests

from server.telegram_api import telegram_method_url
from server.bot_internal import WEBHOOK_URL

url = telegram_method_url("setWebhook")

certificate = {'certificate': open('public.pem', 'rb')}

r = requests.post(url, data={'url': WEBHOOK_URL}, files=certificate)
print r.status_code
print r.reason
