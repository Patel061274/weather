from django.db import models
from django.db.models import UniqueConstraint

# Create your models here.

class WeatherData(models.Model):
    weather_station = models.CharField("Weather Station", max_length=255)
    date = models.DateField("Reported Date(YYYYMMDD)", max_length=50)
    temp_high = models.FloatField("Temperature Maximum",
                                    help_text="The maximum temperature for that day "
                                              "(in tenths of a degree Celsius)", default=None)
    temp_low = models.FloatField("Temperature Minimum",
                                    help_text="The Minimum temperature for that day "
                                              "(in tenths of a degree Celsius)", default=None)
    precip = models.FloatField("Precipitation",
                                 help_text="The amount of precipitation for that day "
                                           "(in tenths of a millimeter)", default=None)
    year = models.IntegerField("Year")

    class Meta:
        constraints = [
            UniqueConstraint(fields=['weather_station', 'date', 'temp_high', 'temp_low', 'precip'],
                             name='unique weather data')
        ]

    def __str__(self):
        return f"{self.weather_station} : {self.date}"


class WeatherDataStats(models.Model):
    weather_station  = models.CharField("Weather Station", max_length=255)
    year = models.IntegerField("Year")
    avg_temp_high = models.FloatField("Avg High Temperature", default=None)
    avg_temp_low = models.FloatField("Avg Low Temperature", default=None)
    total_precip = models.FloatField("Total Precipitation", default=None)


    def __str__(self):
        return f"Weather Station: {self.weather_station} | Year: {self.year}"