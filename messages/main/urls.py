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
    path(
        'messages/office/<int:messages_office_id>/edit/',
        views.messages_office_edit,
        name='message_office_edit'
    ),
    path('priority/', views.priority, name='priority'),
    path('zapros/', views.zapros, name='zapros'),
    path(
        'zapros/<int:zapros_id>/edit/', views.zapros_edit, name='zapros_edit'
    ),
    path('sample/', views.sample, name='sample'),
    path(
        'sample/response/<int:sampleresponse_id>/edit/',
        views.sample_edit,
        name='sample_edit'
    ),
    path(
        'sample/straight/<int:samplestraight_id>/edit/',
        views.samplestraight_edit,
        name='samplestraight_edit'
    ),
]
