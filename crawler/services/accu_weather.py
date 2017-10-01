import requests
import re
from bs4 import BeautifulSoup
from crawler.super_crawler import SuperCrawler

class AccuWeather(SuperCrawler):

    def __init__(self):
        super().__init__()
        self.name = 'accu_weather'

    def get_temperatures(self):

        response = requests.get('https://www.accuweather.com/pl/pl/warsaw/274663/hourly-weather-forecast/274663')
        soup = BeautifulSoup(response.text)
        temps_table = soup.find('div', class_='overview-hourly').table.tbody
        temps_row = temps_table.find('tr')
        temperatures = [tag.text for tag in temps_row('span')]

        next_hours_url = soup.find('div', class_='hourly-control').a['href']

        response = requests.get(next_hours_url)
        soup = BeautifulSoup(response.text)
        temps_table = soup.find('div', class_='overview-hourly').table.tbody
        temps_row = temps_table.find('tr')
        temperatures.extend([tag.text for tag in temps_row('span')])

        next_hours_url = soup.find('div', class_='hourly-control').a['href']

        response = requests.get(next_hours_url)
        soup = BeautifulSoup(response.text)
        temps_table = soup.find('div', class_='overview-hourly').table.tbody
        temps_row = temps_table.find('tr')
        temperatures.extend([tag.text for tag in temps_row('span')])

        temps = []
        for temp in temperatures:
            temps.append(re.findall('\d+', temp)[0])
        return temps


