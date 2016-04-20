import requests

from server.telegram_api import telegram_url_for_method

url = telegram_url_for_method("setWebhook")

certificate = {'certificate': open('public.pem', 'rb')}

r = requests.post(url, data={'url': WEBHOOK_URL}, files=certificate)
print r.status_code
print r.reason
