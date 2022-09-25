import requests
import datetime


def my_date(year, month, day):

    '''Функция возвращает дату в переводе на unixtime, type int'''

    date = int(datetime.datetime(year, month, day).timestamp())
    return date

def usage_of_questions(date, *tag):

    '''Функция получает дату в формате unixtime или "2022-09-12" 

    и кортеж тегов для поиска. Осуществляет Get запрос по url 

    и выводит на печать перечень вопрос по указанным параметрам
    
    '''

    # url = 'https://api.stackexchange.com/2.3/questions?fromdate=1662768000&order=desc&sort=creation&tagged=python&site=stackoverflow'
    url = 'https://api.stackexchange.com/2.3/questions'
    parameters = {
        'fromdate': date, 
        'order': 'desc', 
        'sort': 'creation',
        'tagged': ';'.join(tag),
        'site': 'stackoverflow'
        }

    response = requests.get(url, params=parameters).json()
    for element in response['items']:
        if set(tag).issubset(set(element['tags'])): 
            # print('----------------------------------------')
            # print(element['tags'])
            print(element['title'], end='\n\n')

if __name__ == '__main__':
    # from_date = my_date(2022, 8, 20)
    # usage_of_questions(from_date, 'docxtpl')
    usage_of_questions('2022-09-25', 'python')
    # usage_of_questions(from_date, 'python', 'docxtpl')