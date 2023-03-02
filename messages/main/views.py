from django.db.models.functions import Length
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_page

from .forms import (MessageForm, SampleResponseForm, SampleStraightForm,
                    ZaprosForm)
from .models import (City, Message, Priority, SampleResponse, SampleStraight,
                     Zapros)
from .utils import form_edit


@cache_page(20, key_prefix='index_page')
def index(request):
    cities = City.objects.all().order_by(Length('description').asc())[::-1]
    context = {
        'cities': cities,
    }
    return render(request, 'main/index.html', context)


def sample(request):
    sampleresponse = SampleResponse.objects.all()
    samplestraight = SampleStraight.objects.all()
    context = {
        'sampleresponse': sampleresponse,
        'samplestraight': samplestraight,
    }
    return render(request, 'main/sample.html', context)


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


@cache_page(20, key_prefix='priority_page')
def priority(request):
    priority = Priority.objects.all()
    context = {
        'priority': priority
    }
    return render(request, 'main/priority.html', context)


def message_edit(request, message_id):
    messages = get_object_or_404(Message, id=message_id)
    form = MessageForm(
        messages.cities,
        request.POST or None,
        instance=messages,
    )
    return form_edit(
        request=request,
        model=messages,
        form=form,
        redirect_url=f'/cities/{messages.cities.slug}/'
    )


def zapros_edit(request, zapros_id):
    zapros = get_object_or_404(Zapros, id=zapros_id)
    form = ZaprosForm(
        request.POST or None,
        instance=zapros,
    )
    return form_edit(
        request=request,
        model=zapros,
        form=form,
        redirect_url='/zapros/'
    )


def sample_edit(request, sampleresponse_id):
    sampleresponse = get_object_or_404(SampleResponse, id=sampleresponse_id)
    form = SampleResponseForm(
        request.POST or None,
        instance=sampleresponse,
    )
    return form_edit(
        request=request,
        model=sampleresponse,
        form=form,
        redirect_url='/sample/'
    )


def samplestraight_edit(request, samplestraight_id):
    samplestraight = get_object_or_404(SampleStraight, id=samplestraight_id)
    form = SampleStraightForm(
        request.POST or None,
        instance=samplestraight,
    )
    return form_edit(
        request=request,
        model=samplestraight,
        form=form,
        redirect_url='/sample/'
    )
