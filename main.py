"""
Программа скачивает файлы по адресам указанным в urls.txt и помещает их в директорию download
В файле urls.txt, на последней строке, должен стоять перевод строки
"""
import wget


f = open('urls.txt', 'r', encoding='utf8')
urls = f.readlines()
f.close()
lst_error = []
for url in urls:
    url = url[:-1]
    index = url.rfind('/')
    name_file = url[index + 1:].replace(' ', '_')   # обрезаем все, кроме имени файла меняем пробелы на знак "_"
    try:
        wget.download(url, f'./download/{name_file}')
    except Exception as e:
        print('Ошибка', e)
        lst_error.append(f'{e} - {url}\n')   # список ошибок со ссылками
f = open('link-error.txt', 'w', encoding='utf8')
f.writelines(lst_error)
f.close()
