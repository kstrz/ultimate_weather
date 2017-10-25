"""generates random* temperatures for last 30 days. for tests
run in virtual env: python ./manage.py shell < crawler/random_temps_generator.py
"""
import datetime
import random
from crawler.services.pogoda_interia import PogodaInteria
from crawler.services.twoja_pogoda import TwojaPogoda
from crawler.services.pogoda_onet import PogodaOnet
from crawler.services.accu_weather import AccuWeather
from ultimate_weather_site.models import Service
from ultimate_weather_site.models import Temperatures


today = datetime.date.today()
ordinal_today = datetime.date.toordinal(today)
ordinal_day = ordinal_today

services = [PogodaInteria, TwojaPogoda, PogodaOnet, AccuWeather]

for service in services:
    ordinal_day = ordinal_today
    for x in reversed(range(30)):
        temps = Temperatures()

        temps.service_id = Service.objects.get(name=service().name)

        temps.h_01 = random.randint(5, 10)
        temps.h_02 = random.randint(5, 10)
        temps.h_03 = random.randint(5, 10)
        temps.h_04 = random.randint(5, 10)
        temps.h_05 = random.randint(5, 10)
        temps.h_06 = random.randint(5, 10)
        temps.h_07 = random.randint(5, 10)
        temps.h_08 = random.randint(10, 15)
        temps.h_09 = random.randint(10, 15)
        temps.h_10 = random.randint(15, 22)
        temps.h_11 = random.randint(15, 22)
        temps.h_12 = random.randint(15, 22)
        temps.h_13 = random.randint(15, 22)
        temps.h_14 = random.randint(15, 22)
        temps.h_15 = random.randint(15, 22)
        temps.h_16 = random.randint(15, 22)
        temps.h_17 = random.randint(15, 22)
        temps.h_18 = random.randint(15, 22)
        temps.h_19 = random.randint(10, 15)
        temps.h_20 = random.randint(10, 15)
        temps.h_21 = random.randint(10, 15)
        temps.h_22 = random.randint(5, 10)
        temps.h_23 = random.randint(5, 10)
        temps.h_24 = random.randint(5, 10)
        temps.date = datetime.date.fromordinal(ordinal_day)

        temps.save()
        ordinal_day -= 1