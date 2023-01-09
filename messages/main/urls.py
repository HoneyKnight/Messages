from django.urls import path

from . import views

app_name = 'main'


urlpatterns = [
    path('', views.index, name='index'),
    path('cities/<slug:slug>/', views.messages, name='messages'),
    path(
        'messages/<int:message_id>/edit/',
        views.message_edit,
        name='message_edit'
    ),
    path('priority/', views.priority, name='priority'),
    path('zapros/', views.zapros, name='zapros'),
    path('zapros/<int:zapros_id>/edit/', views.zapros_edit, name='zapros_edit')
]
