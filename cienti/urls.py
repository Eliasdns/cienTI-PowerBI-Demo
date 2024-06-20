from django.urls import path
from . import views


app_name = 'cienti'

urlpatterns = [
    path('', views.VotoCreate.as_view(), name='voto_create'),
]
