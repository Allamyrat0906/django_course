from django.urls import path
from . import views


urlpatterns = [
    path("profiles/", views.CreateProfileView.as_view(), name="create_profiles"),
    path("user_profile/", views.UserProfileView.as_view(), name="user_profile"),
]
