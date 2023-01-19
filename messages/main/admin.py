from django.contrib import admin

from .models import (City, InterviewTime, Message, Priority, SampleResponse,
                     SampleStraight, Zapros)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'cities'
    )
    list_editable = ('cities', )
    search_fields = ('text', )
    empty_value_display = '-пусто-'


@admin.register(InterviewTime)
class InterviewTimeAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'get_cities'
    )

    def get_cities(self, obj):
        return " | ".join([str(City) for City in obj.cities.all()])


admin.site.register(Zapros)
admin.site.register(Priority)
admin.site.register(City)
admin.site.register(SampleResponse)
admin.site.register(SampleStraight)
