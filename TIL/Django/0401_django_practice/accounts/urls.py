from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),

    # 프로필
    path('<str:username>/', views.profile, name='profile'),

    # 팔로우/언팔로우 < --  모델 수정이 필요한거 같은데.
    # 팔로우 url에는 username을 사용하지 마라??? ->RESTful이라는 약속때문에 그렇다.
    # 주소에 게시글 제목을 넣는건 slug
    path('<int:pk>/follow',views.follow, name='follow'),

]
