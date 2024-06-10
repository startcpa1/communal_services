from celery.result import AsyncResult
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import calculate_bill

from buildings.models import House, Apartment, WaterMeter, Tariff
from buildings.serializers import HouseSerializer, ApartmentSerializer, WaterMeterSerializer, TariffMeterSerializer


class HouseViewSet(viewsets.ModelViewSet):
    """Класс для просмотра и редактирования экземпляров House."""
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    """Класс для просмотра и редактирования экземпляров Apartment."""
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class WaterMeterViewSet(viewsets.ModelViewSet):
    """Класс для просмотра и редактирования экземпляров WaterMeter."""
    queryset = WaterMeter.objects.all()
    serializer_class = WaterMeterSerializer


class TariffViewSet(viewsets.ModelViewSet):
    """Класс для просмотра и редактирования экземпляров Tariff."""
    queryset = Tariff.objects.all()
    serializer_class = TariffMeterSerializer


@api_view(['POST'])
def start_calculation(request):
    house_id = request.data.get('house_id')
    month = request.data.get('month')
    task = calculate_bill.delay(house_id, month)
    return Response({'task_id': task.id})


@api_view(['GET'])
def get_task_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        'task_id': task_id,
        'task_status': task_result.status,
        'task_result': task_result.result
    }
    return Response(result)