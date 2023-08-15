
from django.urls import path
from .view.uni_views import( 
    book_data
)
from .view.report_view import(
    report_create
)
app_name ="book"
urlpatterns = [
    path("uni/",book_data, name="book_uni"),
    path("report/create/",report_create,name="report_create")
]
