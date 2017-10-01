import datetime

from crawler.services.pogoda_interia import PogodaInteria
from crawler.services.twoja_pogoda import TwojaPogoda
from crawler.services.pogoda_onet import PogodaOnet
from crawler.services.accu_weather import AccuWeather
from ultimate_weather_site.models import Service
from ultimate_weather_site.models import Temperatures


class Main:

    def __init__(self):
        self.services = [PogodaInteria, TwojaPogoda, PogodaOnet, AccuWeather]
        self.temperatures = []

    def process(self):
        for service in self.services:
            self.service = service
            self.get_temperatures()
            if len(self.temperatures) == 24:
                self.save_temeretures()
            #log exception

    def get_temperatures(self):
        self.temperatures = self.service().get_temperatures()


    def save_temeretures(self):

        temps = Temperatures()

        temps.service_id = Service.objects.get(name=self.service().name)

        temps.h_01 = self.temperatures[0]
        temps.h_02 = self.temperatures[1]
        temps.h_03 = self.temperatures[2]
        temps.h_04 = self.temperatures[3]
        temps.h_05 = self.temperatures[4]
        temps.h_06 = self.temperatures[5]
        temps.h_07 = self.temperatures[6]
        temps.h_08 = self.temperatures[7]
        temps.h_09 = self.temperatures[8]
        temps.h_10 = self.temperatures[9]
        temps.h_11 = self.temperatures[10]
        temps.h_12 = self.temperatures[11]
        temps.h_13 = self.temperatures[12]
        temps.h_14 = self.temperatures[13]
        temps.h_15 = self.temperatures[14]
        temps.h_16 = self.temperatures[15]
        temps.h_17 = self.temperatures[16]
        temps.h_18 = self.temperatures[17]
        temps.h_19 = self.temperatures[18]
        temps.h_20 = self.temperatures[19]
        temps.h_21 = self.temperatures[20]
        temps.h_22 = self.temperatures[21]
        temps.h_23 = self.temperatures[22]
        temps.h_24 = self.temperatures[23]
        temps.date = datetime.datetime.today()

        temps.save()
