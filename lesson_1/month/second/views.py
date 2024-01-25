from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def secondapp(request):
    return HttpResponse("Sexond app new")