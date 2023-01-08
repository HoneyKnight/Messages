from django.shortcuts import get_object_or_404, redirect, render

from .forms import MessageForm, ZaprosForm
from .models import City, Message, Prioritet, Zapros


def index(request):
    cities = City.objects.all()
    context = {
        'cities': cities,
    }
    return render(request, 'main/index.html', context)


def messages(request, slug):
    cities = get_object_or_404(City, slug=slug)
    messages = Message.objects.filter(cities=cities)
    context = {
        'cities': cities,
        'messages': messages,
    }
    return render(request, 'main/city.html', context)


def zapros(request):
    zapros = Zapros.objects.all()
    context = {
        'zapros': zapros,
    }
    return render(request, 'main/zapros.html', context)


def prioritet(request):
    spisok = Prioritet.objects.all()
    context = {
        'spisok': spisok
    }
    return render(request, 'main/prioritet.html', context)


def message_edit(request, message_id):
    messages = get_object_or_404(Message, id=message_id)
    form = MessageForm(
        request.POST or None,
        instance=messages,
    )
    if not form.is_valid():
        return render(request, 'main/edit_message.html', {
            'messages': messages,
            'form': form,
        })
    form.save()
    return redirect(f'/cities/{messages.cities.slug}/')


def zapros_edit(request, zapros_id):
    zapros = get_object_or_404(Zapros, id=zapros_id)
    form = ZaprosForm(
        request.POST or None,
        instance=zapros,
    )
    if not form.is_valid():
        return render(request, 'main/edit_message.html', {
            'zapros': zapros,
            'form': form,
        })
    form.save()
    return redirect('/zapros/')
