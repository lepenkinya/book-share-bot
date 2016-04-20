from config import API_KEY
from config import WEBHOOK_URL
import requests

API_URL = "https://api.telegram.org/bot"

url = API_URL + API_KEY + "/setWebhook"

certificate = {'certificate': open('public.pem', 'rb')}

r = requests.post(url, data={'url': WEBHOOK_URL}, files=certificate)
print r.status_code
print r.reason
