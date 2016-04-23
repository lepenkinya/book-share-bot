from oxford_keys import OXFORD_OCR_KEY
import requests
import json

OXFORD_OCR_URL = 'https://api.projectoxford.ai/vision/v1.0/ocr'


def oxford_ocr(image_url):
    headers = {'Ocp-Apim-Subscription-Key': OXFORD_OCR_KEY, 'Content-Type': 'application/json'}
    url_params = {'detectOrientation': 'true', 'language': 'en'}
    data = {'url': image_url}
    response = requests.post(OXFORD_OCR_URL, params=url_params, headers=headers, data=json.dumps(data))
    print response.status_code


oxford_ocr('http://www.multicultural.vic.gov.au/images/stories/articles/Interpreter-Symbol-text-jpg.jpg')
