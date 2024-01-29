from django.shortcuts import render

# Create your views here.


main_text = "Example Domain"
text = """This domain is for use in illustrative 
examples in documents. You may use
 this domain in literature without prior coordination or asking for permission."""


def index(request):
    return render(request, "example.html", {
        "main_text": main_text,
        "text": text
    })
