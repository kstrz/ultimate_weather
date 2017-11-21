import os
import re
import logging

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ultimate_weather.settings")
import django
django.setup()

from ultimate_weather_site import utils
from crawler.services.pogoda_interia import PogodaInteria
from crawler.services.twoja_pogoda import TwojaPogoda
from crawler.services.pogoda_onet import PogodaOnet
from crawler.services.accu_weather import AccuWeather
from ultimate_weather_site.models import Temperatures, Service


class Main:

    def __init__(self):
        self.services = [PogodaInteria, TwojaPogoda, PogodaOnet, AccuWeather]
        self.temperatures = []

    def process(self):
        for service in self.services:
            self.service = service()
            logging.info('PROCESSING ' + str(self.service))
            self._get_temperatures()
            self._normalize_values()
            self._save_temperatures()

    def _get_temperatures(self):
        self.temperatures = self.service.get_temperatures()
        logging.info('GOT ' + str(len(self.temperatures)) + ' FROM ' + str(self.service))

    def _normalize_values(self):
        logging.info('NORMALIZE ' + str(self.service))
        for i, hour_temp in enumerate(self.temperatures):
            if len(hour_temp[0]) == 1:
                hour_temp = ('0' + hour_temp[0], hour_temp[1])
            self.temperatures[i] = (hour_temp[0], re.findall(r'\d+', str(hour_temp[1]))[0] if hour_temp[1] else None)

    def _save_temperatures(self):
        temps = Temperatures()
        temps.service_id = Service.objects.get(name=self.service.name)

        for hour_temp in self.temperatures:
            setattr(temps, 'h_' + hour_temp[0], hour_temp[1])

        temps.date = utils.get_date()
        try:
            temps.save()
            logging.info('SAVED ' + str(self.service))
        except Exception as e:
            logging.error('SAVE ERROR ' + str(self.service) + str(e))

        #every time updates object in db
        # temps_dict = {}
        # temps_dict['service_id'] = Service.objects.get(name=self.service().name)
        # for hour_temp in self.temperatures:
        #     if hour_temp[1] is not None:
        #         temps_dict['h_' + hour_temp[0]] = hour_temp[1]
        #
        # temps_dict['date'] = datetime.datetime.today()
        #
        #
        # Temperatures.objects.update_or_create(temps_dict)
