from django.shortcuts import render
from pythonping import ping
import datetime
from . import models
# from django.http import HttpResponse


def index(request):
    return render(request, 'main/base.html')


def start(request):
    return render(request, 'main/start.html')


def your(request):
    now = datetime.datetime.now()
    return "Date: " + now.strftime("%Y-%m-%d")


# def pingers(request):
#     Response_List = ping('google.com', timeout=60, count=2, interval=1, verbose=True, df=True)
#     Response_List+=Response_List._responses
#     return Response_List

def landing(request):
    pings = models.django_Pings.objects.all()
    return render(request, 'main/landing.html', locals())

