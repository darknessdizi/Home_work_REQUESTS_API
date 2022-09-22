import requests
import json


def open_http_request(url, list):
    reader = requests.get(url)
    reader = json.loads(reader.text)
    my_list = []
    for item in reader:
        if item['name'] in list:
            my_dict = {}
            my_dict['name'] = item['name']
            my_dict['intelligence'] = item['powerstats']['intelligence']
            my_list.append(my_dict)
    my_list.sort(key=lambda i: i['intelligence'])
    print(my_list[-1])


if __name__ == '__main__':

    url = 'https://akabab.github.io/superhero-api/api/all.json'
    list_hero = ['Hulk', 'Captain America', 'Thanos', 'Batwoman V']

    open_http_request(url, list_hero)
