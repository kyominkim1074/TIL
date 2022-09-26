from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "index.html")


def name_(request):
    return render(request, "name.html")


def result_(request):
    life = request.GET.get("life")
    past = ["거지", "도둑", "왕", "마왕", "해적왕", "제독", "신"]
    random_past = random.choice(past)
    context = {
        "name": life,
        "random_life": random_past,
    }
    return render(request, "result.html", context)
