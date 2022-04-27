"""
Программа скачивает файлы по адресам указанным в urls.txt и помещает их в директорию download
В файле urls.txt, на последней строке, должен стоять перевод строки
"""

import wget


f = open('urls.txt', 'r', encoding='utf8')
lst = f.readlines()
f.close()
for i in range(0, len(lst)):
    url = lst[i][:-1]
    index = lst[i].rfind('/')
    wget.download(url, f'./download/{lst[i][index + 1:-1]}')
