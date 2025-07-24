from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=30)
    temperature = models.FloatField(null=True, blank=True)
    pressure = models.IntegerField(null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True)
    icon = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_user_request = models.BooleanField(default=False)  

    def __str__(self):
        return self.name
