from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    # http://localhost:8000/dinner
    # dinner는 인자를 2개 받는데, 여기서는 하나만 받는 경우가 있다.
    # 그럴때, 함수에 기본값을 설정해주면 좋다.
    path('<str:menu>/',views.dinner),
    # http://localhost:8000/dinner/저녁메뉴/인원수/
    # .../dinner/샐러드/10/ .. 이런식으로 전개
    path('<str:menu>/<int:people>/',views.dinner,name='dinner'),
]
