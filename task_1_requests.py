import requests
from random import randint, sample


def _open_http_request():

    '''Функция осуществляет http запрос по имеющемуся url 
    
    и возвращает объект типа json
    
    '''

    url = 'https://akabab.github.io/superhero-api/api/all.json'
    reader = requests.get(url)
    reader = reader.json()
    return reader

def random_hero():

    '''Функция выбирает случайных героев из общего списка. 
    
    Возвращает список случайных героев (максимум 10)
    
    '''

    count = randint(4, 10)
    list_hero = []
    for item in _open_http_request():
        list_hero.append(item['name'])
    list_hero = sample(list_hero, count)
    return list_hero

def compare_heroes(new_list):

    '''Функция получает список героев и сравнивает их интелект.
    
    Возвращает словарь с данными на самых умных героев
    
    '''

    my_list = []
    for item in _open_http_request():
        if item['name'] in new_list:
            my_dict = {}
            my_dict['name'] = item['name']
            my_dict['intelligence'] = item['powerstats']['intelligence']
            my_list.append(my_dict)
    my_list.sort(key=lambda i: i['intelligence'])
    my_list[-1]['name'] = ', '.join(_recursive_function(my_list))
    return my_list[-1]

def _recursive_function(my_list):

    '''Функция получает отсортированный по интелекту список текущих 
    
    героев и возвращает список имен героев с максимальным уровнем 
    
    интелекта
    
    '''

    first_list = [my_list[-1]['name']]
    if my_list[-2]['intelligence'] == my_list[-1]['intelligence']:
        return first_list + _recursive_function(my_list[:-1])
    else:
        return first_list


if __name__ == '__main__':

    list_hero = random_hero()
    # list_hero = ['Hulk', 'Captain America', 'Thanos']

    hero = compare_heroes(list_hero)

    print(f'Из {len(list_hero)} героев: ', end='')
    print(*list_hero, sep=', ')
    print(f'Самые умные герои: {hero["name"]}. Уровень интелекта: {hero["intelligence"]}')