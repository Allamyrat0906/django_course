from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.month_challenge_number, name="month-n-challenge"),
    path("<str:month>", views.month_challenge, name="month-challenge")
]
