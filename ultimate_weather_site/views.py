from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import generic
from .models import *
import datetime
import sys
# Create your views here.


def index(reqest):
    services = Service.objects.all()
    temp_dict = {}
    for service in services:
        try:
            today_temps = Temperatures.objects.filter(service_id=service.pk, date=datetime.date.today()).first()
            if today_temps:
                temp_dict[service.name] = today_temps.getTemperatures()
        except ObjectDoesNotExist:
            pass

    context = {
        'temp_dict': temp_dict
    }
    return render(reqest, 'ultimate_weather_site/index.html', context)


class IndexView(generic.DetailView):
    template_name = 'ultimate_weather_site/index.html'