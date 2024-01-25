from django.shortcuts import render


months = {
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


def month(request):
    list_key = list(months.keys())
    # month_text = None
    # if name == "january":
    #     month_text = months["january"]
    # if name == "february":
    #     month_text = months["february"]
    # else:
    #     month_text = "this month not entered yet"
    return render(request, "month/index.html", {
        # "tasks": month_text,
        "list_m": list_key

    })
