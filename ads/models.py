import os
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .scripts import ad_image_upload_path


class AdBaseModel(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    city =  models.CharField(max_length = 255)
    pubication_date = models.DateTimeField(default=timezone.now)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.id}'


class AdImageModel(models.Model):

    ad = models.ForeignKey(AdBaseModel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=ad_image_upload_path)

    def __str__(self):
        return f'{self.ad.id}'


class CarModel(AdBaseModel):

    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    body = models.CharField(max_length = 255)
    mileage = models.IntegerField()
    condition = models.CharField(max_length = 255)
    color = models.CharField(max_length = 255)
    engine = models.CharField(max_length = 255)
    wheel = models.CharField(max_length = 255)
    box = models.CharField(max_length = 255)
    cleared = models.BooleanField()
    additionally = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.id} {self.brand} {self.model}'


class TruckModel(CarModel):

    weight = models.CharField(max_length=255)
    body_volume = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.brand} {self.model}'


class BoatModel(AdBaseModel):

    type = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    mileage = models.IntegerField()
    condition = models.CharField(max_length = 255)
    color = models.CharField(max_length = 255)
    engine = models.CharField(max_length = 255)
    cleared = models.BooleanField()
    additionally = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.id} {self.brand} {self.model}'


class EquipmentModel(AdBaseModel):

    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    additionally = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.id} {self.name}'


class ServiceModel(AdBaseModel):

    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    additionally = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.id} {self.name}'
