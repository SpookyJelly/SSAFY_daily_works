from django.urls import path
from . import views

app_name = 'lottos'
urlpatterns = [
    path('', views.index,name='index'),
]