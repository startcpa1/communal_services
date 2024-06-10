from rest_framework import serializers

from buildings.models import House, Apartment, WaterMeter, Tariff


class HouseSerializer(serializers.ModelSerializer):
    """Сериализатор для домов"""

    class Meta:
        model = House
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    """Сериализатор для квартир"""

    class Meta:
        model = Apartment
        fields = '__all__'


class WaterMeterSerializer(serializers.ModelSerializer):
    """Сериализатор для счетчиков"""

    class Meta:
        model = WaterMeter
        fields = '__all__'


class TariffMeterSerializer(serializers.ModelSerializer):
    """Сериализатор для счетчиков"""

    class Meta:
        model = Tariff
        fields = '__all__'
