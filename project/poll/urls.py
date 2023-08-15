
from django.urls import path

from . import views

urlpatterns = [
    path("/fruit",views.fruit_data,name="fruit_data")
]




