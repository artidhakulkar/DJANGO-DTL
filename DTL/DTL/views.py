import datetime

from django.http import HttpResponse
from django.shortcuts import render


def variable(request):
    params = {"today": datetime.datetime.now()}
    return render(request, "index.html", params)


def conditions(request):
    params = {"today": datetime.datetime.now()}
    return render(request, "conditions.html", params)

def loop(request):
    v=['sun','mon','tues','wed','thus','fri','sat', 'sun']
    params = {"days_of_weak": v}

    return render(request, "loop.html", params)