from django.contrib import admin
from .models import WeatherData, WeatherDataStats

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['weather_station', 'date', 'temp_high', 'temp_low', 'precip']
    list_filter = ['weather_station']


@admin.register(WeatherDataStats)
class WeatherDataStatsAdmin(admin.ModelAdmin):
    list_display = ['weather_station', 'year', 'avg_temp_high', 'avg_temp_low', 'total_precip']
    list_filter = ['weather_station']