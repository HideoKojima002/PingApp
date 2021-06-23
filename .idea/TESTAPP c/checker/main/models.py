from django.db import models
from django.db import connection
from pythonping import ping


class django_Pings(models.Model):
    idping = models.BigAutoField(primary_key=True)
    Hosts = models.CharField(max_length=40)
    Pings = models.CharField(max_length=100)
    Data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Hosts, self.Pings, self.Data


def pingers():
    Response_List = ping('google.com', timeout=60, count=2, interval=1, verbose=True, df=True)
    return Response_List._responses


with connection.cursor() as cursor:
    cursor.execute('INSERT INTO django_pings.main_django_pings (Pings) VALUES (Response_List)')
