from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import generic
from .models import *
import datetime
import numpy as np
import sys
# Create your views here.

HISTORY_DAYS = 30

def index(request, date=None):
    
    today = datetime.date.today()
    if not date:
        date = today
    else:
        date = datetime.date(*(int(x) for x in (date.split('-'))))

    services = Service.objects.all()
    temp_dict = {}


    for service in services:
        try:
            today_temps = Temperatures.objects.filter(service_id=service.pk, date=date).first()
            if today_temps:
                temp_dict[service.name] = today_temps.getTemperatures()
        except ObjectDoesNotExist:
            pass

    
    ordinal_today = datetime.date.toordinal(today)
    ordinal_day = ordinal_today
    dates = []
    for x in range(HISTORY_DAYS):
        dates.append(str(datetime.date.fromordinal(ordinal_day)))
        ordinal_day -= 1

    context = {
        'temp_dict': temp_dict,
        'dates': dates,
        'current_date': str(date)
    }
    return render(request, 'ultimate_weather_site/index.html', context)


def correctness(request):

    services = Service.objects.all()

    services_temps = {}

    for service in services:
        services_temps[service] = np.rshape(HISTORY_DAYS,24)
        a = Temperatures.objects.filter(service_id=service.pk, )


    return  render(request, 'ultimate_weather_site/correctness.html')


class IndexView(generic.DetailView):
    template_name = 'ultimate_weather_site/index.html'