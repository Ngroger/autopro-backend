from rest_framework import viewsets
from .models import CarModel, TruckModel, BoatModel, EquipmentModel, ServiceModel
from .serializers import CarModelSerializer, TruckModelSerializer, BoatModelSerializer, EquipmentModelSerializer, ServiceModelSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer  


class TruckModelViewSet(viewsets.ModelViewSet):
    queryset = TruckModel.objects.all()
    serializer_class = TruckModelSerializer  


class BoatModelViewSet(viewsets.ModelViewSet):
    queryset = BoatModel.objects.all()
    serializer_class = BoatModelSerializer  


class EquipmentModelViewSet(viewsets.ModelViewSet):
    queryset = EquipmentModel.objects.all()
    serializer_class = EquipmentModelSerializer  


class ServiceModelViewSet(viewsets.ModelViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceModelSerializer  