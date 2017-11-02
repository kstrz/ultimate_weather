from django.shortcuts import render
from django.views import generic
from ultimate_weather_site.utils import *


def index(request, date=None):
    date = get_date(date)
    temp_dict_with_colors = get_temperatures_with_colors(date)
    context = {
        'temp_dict': temp_dict_with_colors,
        'dates': get_history_dates(),
        'current_date': str(date)
    }
    return render(request, 'ultimate_weather_site/index.html', context)


def statistics(request):
    services_stats = get_stats()
    context = {'services_stats': services_stats,
               'dates': get_history_dates()
               }
    return render(request, 'ultimate_weather_site/statistics.html', context)


class IndexView(generic.DetailView):
    template_name = 'ultimate_weather_site/index.html'