from django.shortcuts import render, redirect
from pythonping import ping
import datetime
from .models import django_Pings


def index(request):
    return render(request, 'main/base.html')


def start(request):
    return render(request, 'main/start.html')


def your(request):
    now = datetime.datetime.now()
    return "Date: " + now.strftime("%Y-%m-%d")


def pingers(request):
    host = 'google.com'
    try:
        Response_List = ping(host, timeout=60, count=2, interval=1, verbose=True, df=True)
        Response_List = Response_List._responses
        for item in Response_List:
            django_Pings.objects.create(
                Hosts=host,
                Pings=item.time_elapsed_ms,
            )
    except RuntimeError:
        Response_List = []
    return redirect('landing')


def landing(request):
    pings = django_Pings.objects.all()
    return render(request, 'main/landing.html', context={'pings': pings})

