from rest_framework.views import APIView
from .models import WeatherData, WeatherDataStats
from .serializers import WeatherDataSerializer, WeatherDataStatsSerializer
from home.pagination import CustomPagination
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from datetime import datetime


# WeatherDataApiView
limit = openapi.Parameter('limit', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True, default=365)
offset = openapi.Parameter('offset', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True, default=0)
weather_station = openapi.Parameter('weather_station', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
date = openapi.Parameter('date', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
temp_high = openapi.Parameter('temp_high', in_=openapi.IN_QUERY, type=openapi.TYPE_NUMBER)
temp_low = openapi.Parameter('temp_low', in_=openapi.IN_QUERY, type=openapi.TYPE_NUMBER)
precip = openapi.Parameter('precip', in_=openapi.IN_QUERY, type=openapi.TYPE_NUMBER)
year = openapi.Parameter('year', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER)

avg_temp_high = openapi.Parameter('avg_temp_high', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
avg_temp_low = openapi.Parameter('avg_temp_low', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
total_precip = openapi.Parameter('total_precip', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER)


class WeatherDataApiView(APIView):
    # pagination_class = CustomPagination

    @swagger_auto_schema(
        manual_parameters=[offset, limit, weather_station, date, temp_high, temp_low, precip, year],
    )
    def get(self, request, *args, **kwargs):
        filters = {}
        for key, value in request.GET.items():
            if key in ['weather_station', 'date', 'temp_high', 'temp_low', 'precip', 'year']:
                if key == 'date':
                    value = datetime.strptime(self.request.GET['date'], '%Y%m%d')
                filters[key] = value
        if filters:
            datastore =  WeatherData.objects.filter(**filters)
        else:
            datastore = WeatherData.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(datastore, request)
        serializer = WeatherDataSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)


class WeatherDataStatsApiView(APIView):
    @swagger_auto_schema(
        manual_parameters=[offset, limit, weather_station,avg_temp_high, avg_temp_low, total_precip, year],
    )
    def get(self, request, *args, **kwargs):
        filters = {}
        for key, value in request.GET.items():
            if key in ['weather_station', 'avg_temp_high', 'avg_temp_low', 'total_precip', 'year']:
                filters[key] = value
        if filters:
            datastore = WeatherDataStats.objects.filter(**filters)
        else:
            datastore = WeatherDataStats.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(datastore, request)
        serializer = WeatherDataStatsSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)
