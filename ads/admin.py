from django.contrib import admin
from .models import *

admin.site.register(AdBaseModel)
admin.site.register(AdImageModel)
admin.site.register(CarModel)
admin.site.register(TruckModel)
admin.site.register(BoatModel)
admin.site.register(EquipmentModel)
admin.site.register(ServiceModel)