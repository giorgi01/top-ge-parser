import requests
from bs4 import BeautifulSoup


class Parser:

    def __init__(self, url, page):
        self.web = requests.get(url=url)
        if page > 1:
            self.web = requests.get(url=url+f'page/{page}')

    def parse(self):
        soup = BeautifulSoup(self.web.content, 'html.parser')
        for item, item1 in \
            zip(soup.find_all('a', class_='stie_title'), soup.find_all('td',
                class_='tr_paddings desc_pd hidden-xs ipad_hidden')):
            print(item.get('href'))
            print(item.text)
            print(item1.text)
            print(" ".join(item.get('onmouseover').split(' ')[3:7])
                  .replace("<br/>',", ""))


topge_first = Parser('https://top.ge/', 3)
topge_first.parse()
