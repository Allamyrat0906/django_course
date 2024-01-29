from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


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


def all_months(request):
    all_month = list(months_dict.keys())

    return render(request, "month/index.html", {
        "all_month": all_month

    })


def month_str(request, month):
    # month_text = None
    # if month == "january":
    #     month_text = months["january"]
    # if month == "february":
    #     month_text = months["february"]
    # else:
    #     return HttpResponseNotFound("This month does not exist")
    # return HttpResponse(month_text)
    try:
        month_all = months_dict[month]
        return HttpResponse(month_all)
    except:
        return HttpResponseNotFound("This month does not exist")


def month_number(request, month):
    all_months = list(months_dict.keys())

    if month > len(months_dict):
        return HttpResponseNotFound("invalid month")

    redir = all_months[month-1]
    redir_peth = reverse("monthly:month-challenges", args=[redir])

    return HttpResponseRedirect(redir_peth)
