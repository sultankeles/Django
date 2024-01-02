from django.urls import path, include
from .views import home

urlpatterns = [

    path('home/', home),

    # If we define an endpoint like path('', home), it directly executes 'home'.

    # When creating a new app, the first thing we need to do is to enter our app's full name into the INSTALLED_APPS section of the settings.py file.

]