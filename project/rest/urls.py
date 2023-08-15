
from django.urls import path
from .view.korea_views import (
    korea_food,
    food_detail
)


app_name ="food"
urlpatterns = [
    path("koreafood/",korea_food, name="korea_food"),
    path("food_detail/<int:SH_ID>/",food_detail,name="food_detail")
]
