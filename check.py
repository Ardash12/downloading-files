"""
Программа проверки урлов.
Список адресов для проверки берется из файла check-urls.txt
Адреса с кодом ответа отличным от 200, копируются в файл check-error.txt
"""
import requests
from requests.exceptions import ConnectionError


f = open('check-urls.txt', 'r', encoding='utf8')
urls = f.readlines()
f.close()
lst_error = []
count = 0
for url in urls:
    count += 1
    print(count, end=' ')
    try:
        response = requests.get('https://www.m-vanna.ru/' + url[:-1])
        if response.status_code == 200:
            print(response.status_code, 'https://www.m-vanna.ru/' + url[:-1])
        else:
            print(response.status_code, 'https://www.m-vanna.ru/' + url[:-1])
            lst_error.append(url)
    except ConnectionError as e:
        print(e)

f = open('check-error.txt', 'w', encoding='utf8')
f.writelines(lst_error)
f.close()




