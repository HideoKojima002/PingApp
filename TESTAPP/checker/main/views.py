import datetime
from django.shortcuts import render, redirect
from pythonping import ping
from .models import django_Pings
from .forms import django_PingsForm

def index(request):
    return render(request, 'main/base.html')


def start(request):
    return render(request, 'main/start.html')


def your(request):
    now = datetime.datetime.now()
    return "Date: " + now.strftime("%Y-%m-%d")


def pingers(request):
    if request.method == 'POST':
        form = django_PingsForm(request.POST)
        if form.is_valid():
            form.save()
    form = django_PingsForm()
    context = {
        "form": form
    }
    host = form
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
    pings = django_Pings.objects.order_by('-id')   #.all
    return render(request, 'main/landing.html', context={'pings': pings})

