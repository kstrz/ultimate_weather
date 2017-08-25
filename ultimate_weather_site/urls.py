from django.conf.urls import url
from ultimate_weather_site.views import *
app_name = 'ultimate_weather_site'

urlpatterns = [
    url(r'^$', index, name='index')
]