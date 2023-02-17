from django.core.management.base import BaseCommand, CommandError
import glob
import pandas as pd
from home.models import WeatherData, WeatherDataStats
from django.db.models import Avg, Sum
from django.db.models.functions import Round

class Command(BaseCommand):
    help = 'Extracting the data from the WeatherData' \
           ' and Store the Data Analysing into WeatherDataStats'

    def handle(self, *args, **options):
        self.stdout.write(f"Extracting data from WeatherData to Process data analysis")
        response = WeatherData.objects.values('weather_station', 'year').annotate(
            avg_temp_high=Round(Avg('temp_high'), 2)).annotate(
            avg_temp_low=Round(Avg('temp_low'), 2)).annotate(
            total_precip=Round(Sum('precip'), 2))
        self.stdout.write(f"Total WeatherData count: {len(response)}")
        if len(response) == 0:
            raise CommandError(f"Response returns empty")

        for row in response:
            weather_data_stats = WeatherDataStats.objects.create(**row)

        self.stdout.write(f"Successfully inserted analysed data into WeatherDataStats")

