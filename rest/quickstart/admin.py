from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop


admin.site.register(Shop, OSMGeoAdmin)

