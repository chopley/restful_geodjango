from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop, Sensor, SensorData


admin.site.register(Shop, OSMGeoAdmin)
admin.site.register(Sensor, OSMGeoAdmin)
admin.site.register(SensorData, OSMGeoAdmin)

