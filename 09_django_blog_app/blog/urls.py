from django.urls import path, include

from .views import CategoryMVS, BlogMVS

from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryMVS)
router.register('blog', BlogMVS)

urlpatterns = [
    path('', include(router.urls))
]