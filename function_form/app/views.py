from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest


# Create your views here.
def hub_page(request: HttpRequest) -> render:
    print(request.GET)
    return render(request, "index.html")


def Hey_You(request: HttpRequest):
    if request.GET:
        input_name = str(request.GET["input_name"])
        return render(request, "Hey.html", {"input_name": input_name})
    else:
        return render(request, "Hey.html")


def Age_in_2050(request: HttpRequest):
    if request.GET:
        birthyear = int(request.GET["birthyear"])
        ageyear = int(request.GET["ageyear"])
        answer = ageyear -birthyear
        return render(request, "Age.html", {"birthyear":birthyear, "ageyear":ageyear, "answer":answer})
    else:
        return render(request, "Age.html")


def Order(request: HttpRequest):
    return render(request, "Order.html")
