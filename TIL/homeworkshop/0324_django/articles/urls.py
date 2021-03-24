from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    # comment url은 실제 댓글을 올릴때 필요한 주소와 함수이다.
    path('<int:article_pk>/comments/',views.comments, name='comments'),
    path('<int:article_pk>/comments/<int:pk>/delete/',views.comment_delete,name='comment_delete'),
]
