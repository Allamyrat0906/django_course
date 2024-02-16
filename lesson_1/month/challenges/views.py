from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# def index(request):
#     return HttpResponse("this is first request")

lists = [1, 2, 3, 4, 5]


def showtemplates(request):

    return render(request, "challenges/challenge.html",
                  {
                      "lists": lists
                  })
