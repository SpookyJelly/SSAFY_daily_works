from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # CREATE
    # 폼 보여주는거랑 DB 업데이트를 new하나가 동시에 !
    path('new/',views.new,name='new'),

    #READ
    path('',views.index,name='index'),
    path('<int:article_pk>/detail/',views.detail,name='detail'),
    #UPDATE
    # 변수 넣어주기 잊지말자. 우리는 pk번째 글을 위한 views와 url을 만드는거야
    path('<int:article_pk>/update/',views.update,name='update'),
    #DELETE
]
