from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # http://localhost:8000/signup/
    path('signup/', views.signup, name='signup'),

    #http://localhost:8000/result/
    path('result/',views.result, name ='result'),
]
