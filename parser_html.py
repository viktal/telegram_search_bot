import requests
import socks
import socket
import typing
from bs4 import BeautifulSoup
from dataclasses import dataclass


def get_html(url) -> typing.Tuple[str, str]:
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
    socket.socket = socks.socksocket
    response = requests.get(url)
    response.encoding = "utf8"
    return response.url, response.text


@dataclass
class File:
    name: str
    date: str
    link: str
    download: str
    distributions: str
    loadings: str
    size: str


def parser_text(text):
    soup = BeautifulSoup(text, features='html.parser')
    soup.prettify()
    downloads_list = soup.find('div', {'id': 'index'})
    if downloads_list is None:
        error = soup.find_all('h1')[1].text.split(".")[0]
        raise ValueError(error)

    download_items = downloads_list.find_all('tr', {'class': ["gai", "tum"]})

    files: typing.List[File] = []
    for file in download_items:
        item = file.find_all("td")

        normalize = lambda x: x.replace("\xa0", " ").strip()

        date: str = normalize(item[0].text)
        name: str = normalize(item[1].text)

        links: typing.List = item[1].find_all("a")
        download: str = normalize(links[0].get("href"))
        link: str = normalize(links[2].get("href"))

        ind: int = 2
        if not (item[2].text.endswith("GB") or item[2].text.endswith("MB")):
            ind += 1
        size: str = normalize(item[ind].text)

        distributions: str = normalize(item[ind + 1].find('span', {'class': 'green'}).text)
        loadings: str = normalize(item[ind + 1].find('span', {'class': 'red'}).text)

        files.append(File(
            name, date, link, download, distributions, loadings, size
        ))
    return files
