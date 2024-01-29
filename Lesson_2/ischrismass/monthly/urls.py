from django.urls import path
from . import views


app_name = "monthly"
urlpatterns = [
    path("month", views.all_months),
    path("<int:month>", views.month_number, ),
    path("<str:month>", views.month_str, name="month-challenges"),


]
