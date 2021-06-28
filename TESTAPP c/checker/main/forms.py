from .models import django_Pings
from django.forms import ModelForm, TextInput


class django_PingsForm(ModelForm):
    class Meta:
        model = django_Pings
        fields = ["Hosts"]
        widgets = {
            "Hosts": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя хоста через кавычки',
            }),
        }