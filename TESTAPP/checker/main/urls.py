from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('start', views.start),
    path('landing', views.landing, name='landing'),
    path('pingers', views.pingers),
]
