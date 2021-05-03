import requests
from bs4 import BeautifulSoup
from time import sleep

class Scraper():
    def __init__(self):
        self.base_url = 'https://www.bbc.com/'
        self.url = 'https://www.bbc.com/portuguese/topics/clmq8rgyyvjt/page/'
        self.links = []

    def get_links(self,page):
        sleep(0.25)

        r = requests.get(self.url + str(page))
        soup = BeautifulSoup(r.text,'lxml')

        for element in soup.find_all("a",class_='qa-heading-link lx-stream-post__header-link'):
            self.links.append(element['href'])
    
    def get_all_links(self):

        r = requests.get(self.url + '1')
        soup = BeautifulSoup(r.text,'lxml')

        first_page_num = soup.find("span",class_='lx-pagination__page-number qa-pagination-current-page-number').string
        last_page_num = soup.find("span",class_='lx-pagination__page-number qa-pagination-total-page-number').string

        for i in range(int(first_page_num),int(last_page_num)+1):
            self.get_links(i)
    
    def scrap_article(self,url):
        sleep(0.25)

        link = self.base_url + url

        r = requests.get(link)
        soup = BeautifulSoup(r.text,'lxml')
        
        page = {}
        page['Titulo'] = soup.h1.string
        page['Data'] = soup.time['datetime']
        page['Texto'] = ''
        page['Url'] = link

        try:
            page['Autor'] = soup.find("li",class_='bbc-1a3w4ok e1c9i7u11').string
        except AttributeError:
            page['Autor'] = 'Não informado'
        
        for element in soup.find_all("p",class_="bbc-bm53ic e1cc2ql70"):
            text = (str(element.string) + "\n")
            page['Texto'] += text

        return page
