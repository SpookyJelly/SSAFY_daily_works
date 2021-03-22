from django.urls import path
from . import views

app_name ='accounts'
urlpatterns = [
    #Login
    # 절대 경로 http://localhost:8000/accounts/login/
    path('',views.index,name='index'),

    path('login/',views.login,name='login'),

    #Logout
    path('logout/',views.logout,name='logout'),

    #Signup
    path('signup/',views.signup,name='signup'),

    #delete (회원 탈퇴)
    path('delete/',views.delete, name='delete'),

    #Update(회원정보수정)
    path('update/',views.update,name='update'),
]
