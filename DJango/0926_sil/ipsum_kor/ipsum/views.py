from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "index.html")


def text(request):
    return render(request, "text.html")


def result(request):
    word_list = ["소", "돼지", "개", "말"]
    paragraph = int(request.GET.get("paragraph"))
    word = int(request.GET.get("word"))
    lorem_para = []

    string = ""
    for _ in range(word):
        string += random.choice(word_list) + " "
    return render(request, "ipsum/resuelt.html")
