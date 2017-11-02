import lxml
import json
import requests
from bs4 import BeautifulSoup
from crawler.super_crawler import SuperCrawler

class TwojaPogoda(SuperCrawler):

    def __init__(self):
        super().__init__()
        self.name = 'twoja_pogoda'

    def get_temperatures(self):
        self.temps = []
        response = requests.get('http://data.twojapogoda.pl/forecasts/city/hourly/2333/1').text
        self.response_json = json.loads(response)
        self._get_hours_and_temps()
        response = requests.get('http://data.twojapogoda.pl/forecasts/city/hourly/2333/2').text
        self.response_json = json.loads(response)
        self._get_hours_and_temps()

        return self.temps

    def _get_hours_and_temps(self):
        for row in self.response_json['forecasts']:
            self.temps.append((row['name'].split(':')[0], row['temp']))
