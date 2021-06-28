from django.db import models
from django.db import connection
from pythonping import ping


class django_Pings(models.Model):
    Hosts = models.CharField(max_length=40)
    Pings = models.CharField(max_length=100)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Hosts, self.Pings, self.Date


def pingers():
    Response_List = ping('google.com', timeout=60, count=2, interval=1, verbose=True, df=True)
    return Response_List._responses

