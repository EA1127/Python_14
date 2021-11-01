
import requests

import json
from datetime import datetime

URL = "https://www.reddit.com/r/entertainment/.json"

def timestamp_to_date(timestamp_obj):
    datetime_obj = datetime.fromtimestamp(timestamp_obj).strftime("%m/%d/%Y, %H:%M:%S")
    # print(datetime_obj)
    return str(datetime_obj)

def get_data(url):
    resonse = requests.get(url, headers={'User-agent': "your bot 0.1"})
    # print(resonse.status_code)
    # print(resonse.text)
    # print(type(resonse.text))
    json_object = resonse.text
    python_object = json.loads(json_object)
    # print(type(python_object))
    news = python_object['data']['children']
    # print(len(news))

    data = []
    number = 1
    for new in news:
        news_dictionary = {
            f'News No. {number}': {
                "title": new['data']['title'],
                "created": timestamp_to_date(new['data']['created']),
                "author": new['data']['author']
            }
        }
        number += 1
        data.append(news_dictionary)

    return data

def write_to_json(some_data):
    with open('Redditnews.json', 'w') as file:
        json.dump(some_data, file, indent=4)

def main(url):
    data = get_data(url)
    write_to_json(data)

main(URL)