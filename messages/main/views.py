from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page

from .forms import (MessageForm, SampleResponseForm, SampleStraightForm,
                    ZaprosForm, MessageOfficeForm)
from .models import (City, Message, MessageOffice, Priority, SampleResponse,
                     SampleStraight, Zapros)


@cache_page(20, key_prefix='index_page')
@login_required
def index(request):
    cities = City.objects.all()
    context = {
        'cities': cities,
    }
    return render(request, 'main/index.html', context)


@login_required
def sample(request):
    sampleresponse = SampleResponse.objects.all()
    samplestraight = SampleStraight.objects.all()
    context = {
        'sampleresponse': sampleresponse,
        'samplestraight': samplestraight,
    }
    return render(request, 'main/sample.html', context)


@login_required
def messages(request, slug):
    cities = get_object_or_404(City, slug=slug)
    messages = Message.objects.filter(cities=cities)
    messages_office = MessageOffice.objects.filter(cities=cities)
    context = {
        'cities': cities,
        'messages': messages,
        'messages_office': messages_office,
    }
    return render(request, 'main/city.html', context)


@login_required
def zapros(request):
    zapros = Zapros.objects.all()
    context = {
        'zapros': zapros,
    }
    return render(request, 'main/zapros.html', context)


@cache_page(20, key_prefix='priority_page')
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
def messages_office_edit(request, messages_office_id):
    messages_office = get_object_or_404(MessageOffice, id=messages_office_id)
    form = MessageOfficeForm(
        request.POST or None,
        instance=messages_office,
    )
    if not form.is_valid():
        return render(request, 'main/edit_message.html', {
            'messages_office': messages_office,
            'form': form,
        })
    form.save()
    return redirect(f'/cities/{messages_office.cities.slug}/')


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


@login_required
def sample_edit(request, sampleresponse_id):
    sampleresponse = get_object_or_404(SampleResponse, id=sampleresponse_id)
    form = SampleResponseForm(
        request.POST or None,
        instance=sampleresponse,
    )
    if not form.is_valid():
        return render(request, 'main/edit_message.html', {
            'sampleresponse': sampleresponse,
            'form': form,
        })
    form.save()
    return redirect('/sample/')


@login_required
def samplestraight_edit(request, samplestraight_id):
    samplestraight = get_object_or_404(SampleStraight, id=samplestraight_id)
    form = SampleStraightForm(
        request.POST or None,
        instance=samplestraight,
    )
    if not form.is_valid():
        return render(request, 'main/edit_message.html', {
            'samplestraight': samplestraight,
            'form': form,
        })
    form.save()
    return redirect('/sample/')
