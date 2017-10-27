from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import generic
from .models import *
import datetime
import numpy as np
from ultimate_weather_site.statistics import Statistics
import sys
# Create your views here.

HISTORY_DAYS = 30

def get_dates():
    today = datetime.date.today()
    ordinal_today = datetime.date.toordinal(today)
    ordinal_day = ordinal_today
    dates = []
    for x in range(HISTORY_DAYS):
        dates.append(str(datetime.date.fromordinal(ordinal_day)))
        ordinal_day -= 1

    return dates


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
                temp_dict[str(service)] = [x if x else '-' for x in today_temps.get_temperatures()]
        except ObjectDoesNotExist:
            pass

    context = {
        'temp_dict': temp_dict,
        'dates': get_dates(),
        'current_date': str(date)
    }
    return render(request, 'ultimate_weather_site/index.html', context)


def statistics(request):

    last_day = datetime.datetime.today()
    first_day = datetime.datetime.fromordinal(datetime.datetime.toordinal(last_day)-HISTORY_DAYS)
    services = Service.objects.all()
    services_temps = {}


    for service in services:
        service_name = str(service)
        services_temps[service_name] = np.full((HISTORY_DAYS, 24), -300, dtype=np.int32)
        daily_temps = Temperatures.objects.all().filter(service_id=service.pk, date__gt=first_day, date__lte=last_day).all()
        for i, today_temps in enumerate(daily_temps):
            services_temps[service_name][i] = [x if x is not None else -300 for x in today_temps.get_temperatures()]


    real_temps = services_temps['Actual']
    del services_temps['Actual']

    services_stats = {}
    for service_name, temps in services_temps.items():
        stats = Statistics(temps, real_temps)
        services_stats[service_name] = {}
        services_stats[service_name]['correctness'] = stats.count_service_correctness()
        services_stats[service_name]['avg_temp_diff'] = stats.count_avg_temp_diff()
        services_stats[service_name]['std'] = stats.count_std()
        services_stats[service_name]['median'] = stats.count_median()
        services_stats[service_name]['mode'] = stats.count_mode()

    context = {'services_stats': services_stats,
               'dates': get_dates()
               }
    return render(request, 'ultimate_weather_site/statistics.html', context)


class IndexView(generic.DetailView):
    template_name = 'ultimate_weather_site/index.html'