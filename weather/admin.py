from django.contrib import admin
from django import forms
from .models import City
import requests
from django.conf import settings
from django.utils import timezone

class CityAdminForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']  

    def save(self, commit=True):
        instance = super().save(commit=False)
        appid = settings.WEATHER_API_KEY
        url = f'https://api.openweathermap.org/data/2.5/weather?q={instance.name}&units=metric&appid={appid}'
        try:
            res = requests.get(url).json()
            if res.get('cod') == 200:  # Successful request
                instance.temperature = res["main"]["temp"]
                instance.pressure = res["main"]["pressure"]
                instance.humidity = res["main"]["humidity"]
                instance.icon = res["weather"][0]["icon"]
                instance.is_user_request = False  # Admin-added cities
            else:
                self.add_error('name', f"City not found: {res.get('message', 'Unknown error')}")
                raise ValueError(f"API error: {res.get('message')}")
        except requests.RequestException as e:
            self.add_error('name', 'Failed to connect to the weather service')
            raise ValueError(f"Request error: {str(e)}")
        
        if commit:
            instance.save()
        return instance

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    form = CityAdminForm
    list_display = ('name', 'temperature', 'pressure', 'humidity', 'created_at', 'is_user_request')
    list_filter = ('created_at', 'is_user_request')
    search_fields = ('name',)
    ordering = ('-created_at',)