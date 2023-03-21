from django.contrib import admin

from .models import (City, InterviewTime, Message, Priority, SampleResponse,
                     SampleStraight, Demand)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'city'
    )
    list_editable = ('city', )
    search_fields = ('text', )
    empty_value_display = '-пусто-'


@admin.register(InterviewTime)
class InterviewTimeAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'get_cities'
    )

    def get_cities(self, obj):
        return " | ".join([str(City) for City in obj.city.all()])


admin.site.register(Demand)
admin.site.register(Priority)
admin.site.register(City)
admin.site.register(SampleResponse)
admin.site.register(SampleStraight)
