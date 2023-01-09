from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import MessageForm, ZaprosForm
from .models import City, Message, Priority, Zapros
from django.views.decorators.cache import cache_page


@login_required
@cache_page(20, key_prefix='index_page')
def index(request):
    cities = City.objects.all()
    context = {
        'cities': cities,
    }
    return render(request, 'main/index.html', context)


@login_required
def messages(request, slug):
    cities = get_object_or_404(City, slug=slug)
    messages = Message.objects.filter(cities=cities)
    context = {
        'cities': cities,
        'messages': messages,
    }
    return render(request, 'main/city.html', context)


@login_required
def zapros(request):
    zapros = Zapros.objects.all()
    context = {
        'zapros': zapros,
    }
    return render(request, 'main/zapros.html', context)


@login_required
def priority(request):
    priority = Priority.objects.all()
    context = {
        'priority': priority
    }
    return render(request, 'main/priority.html', context)


@login_required
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


@login_required
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
