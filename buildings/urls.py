from django.urls import path
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from buildings.apps import BuildingsConfig
from buildings.views import HouseViewSet, ApartmentViewSet, WaterMeterViewSet, TariffViewSet

app_name = BuildingsConfig.name

router = DefaultRouter()
router.register(r'houses', HouseViewSet)
router.register(r'apartment', ApartmentViewSet)
router.register(r'water-meter', WaterMeterViewSet)
router.register(r'tariffs', TariffViewSet)


urlpatterns = [

]
