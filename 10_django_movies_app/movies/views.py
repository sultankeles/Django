from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Categories

from .serializers import CategoriesSerializer


class CategoriesMVS(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer