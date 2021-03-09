from django.urls import path
from . import views


app_name = 'articles' # url name을 구분해 주기 위한 prefix

urlpatterns =[
    
    #http://localhost:8000/articles/
    # name 이라는 3번째 parameter로 별명을 지어줄 수 있다.
    path('', views.index, name='index'),
]