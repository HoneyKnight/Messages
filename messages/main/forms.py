from django import forms
from django.forms import SelectDateWidget

from .models import Message, Zapros


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('weektime', 'hourtime')
        label = {'weektime': 'Выберите дату', 'hourtime': 'Выберите время'}
        widgets = {'weektime': SelectDateWidget()}


class ZaprosForm(forms.ModelForm):
    class Meta:
        model = Zapros
        fields = ('town', 'name', 'number', 'baza')
        label = {
            'town': 'Введите город',
            'name': 'Введите имя',
            'number': 'Введите номер',
            'baza': 'Вставьте ссылку на кандидата'
        }
