from django.contrib import admin

from .models import City, Message, Prioritet, SobesTime, Zapros


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'cities'
    )
    list_editable = ('cities', )
    search_fields = ('text', )
    empty_value_display = '-пусто-'


admin.site.register(Zapros)
admin.site.register(Prioritet)
admin.site.register(City)
admin.site.register(SobesTime)
admin.site.register(Message, MessageAdmin)
