from rest_framework import serializers
from .models import AdBaseModel, AdImageModel, CarModel, TruckModel, BoatModel, EquipmentModel, ServiceModel


class AdImageModelSerializer(serializers.ModelSerializer):

    ad = serializers.PrimaryKeyRelatedField(queryset=AdBaseModel.objects.all())

    class Meta:
        model = AdImageModel
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):

    images = AdImageModelSerializer(many=True, required=False)
    
    class Meta: 
        model = CarModel
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        car = CarModel.objects.create(**validated_data)
        ad = AdBaseModel.object.create(**validated_data)
        for image_data in images_data:
            ad_instance = car.get_real_instance()
            AdImageModel.objects.create(ad=ad_instance, **image_data)
        return car 


class TruckModelSerializer(serializers.ModelSerializer):

    images = AdImageModelSerializer(many=True, required=False)

    class Meta:
        model = TruckModel
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        truck = TruckModel.objects.create(**validated_data)
        ad = AdBaseModel.object.create(**validated_data)
        for image_data in images_data:
            ad_instance = truck.get_real_instance()
            AdImageModel.objects.create(ad=ad_instance, **image_data)
        return truck 
    

class BoatModelSerializer(serializers.ModelSerializer):

    images = AdImageModelSerializer(many=True, required=False)

    class Meta:
        model = BoatModel
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        boat = BoatModel.objects.create(**validated_data)
        ad = AdBaseModel.object.create(**validated_data)
        for image_data in images_data:
            ad_instance = boat.get_real_instance()
            AdImageModel.objects.create(ad=ad_instance, **image_data)
        return boat 
    

class EquipmentModelSerializer(serializers.ModelSerializer):

    images = AdImageModelSerializer(many=True, required=False)

    class Meta:
        model = EquipmentModel
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        equipment = EquipmentModel.objects.create(**validated_data)
        ad = AdBaseModel.object.create(**validated_data)
        for image_data in images_data:
            ad_instance = equipment.get_real_instance()
            AdImageModel.objects.create(ad=ad_instance, **image_data)
        return equipment 
    

class ServiceModelSerializer(serializers.ModelSerializer):

    images = AdImageModelSerializer(many=True, required=False)

    class Meta:
        model = ServiceModel
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        service = ServiceModel.objects.create(**validated_data)
        ad = AdBaseModel.object.create(**validated_data)
        for image_data in images_data:
            ad_instance = service.get_real_instance()
            AdImageModel.objects.create(ad=ad_instance, **image_data)
        return service 