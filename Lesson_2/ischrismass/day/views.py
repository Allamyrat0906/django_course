
from django.shortcuts import render
import datetime


def isnewyear(request):
    now = datetime.datetime.now()
    isnewyear = (now.month == 1 and now.day == 1)
    return render(request, "index.html", {
        "isnewyear": isnewyear
    })
