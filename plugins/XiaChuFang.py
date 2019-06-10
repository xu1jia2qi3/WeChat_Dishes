from .MenuProvider import MenuProvider
from bs4 import BeautifulSoup
from urllib.request import urlopen


class XiaChuFang(MenuProvider):

    def __init__(self, num_suggestions: int):
        super().__init__(num_suggestions)
        self.name = 'XiaChuFang'

    def _update_menu(self):
        html = urlopen(
            "https://www.xiachufang.com/explore/").read().decode('utf-8')
        soup = BeautifulSoup(html)
        for li in soup.select('div.recipe'):
            self.menu.append({
                'title': li.img['alt'],
                'img': li.img['data-src'],
                'url': 'https://www.xiachufang.com' + li.a['href']
            })
