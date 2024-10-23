from django.db import models

# Data models for soil moisture readings, sensor information, and possibly weather data.


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class MoistureReading(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    moisture_level = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sensor.name} - {self.moisture_level}%'
