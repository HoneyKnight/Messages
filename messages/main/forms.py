from django import forms
from django.forms import SelectDateWidget

from .models import (InterviewTime, Message, SampleResponse, SampleStraight,
                     Zapros)


class MessageForm(forms.ModelForm):
    hourtime = forms.ModelChoiceField(
        queryset=InterviewTime.objects.all(),
        label='Время собеседования',
        help_text='Выберите время собеседования'
    )
    def __init__(self, cities, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['hourtime'].queryset = InterviewTime.objects.filter(cities=cities)
    class Meta:
        model = Message
        fields = ('weektime', 'hourtime', 'number')
        label = {
            'weektime': 'Выберите дату',
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
