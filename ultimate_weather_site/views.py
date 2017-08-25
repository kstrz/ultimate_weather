from django.shortcuts import render
from django.views import generic
from .models import *
# Create your views here.


def index(reqest):
    services = Service.objects.all()
    temp_dict = {}
    for service in services:
        temp_dict[service.name] = Temperatures.objects.get(service_id=service.pk).getTemperatures()

    context = {
        'temp_dict': temp_dict
    }
    return render(reqest, 'ultimate_weather_site/index.html', context)


class IndexView(generic.DetailView):
    template_name = 'ultimate_weather_site/index.html'