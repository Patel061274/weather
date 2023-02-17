from django.urls import path
from .views import (
    WeatherDataApiView,
    WeatherDataStatsApiView
)

urlpatterns = [
    path('weather', WeatherDataApiView.as_view()),
    path('weather/stats', WeatherDataStatsApiView.as_view()),

]