from django.urls import path
from . import views


urlpatterns = [
    path("profiles/", views.CreateProfilesViews.as_view(), name="create_profiles")
]
