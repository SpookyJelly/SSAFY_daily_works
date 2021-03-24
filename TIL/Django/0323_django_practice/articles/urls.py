from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),

    # 댓글 저장
    # http://localhost:8000/articles/몇번째 게시글 / create/ comments
    path('<int:article_pk>/comments/', views.create_comment,name='create_comment')

]
