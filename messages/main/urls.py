from django.urls import path

from . import views

app_name = 'main'


urlpatterns = [
    path('', views.index, name='index'),
    path('cities/<slug:slug>/', views.message, name='messages'),
    path(
        'messages/<int:message_id>/edit/',
        views.message_edit,
        name='message_edit'
    ),
    path('priority/', views.priority, name='priority'),
    path('demand/', views.demand, name='demand'),
    path(
        'demand/<int:demand_id>/edit/', views.demand_edit, name='demand_edit'
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
