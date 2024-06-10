from rest_framework import viewsets

from buildings.models import House, Apartment, WaterMeter, Tariff
from buildings.serializers import HouseSerializer, ApartmentSerializer, WaterMeterSerializer, TariffMeterSerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.object.all()
    serializer_class = HouseSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.object.all()
    serializer_class = ApartmentSerializer


class WaterMeterViewSet(viewsets.ModelViewSet):
    queryset = WaterMeter.object.all()
    serializer_class = WaterMeterSerializer


class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.object.all()
    serializer_class = TariffMeterSerializer
