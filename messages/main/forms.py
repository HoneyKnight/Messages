from django import forms
from django.forms import SelectDateWidget

from .models import Message, SampleResponse, SampleStraight, Zapros, MessageOffice


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('weektime', 'hourtime', 'number')
        label = {
            'weektime': 'Выберите дату',
            'hourtime': 'Выберите время',
            'number': 'Вставьте номер кандидата',
        }
        widgets = {'weektime': SelectDateWidget()}


class MessageOfficeForm(forms.ModelForm):
    class Meta:
        model = MessageOffice
        fields = ('weektime', 'hourtime', 'number')
        label = {
            'weektime': 'Выберите дату',
            'hourtime': 'Выберите время',
            'number': 'Вставьте номер кандидата',
        }
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


class SampleResponseForm(forms.ModelForm):
    class Meta:
        model = SampleResponse
        fields = ('number',)
        label = {'number': 'Вставьте номер телефона'}


class SampleStraightForm(forms.ModelForm):
    class Meta:
        model = SampleStraight
        fields = ('name', 'number')
        label = {
            'name': 'Введите своё имя',
            'number': 'Вставьте номер кандидата',
        }
