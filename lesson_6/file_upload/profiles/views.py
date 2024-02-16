from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from profiles.form import ProfilesForm
from profiles.models import UserModel
# Create your views here.


class CreateProfilesViews(View):
    def get(self, request):
        form = ProfilesForm()
        return render(request, "profiles/create_profile.html", {
            "form": form
        })

    def post(self, request):
        sumbit_form = ProfilesForm(request.POST, request.FILES)
        if sumbit_form.is_valid():
            profile = UserModel(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/profiles")
        return render(request, "profiles/create_profile.html", {
            "submit_form": sumbit_form
        })
