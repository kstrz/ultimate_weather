from datetime import date, datetime
from ultimate_weather_site.models import Service, Temperatures
from ultimate_weather_site.statistics import Statistics
import numpy as np
import pytz

HISTORY_DAYS = 30
ACTUAL_TEMPERATURES_SERVICE = Service.objects.get(name='actual')


def get_history_dates():
    today = get_local_date()
    ordinal_today = date.toordinal(today)
    ordinal_day = ordinal_today
    dates = []
    for x in range(HISTORY_DAYS):
        dates.append(str(date.fromordinal(ordinal_day)))
        ordinal_day -= 1

    return dates


def get_date(date_=None):
    today = get_local_date()
    if not date_:
        return today
    else:
        return date(*(int(x) for x in (date_.split('-'))))


def get_temperatures_with_colors(date_):
    temp_dict = {}
    services = Service.objects.all().exclude(name=ACTUAL_TEMPERATURES_SERVICE.name)
    real_temps_per_day_query = Temperatures.objects.filter(service_id__name=ACTUAL_TEMPERATURES_SERVICE.name,
                                                           date=date_).first()
    if real_temps_per_day_query:
        temp_dict[str(ACTUAL_TEMPERATURES_SERVICE)] = [{x: 'blue'} if x is not None else {'-': 'white'}
                                                       for x in real_temps_per_day_query.get_temperatures()]
    else:
        temp_dict[str(ACTUAL_TEMPERATURES_SERVICE)] = [{'-': 'white'} for x in range(24)]
    for service in services:
        temps_per_day_query = Temperatures.objects.filter(service_id=service.pk, date=date_).first()
        if temps_per_day_query:
            temps_per_day_with_colors = []
            temps_per_day = [x if x is not None else '-' for x in temps_per_day_query.get_temperatures()]
            for i, x in enumerate(temps_per_day):
                real_temp = list(temp_dict[str(ACTUAL_TEMPERATURES_SERVICE)][i].keys())[0]
                if isinstance(x, int) and isinstance(real_temp, int):
                    if abs(x - real_temp) < 2:
                        temps_per_day_with_colors.append({x: 'green'})
                    elif abs(x - real_temp) < 4:
                        temps_per_day_with_colors.append({x: 'yellow'})
                    else:
                        temps_per_day_with_colors.append({x: 'red'})
                else:
                    temps_per_day_with_colors.append({x: 'white'})
            temp_dict[str(service)] = temps_per_day_with_colors
    return temp_dict


def get_stats():
    historical_temps = _get_historical_temps()
    real_temps = historical_temps[str(ACTUAL_TEMPERATURES_SERVICE)]
    del historical_temps[str(ACTUAL_TEMPERATURES_SERVICE)]

    services_stats = {}
    for service_name, temps in historical_temps.items():
        stats = Statistics(temps, real_temps)
        services_stats[service_name] = {}
        if stats.are_statistics_available():
            services_stats[service_name]['correctness'] = stats.count_service_correctness()
            services_stats[service_name]['avg_temp_diff'] = stats.count_avg_temp_diff()
            services_stats[service_name]['std'] = stats.count_std()
            services_stats[service_name]['median'] = stats.count_median()
            services_stats[service_name]['mode'] = stats.count_mode()

    return services_stats


def _get_historical_temps():
    last_day = get_local_date()
    first_day = date.fromordinal(date.toordinal(last_day) - HISTORY_DAYS)
    services = Service.objects.all()
    historical_temps = {}

    for service in services:
        service_name = str(service)
        historical_temps[service_name] = np.full((HISTORY_DAYS, 24), -300, dtype=np.int32)
        all_history_temps = Temperatures.objects.all().filter(service_id=service.pk, date__gt=first_day,
                                                              date__lte=last_day).all()
        for i, temps_per_day in enumerate(all_history_temps):
            historical_temps[service_name][i] = [x if x is not None else -300 for x in temps_per_day.get_temperatures()]

    return historical_temps


def get_local_date():
    utc_moment = datetime.utcnow().replace(tzinfo=pytz.utc)
    local_time = utc_moment.astimezone(pytz.timezone('Poland'))
    return local_time.date()