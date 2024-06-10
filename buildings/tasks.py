from celery import shared_task

from buildings.models import House, Apartment


@shared_task
def calculate_bill(house_id, month_id):
    """Асинхронная задача для расчета счета за воду для всех квартир в доме за указанный месяц."""
    house = House.objects.get(id=house_id)
    apartments = Apartment.objects.filter(house=house)

    total = 0  # начальное значение равно 0

    for apartment in apartments:
        water_meter = apartment.water_meters.filter(month=month_id)
        if water_meter:
            tariff = apartment.tariff
            bill = water_meter.readings * tariff.price_per_unit + apartment.area * tariff.price_per_area
            total += bill
    return total
