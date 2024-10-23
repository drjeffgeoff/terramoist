from django.shortcuts import render
from .models import Sensor, MoistureReading

# Create your views here.


def dashboard(request):
    sensors = Sensor.objects.all()
    readings = MoistureReading.objects.all().order_by('-timestamp')[:10]
    return render(request, 'monitoring/dashboard.html', {'sensors': sensors, 'readings': readings})
