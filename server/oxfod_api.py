from oxford_keys import OXFORD_OCR_KEY
import requests
import json

OXFORD_OCR_URL = 'https://api.projectoxford.ai/vision/v1.0/ocr'


def oxford_ocr(image_url):
    headers = {'Ocp-Apim-Subscription-Key': OXFORD_OCR_KEY, 'Content-Type': 'application/json'}
    url_params = {'detectOrientation': 'true', 'language': 'en'}
    data = {'url': image_url}
    response = requests.post(OXFORD_OCR_URL, params=url_params, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        data = json.loads(response.content)

        for region in data['regions']:
            print 'region'
            for line in region['lines']:
                for word in line['words']:
                    print word['text'] + ' ',
                print ''


oxford_ocr('http://1.bp.blogspot.com/-zJPE8d1AUAQ/TvIMKiUSTUI/AAAAAAAABqQ/JQlmMg6wyOc/s1600/words.png')
