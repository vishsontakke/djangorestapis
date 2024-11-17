from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import Productvieset

router = DefaultRouter()
router.register(r'products',Productvieset)

urlpatterns = [
    path('', include(router.urls)),
]