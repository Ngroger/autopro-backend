from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ads.views import CarModelViewSet, TruckModelViewSet, BoatModelViewSet, EquipmentModelViewSet, ServiceModelViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from user.views import RegistrationAPIView, LoginAPIView, LogoutAPIView, CheckTokenView
from chat.views import UserModelView, MessageModelView, RoomModelView


router = routers.DefaultRouter()

router.register('api/car', CarModelViewSet)
router.register('api/truck', TruckModelViewSet)
router.register('api/boat', BoatModelViewSet)
router.register('api/eqipment', EquipmentModelViewSet)
router.register('api/service', ServiceModelViewSet)

router.register('api/users', UserModelView)
router.register('api/messages', MessageModelView)
router.register('api/rooms', RoomModelView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('check-token/', CheckTokenView.as_view(), name='check-token'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)