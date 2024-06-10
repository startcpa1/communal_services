from django.db import models


class House(models.Model):
    """Модель для хранения информации о доме."""
    address = models.CharField(max_length=200, verbose_name='адрес')

    def __str__(self):
        return f"{self.address}"

    class Meta:
        verbose_name = 'дом'
        verbose_name_plural = 'дома'


class Apartment(models.Model):
    """Модель для хранения информации о квартире."""
    house = models.ForeignKey(House, on_delete=models.CASCADE, verbose_name='квартира', related_name='apartments')
    area = models.FloatField(verbose_name='площадь')

    def __str__(self):
        return f"{self.house}"

    class Meta:
        verbose_name = 'квартира'
        verbose_name_plural = 'квартиры'


class WaterMeter(models.Model):
    """Модель для хранения информации о счетчике."""
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name='адрес',
                                  related_name='water_meters')
    readings = models.FloatField(verbose_name='показания')
    month = models.DateField(verbose_name='дата')

    def __str__(self):
        return f"{self.apartment}"

    class Meta:
        verbose_name = 'счетчик'
        verbose_name_plural = 'счетчики'


class Tariff(models.Model):
    """Модель для хранения информации о тарифах."""
    price_per_unit = models.FloatField(verbose_name='тариф за единицу')
    price_per_area = models.FloatField(verbose_name='тариф за площадь')

    def __str__(self):
        return f"{self.price_per_unit}, {self.price_per_area}"

    class Meta:
        verbose_name = 'тариф'
        verbose_name_plural = 'тарифы'
