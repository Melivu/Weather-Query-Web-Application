import requests
from django.shortcuts import render
from .models import City
from django.utils import timezone
from django.conf import settings

def index(request):
    appid = settings.WEATHER_API_KEY
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        city_name = request.POST.get('city', '').strip()
        if city_name:
            try:
                res = requests.get(url.format(city_name)).json()
                if res.get('cod') == 200:  # Successful request
                    city_info = {
                        'city': city_name,
                        'temp': res["main"]["temp"],
                        'pressure': res["main"]["pressure"],
                        'humidity': res["main"]["humidity"],
                        'icon': res["weather"][0]["icon"]
                    }
                    # Save to database with is_user_request=True
                    City.objects.create(
                        name=city_name,
                        temperature=res["main"]["temp"],
                        pressure=res["main"]["pressure"],
                        humidity=res["main"]["humidity"],
                        icon=res["weather"][0]["icon"],
                        created_at=timezone.now(),
                        is_user_request=True
                    )
                else:
                    city_info = {'city': city_name, 'error': res.get('message', 'City not found or API error')}
            except requests.RequestException:
                city_info = {'city': city_name, 'error': 'Failed to connect to the weather service'}
        else:
            city_info = {'error': 'Please enter a city name'}
    else:
        city_info = {}

    context = {'info': city_info}
    return render(request, 'weather/index.html', context)

def history(request):
    history = City.objects.filter(is_user_request=True).order_by('-created_at')
    context = {'history': history}
    return render(request, 'weather/history.html', context)