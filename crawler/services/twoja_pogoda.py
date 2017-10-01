import requests
from bs4 import BeautifulSoup
from crawler.super_crawler import SuperCrawler

class TwojaPogoda(SuperCrawler):

    def __init__(self):
        super().__init__()
        self.name = 'twoja_pogoda'

    def get_temperatures(self):
        response = requests.get('http://www.twojapogoda.pl/polska/mazowieckie/warszawa/godzinowa')
        soup = BeautifulSoup(response.text)
        hours = [tag.contents[0].strip() for tag in soup.find_all('th', colspan=4)]
        temperatures = [tag.strong.text for tag in soup.find_all('div', class_='info')]
        # temp_dict = list(zip(hours, temperatures))


        response = requests.get('http://www.twojapogoda.pl/polska/mazowieckie/warszawa/godzinowa/2')
        soup = BeautifulSoup(response.text)
        hours = [tag.contents[0].strip() for tag in soup.find_all('th', colspan=4)]
        temperatures.extend([tag.strong.text for tag in soup.find_all('div', class_='info')])
        # temp_dict.extend(list(zip(hours, temperatures)))

        return temperatures

