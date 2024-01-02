from django.urls import path, include
from cosmiosds.views import dshome

urlpatterns = [
    
    path('dshome/', dshome),

]
