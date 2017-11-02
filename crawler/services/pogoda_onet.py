import requests
import re
import lxml
from datetime import datetime
from bs4 import BeautifulSoup
from crawler.super_crawler import SuperCrawler
class PogodaOnet(SuperCrawler):

    def __init__(self):
        super().__init__()
        self.name = 'pogoda_onet'

    def get_temperatures(self):
        response = requests.get('https://pogoda.onet.pl/prognoza-pogody/warszawa-357732')
        soup = BeautifulSoup(response.text, 'lxml')
        chart_div = soup.find('div', class_='chartSvgWrapper')
        temps = [re.findall('\d+', tag.text)[0] for tag in chart_div('text', class_='chartValue')]
        hours = []
        for tag in soup.find('ul', class_='list swiper-wrapper')('li'):
            hours.append(tag.find('div', class_='row hTime time').text.split(':')[0].strip())
        temps = temps[:24]
        hours = hours[:24]
        return list(zip(hours, temps))

