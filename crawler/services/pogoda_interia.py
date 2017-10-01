import requests
from bs4 import BeautifulSoup
from crawler.super_crawler import SuperCrawler
class PogodaInteria(SuperCrawler):

    def __init__(self):
        super().__init__()
        self.name = 'pogoda_interia'

    def get_temperatures(self):
        response = requests.get('https://pogoda.interia.pl/prognoza-szczegolowa-warszawa,cId,8755')
        soup = BeautifulSoup(response.text)
        today_list = soup.find('li', class_='weather-forecast-day')
        # hours = [tag.text for tag in today_list('span', class_='hour')]
        temperatures = [tag.text for tag in today_list('span', class_='forecast-temp')]
        # temp_dict = list(zip(hours, temperatures))

        return temperatures
