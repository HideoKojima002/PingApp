from django.db import models



class django_Pings(models.Model):
    Hosts = models.CharField(max_length=40)
    Pings = models.CharField(max_length=100)
    Data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Hosts, self.Pings, self.Data



