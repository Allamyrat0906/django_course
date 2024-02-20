from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

months_dict = {
    "january": "eat  organic food",
    "february": "training more sport",
    "march": "get up early ",
    "april": "swimming  one hour each day",
    "may": "get spring seasons",
    "june ": "eat more food",
    "july": " watch tv",
    "august": "coding",
    "september": "resting",
    "october": " Returning",
    "november": " trying",
    "december": "finished"
}


def index(request):
    month_list = list(months_dict.keys())
    return render(request, "months/index.html", {
        "months": month_list
    })


def month_challenge_number(request, month):
    month_number = list(months_dict.keys())
    redirect_month = month_number[month-1]
    redirest_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirest_path)


def month_challenge(request, month):
    try:
        month_text = months_dict[month]
        return render(request, "months/challenge.html", {
            "month": month_text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("Could not find challenge")
