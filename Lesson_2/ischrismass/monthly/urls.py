from django.urls import path
from . import views


urlpatterns = [
    path("", views.month)
    # path("<str:name>", views.month)

]
