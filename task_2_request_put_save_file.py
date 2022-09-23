import os
import requests


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        path = file_path.split('/')
        if len(path) > 1:
            list_folders = '/'.join(path[:-1])
            self.create_folder(list_folders)
        parameters = {'path': file_path, 'overwrite': 'true'}
        headers = self.get_headers()
        response = requests.get(url, headers=headers, params=parameters).json()
        with open(file_path, 'rb') as file:
            response = requests.put(response['href'], files={'file': file}, headers=headers, params=parameters)

    def get_file(self, url):
        headers = self.get_headers()
        response = requests.get(url, headers=headers).json()
        for files in response['items']:
            for y in files.items():
                print(y)

    def create_folder(self, list_folders):
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources' 
        headers = self.get_headers()
        parameters = {'path': list_folders, 'overwrite': 'false'}
        response = requests.put(url, headers=headers, params=parameters)

def open_file_token(path, encoding):
    with open(path, encoding=encoding) as file:
        reader = file.readline().rstrip('\n')
    return reader


if __name__ == '__main__':

    path_to_file = 'list_file/test1.txt'
    token = open_file_token('token.txt', 'utf-8')
    uploader = YaUploader(token)
    # file = uploader.get_file('https://cloud-api.yandex.net:443/v1/disk/resources/files')
    result = uploader.upload(path_to_file)
   