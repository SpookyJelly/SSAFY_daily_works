from django.urls import path
from . import views

urlpatterns = [
    # 첫번째 인자로 들어가는것은 사용자가 요청하는 위치
    # http://127.0.0.1:8000/articles/ <-- 이게 기본으로 딸려온다

    path('', views.index),

    # variable routing
    # http://127.0.0.1:8000/articles/<데이터 타입면 
    path('<int:article_id>/', views.detail),

    # 게시글 작성 기능 구현하기
    # 1. 사용자가 장고 서버로 게시글 작성 페이지 요청
    # 2. 장고가 사용자에게 게시글 작성 페이지 응답
    # 3. 사용자가 장고 서버로 게시글 작성해서 요청 (==form 전달)
    # 4. 장고가 사용자로부터 게시글 정보 받아서, 다시 사용자에게 보여주기
    path('write/', views.write),
    path('save/',views.save),
]
