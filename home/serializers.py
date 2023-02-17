from rest_framework import serializers
from .models import WeatherData, WeatherDataStats




class WeatherDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherData
        fields = ["weather_station", "date", "temp_high", "temp_low", "precip"]

    # def to_representation(self, instance):
    #     data = super(DataStoreSerializer, self).to_representation(instance)
    #     data['timestamp'] = data.pop('last_updated')
    #     data['price'] = data.pop('current_price')
    #     data['coin'] = data.pop('coin_id')
    #     return data

class WeatherDataStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherDataStats
        fields = ["weather_station", "year", "avg_temp_high", "avg_temp_low", "total_precip"]
