from tokenize import Number
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def odd(request, _number):
    context = {
        "number": _number,
    }
    return render(request, "odd.html", context)


def calculation(request, a, b):
    context = {
        "num_a": a,
        "num_b": b,
    }
    return render(request, "calculation.html", context)
