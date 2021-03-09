from django.urls import path
from . import views

app_name = 'pages' # url name을 구분해 주기 위한 prefix
urlpatterns = [
    #http://localhost:8000/pages/
    # 자꾸 index라고 하는데, 관습적으로 메인페이지를 index라고 한다
    path('',views.index,name = 'index'),
]
