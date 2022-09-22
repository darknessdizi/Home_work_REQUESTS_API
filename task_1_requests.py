import requests
import json


def save_http_request(url):
    reader = requests.get(url)
    name_file = url.split('/')[-1]
    name_file = ''.join(name_file) + '.txt'
    with open(name_file, 'w', encoding='utf-8') as file:
        file.write(reader.text)
    return name_file

def compare_heroes(*arg):
    list_heroes = [*arg]
    return list_heroes
    
def read_json(file, list):
    with open(file, encoding='utf-8-sig') as f:
        reader = json.load(f)
        my_list = []
        # for item in reader['rss']['channel']['items']:
        for item in reader:
            if item['name'] in list:
                my_dict = {}
                my_dict['name'] = item['name']
                my_dict['intelligence'] = item['powerstats']['intelligence']
                my_list.append(my_dict)
            # des = [word for word in item['description'].split(' ') if len(word) > max]
            # my_list.extend(des)
        print(my_list)


if __name__ == '__main__':

    url = 'https://akabab.github.io/superhero-api/api/all.json'
    list_hero = compare_heroes('Hulk', 'Captain America', 'Thanos')
    read_json(save_http_request(url), list_hero)
