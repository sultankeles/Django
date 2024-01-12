from django.urls import path, include

from .views import CategoriesMVS

from rest_framework import routers


router = routers.DefaultRouter()
router.register('categories', CategoriesMVS)

urlpatterns = [
    path('', include(router.urls))
]