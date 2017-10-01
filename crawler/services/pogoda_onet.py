import requests
import re
from bs4 import BeautifulSoup
from crawler.super_crawler import SuperCrawler
class PogodaOnet(SuperCrawler):

    def __init__(self):
        super().__init__()
        self.name = 'pogoda_onet'

    def get_temperatures(self):
        response = requests.get('https://pogoda.onet.pl/prognoza-pogody/warszawa-357732')
        soup = BeautifulSoup(response.text)
        chart_div = soup.find('div', class_='chartSvgWrapper')
        temps = [re.findall('\d+', tag.text)[0] for tag in chart_div('text', class_='chartValue')]
        temps = temps[:24]
        return temps

