import requests
import socks
import socket
import collections
import re
import typing
from bs4 import BeautifulSoup

"""
Сортировка OK
Стрелочки OK
Кол-во скачивающих OK
try..except если порвалось соединение OK
статусы
Язык
open search (you can use russian language)
Have a good day
Tell me Thanks! for end
Справка
Показывать по 10
Enter in terminal

start оставить и добавить справку
FILES глобально! вывести печатать в отдельную функцию и печатать их с переменной
В конце вывести вариант закончить или продолжать 
"""

def get_html(url):
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
    socket.socket = socks.socksocket
    response = requests.get(url)
    response.encoding = "utf8"
    return response.url, response.text


def parser_text(text):
    soup = BeautifulSoup(text, features='html.parser')
    soup.prettify()
    downloads_list = soup.find('div', {'id': 'index'})
    download_items = downloads_list.find_all('tr', {'class': ["gai", "tum"]})

    File = collections.namedtuple("File", "name date link download distributions loadings size")
    files: typing.List[File] = []
    for file in download_items:
        item = file.find_all("td")

        date: str = item[0].text
        name: str = item[1].text
        links: typing.List = item[1].find_all("a")
        download: str = links[0].get("href")
        link: str = links[2].get("href")
        i: int = 2
        if not (item[2].text.endswith("GB") or item[2].text.endswith("MB")):
            i += 1
        size: str = item[i].text

        distributions: str = item[i + 1].find('span', {'class': 'green'}).text
        loadings: str = item[i + 1].find('span', {'class': 'red'}).text

        append_line: File = File(name, date, link, download, distributions, loadings, size)
        # sub_re = re.compile(r"[\s]+")
        # for elem in append_line:
        #     elem = re.sub(sub_re, " ", elem)
        #     elem = elem.rstrip()
        #     print(elem)

        files.append(append_line)
    return files

# with open("text.html", "w") as fh:
#     text = get_html("http://www.rutor.info/search/%D1%80%D0%B8%D0%BA%20%D0%B8%20%D0%BC%D0%BE%D1%80%D1%82%D0%B8")
#     fh.write(text)
# files = parser_text(text)

# with open("text.html", "r") as fh:
#     text = fh.read()
# parser_text(text)
