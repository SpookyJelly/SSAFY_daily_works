"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from . import views 하면 왜 에러나지??
# 동일한 경로에 없어서 그런거 같은데...(intro와 pages가 같은 레벨에 있다는 말)
# 라이브 수업시간에는 그냥 . 찍어도 되지 않았나??
from pages import views

# 1단계 url 매핑 
# 중요한 포인트는 views.py를 내가 생성한 pages 라는 app에서 import 해야한다는 점 
urlpatterns = [
    path('pages/', views.lottos),
    path('admin/', admin.site.urls),
]
