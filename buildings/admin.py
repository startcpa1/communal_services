from django.contrib import admin

from buildings.models import House, Apartment, WaterMeter, Tariff

admin.site.register(House)
admin.site.register(Apartment)
admin.site.register(WaterMeter)
admin.site.register(Tariff)




