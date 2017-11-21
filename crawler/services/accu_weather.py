import requests
import re
from bs4 import BeautifulSoup
from crawler.super_crawler import SuperCrawler
import lxml

class AccuWeather(SuperCrawler):

    def __init__(self):
        super().__init__()
        self.name = 'accu_weather'

    def __str__(self):
        return 'ACCU_WEATHER_SERVICE'

    def get_temperatures(self):
        self.response = requests.get('https://www.accuweather.com/pl/pl/warsaw/274663/hourly-weather-forecast/274663',
                                     headers={
                                         'authority':'www.accuweather.com',
                    'method':'GET',
                    'path':'/pl/pl/warsaw/274663/hourly-weather-forecast/274663',
                    'scheme':'https',
                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'accept-encoding':'gzip, deflate, br',
                    'accept-language':'pl-PL,pl;q=0.8,en-US;q=0.6,en;q=0.4',
                    'upgrade-insecure-requests':'1',
                    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'})

        self.soup = BeautifulSoup(self.response.text, 'lxml')

        self.temperatures = []
        self.hours = []
        # table shows 8 hours at once
        for _ in range(3):
            self._get_temperatures()
            self._get_hours()
            self._get_next_hours()

        return list(zip(self.hours, self.temperatures))

    def _get_temperatures(self):
        self.temps_table = self.soup.find('div', class_='overview-hourly').table
        temps_row = self.temps_table.find('tbody').find('tr')
        self.temperatures.extend([ re.findall('\d+', tag.text)[0] for tag in temps_row('span')])

    def _get_hours(self):
        tr_tag = self.temps_table.find('thead').find('tr')
        self.hours.extend([td_tag.find('div').text for td_tag in tr_tag('td')])

    def _get_next_hours(self):
        self.next_hours_url = self.soup.find('div', class_='hourly-control').find('a', class_='right-float')['href']
        self.response = requests.get(self.next_hours_url, headers={
                                         'authority':'www.accuweather.com',
                    'method':'GET',
                    'path':'/pl/pl/warsaw/274663/hourly-weather-forecast/274663',
                    'scheme':'https',
                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'accept-encoding':'gzip, deflate, br',
                    'accept-language':'pl-PL,pl;q=0.8,en-US;q=0.6,en;q=0.4',
                    'upgrade-insecure-requests':'1',
                    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'})
        self.soup = BeautifulSoup(self.response.text, 'lxml')
