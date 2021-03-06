import requests
from bs4 import BeautifulSoup
from time import sleep


class Scraper:
    def __init__(self):
        self.base_url = "https://www.bbc.com/"
        self.url = "https://www.bbc.com/portuguese/topics/clmq8rgyyvjt/page/"
        self.classes = {'page-links-class':'qa-heading-link lx-stream-post__header-link',
                        'author-class':'bbc-1a3w4ok e1c9i7u11',
                        'text-class':'bbc-bm53ic e1cc2ql70'}

    def get_links(self, page):
        """
        returns an iterator with the links from the website page
        """
        sleep(0.25)

        r = requests.get(self.url + str(page))
        soup = BeautifulSoup(r.text, "lxml")

        for element in soup.find_all(
            "a", class_=self.classes['page-links-class']
        ):
            yield element["href"]

    def get_all_links(self):

        r = requests.get(self.url + "1")
        soup = BeautifulSoup(r.text, "lxml")

        first_page_num = soup.find(
            "span",
            class_="lx-pagination__page-number qa-pagination-current-page-number",
        ).string
        last_page_num = soup.find(
            "span", class_="lx-pagination__page-number qa-pagination-total-page-number"
        ).string

        for i in range(int(first_page_num), int(last_page_num) + 1):
            self.get_links(i)

    def _get_link(self, url: str) -> str:
        return self.base_url + url

    def _build_json(self, soup: BeautifulSoup, url: str) -> dict:
        """
        Returns a dict object with data extracted from the website
        """
        return dict(
            Titulo=soup.h1.string,
            Data=soup.time["datetime"],
            Texto=self._get_text(soup),
            Url=self._get_link(url),
            Autor=self._get_author(soup),
        )

    def _get_author(self, soup: BeautifulSoup) -> str:
        try:
            return soup.find("li", class_=self.classes['author-class']).string
        except AttributeError:
            return "Não informado"

    def _get_text(self, soup: BeautifulSoup) -> str:
        text = ""
        for element in soup.find_all("p", class_=self.classes['text-class']):
            text += str(element.string) + "\n"
        return text

    def scrap_article(self, url):
        sleep(0.25)

        link = self._get_link(url)

        r = requests.get(link)
        soup = BeautifulSoup(r.text, "lxml")

        return self._build_json(soup=soup, url=url)
