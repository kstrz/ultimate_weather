import requests
from bs4 import BeautifulSoup
import lxml
from crawler.super_crawler import SuperCrawler
class PogodaInteria(SuperCrawler):

    def __init__(self):
        super().__init__()
        self.name = 'pogoda_interia'

    def __str__(self):
        return 'POGDA_INTERIA_SERVICE'

    def get_temperatures(self):
        response = requests.get('https://pogoda.interia.pl/prognoza-szczegolowa-warszawa,cId,8755')
        soup = BeautifulSoup(response.text, 'lxml')
        today_list = soup.find('div', class_='weather-forecast-hbh-main-list')\
            .find('div', class_='weather-forecast-hbh-list is-not-hidden')
        hours = [tag.span.span.text for tag in today_list('div', class_='entry-hour')]
        temperatures = [tag.text for tag in today_list('span', class_='forecast-temp')]


        return list(zip(hours, temperatures))

