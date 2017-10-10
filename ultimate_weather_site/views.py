from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import generic
from .models import *
import datetime
import sys
# Create your views here.


def index(reqest, date=None):

    if not date:
        date = datetime.date.today()
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

    today = datetime.date.today()
    ordinal_today = datetime.date.toordinal(today)
    ordinal_day = ordinal_today
    dates = []
    for x in range(30):
        dates.append(str(datetime.date.fromordinal(ordinal_day)))
        ordinal_day -= 1

    context = {
        'temp_dict': temp_dict,
        'dates': dates,
        'current_date': str(date)
    }
    return render(reqest, 'ultimate_weather_site/index.html', context)


class IndexView(generic.DetailView):
    template_name = 'ultimate_weather_site/index.html'