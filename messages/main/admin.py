from django.contrib import admin

from .models import (City, InterviewTime, InterviewTimeOffice, Message,
                     MessageOffice, Priority, SampleResponse, SampleStraight,
                     Zapros)


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'cities'
    )
    list_editable = ('cities', )
    search_fields = ('text', )
    empty_value_display = '-пусто-'


class MessageOfficeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'cities'
    )
    list_editable = ('cities', )
    search_fields = ('text', )
    empty_value_display = '-пусто-'


admin.site.register(Zapros)
admin.site.register(Priority)
admin.site.register(City)
admin.site.register(InterviewTime)
admin.site.register(Message, MessageAdmin)
admin.site.register(SampleResponse)
admin.site.register(SampleStraight)
admin.site.register(MessageOffice, MessageOfficeAdmin)
admin.site.register(InterviewTimeOffice)
