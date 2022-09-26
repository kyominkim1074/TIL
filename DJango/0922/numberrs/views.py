from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def print_number(request, _number):
    context = {
        "number": _number,
    }
    return render(request, "number.html", context)


def print_text(request):
    text = request.GET.get("_text")
    context = {
        "template_text": text,
    }
    return render(request, "text.html", context)
