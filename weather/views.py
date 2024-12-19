import requests
from django.shortcuts import render
from .models import CitySearchHistory
from django.conf import settings

def get_weather_data(city_name, units):
    api_key = "6b7fc746d344a9818d18f31d94780651"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&units={units}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def weather_view(request):
    context = {}
    if request.method == "POST":
        city_name = request.POST.get("city_name")
        units = request.POST.get("units", "metric")
        days = int(request.POST.get("days", 5))
        max_entries = days * 8
        weather_data = get_weather_data(city_name, units)
        if weather_data.get("cod") == "200":
            CitySearchHistory.objects.create(city_name=city_name)
            context = {
                "city": city_name,
                "units": units,
                "days": days,
                "max_entries": 40,
                "weather": weather_data,
                "history": CitySearchHistory.objects.order_by('-searched_at')[:5],
            }
        else:
            context = {"error": "City not found!", "history": CitySearchHistory.objects.order_by('-searched_at')[:5]}
    return render(request, "weather/index.html", context)
