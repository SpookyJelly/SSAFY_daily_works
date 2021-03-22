from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model

from .forms import CustomUserChangeForm
# Create your views here.

def index(request):
    User = get_user_model()
    users = User.objects.all()
    context ={
        'users':users,
    }
    return render(request,'accounts/index.html',context)




def login(request):

    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            # 이 시점에서 로그인 == 세션 생성
            # 첫번째 인자에 요청 정보 (request)
            # 두번째 인자에 유저 객체를 넣어야한다.
            auth_login(request,form.get_user())
            return redirect('articles:index')
    else:
        # GET
        form = AuthenticationForm()

    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)
@require_POST
def logout(request):
    # 로그아웃 == 세션을 삭제합니다.
    # request에는 현재 로그인 된 유저의 요청정보만 담겨있다. -> 다른 사람은 전혀 고려하지 않는다.
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # 데이터 베이스에 회원 정보 생성
            auth_login(request, user) # 세션 생성 == 로그인
            return redirect('articles:index')
    #GET
    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html',context)

@require_POST
def delete(request):
    # request.user == 여기까지가 현재 로그인 된 유저 객체
    # is_staff,is_active, is_authenticated,last_login
    
    # 진짜 삭제
    request.user.delete()

    # 계정만 비활성화 시키는 경우
    # request.user.is_active = False
    # request.user.save

    return redirect('articles:index')

def update(request):
    if request.method =='POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form':form,
    }
    return render(request,'accounts/update.html',context)