from django.contrib import admin
from .models import Sensor, MoistureReading

# Manage the sensors and readings

admin.site.register(Sensor)
admin.site.register(MoistureReading)
