from django.db.models.functions import Length
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page

from .forms import (MessageForm, SampleResponseForm, SampleStraightForm,
                    DemandForm)
from .models import (City, Message, Priority, SampleResponse, SampleStraight,
                     Demand)


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


def message(request, slug):
    city = get_object_or_404(City, slug=slug)
    message = city.messages.select_related('hourtime')
    context = {
        'city': city,
        'message': message,
    }
    return render(request, 'main/city.html', context)


def demand(request):
    demand = Demand.objects.all()
    context = {
        'demand': demand,
    }
    return render(request, 'main/demand.html', context)


@cache_page(20, key_prefix='priority_page')
def priority(request):
    priority = Priority.objects.all()
    context = {
        'priority': priority
    }
    return render(request, 'main/priority.html', context)


def message_edit(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    form = MessageForm(
        message.city,
        request.POST or None,
        instance=message,
    )
    if not form.is_valid():
        context = {
            'messages': message,
            'form': form,
        }
        return render(request, 'main/edit_message.html', context)
    form.save()
    return redirect(f'/cities/{message.city.slug}/')


def demand_edit(request, demand_id):
    demand = get_object_or_404(Demand, id=demand_id)
    form = DemandForm(
        request.POST or None,
        instance=demand,
    )
    if not form.is_valid():
        context = {
            'demand': demand,
            'form': form,
        }
        return render(request, 'main/edit_message.html', context)
    form.save()
    return redirect('/demand/')


def sample_edit(request, sampleresponse_id):
    sampleresponse = get_object_or_404(SampleResponse, id=sampleresponse_id)
    form = SampleResponseForm(
        request.POST or None,
        instance=sampleresponse,
    )
    if not form.is_valid():
        context = {
            'sampleresponse': sampleresponse,
            'form': form,
        }
        return render(request, 'main/edit_message.html', context)
    form.save()
    return redirect('/sample/')


def samplestraight_edit(request, samplestraight_id):
    samplestraight = get_object_or_404(SampleStraight, id=samplestraight_id)
    form = SampleStraightForm(
        request.POST or None,
        instance=samplestraight,
    )
    if not form.is_valid():
        context = {
            'samplestraight': samplestraight,
            'form': form,
        }
        return render(request, 'main/edit_message.html', context)
    form.save()
    return redirect('/sample/')
