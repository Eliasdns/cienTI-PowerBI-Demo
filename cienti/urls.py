from django.urls import path
from . import views


app_name = 'cienti'

urlpatterns = [
    path('', views.index, name='index'),
]
