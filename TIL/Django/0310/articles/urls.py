from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    #http://localhost:8000/articles/
    path('',views.index,name='index'),


    # 1. 글 작성 form 보여주는 주소
    path('new/',views.new,name='new'),
    
    # 2. form을 받아서 저장하는 주소
    path('write/',views.write,name='write'),
]
