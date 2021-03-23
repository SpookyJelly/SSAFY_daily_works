from django.shortcuts import render,redirect
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib import messages

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.
def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save() # DB에 생성된 유저 객체 반환. 마치 article 을 Article 폼으로 만들었을때, article이 반환되는것 처럼...
            # UserCreationForm은 User를 만드는 Form이다 보니까, 반환으로 유저 객체를 반환하다.
            # 그리고 save()를 찾아올라가서 보니까 UserCreation의 기능으로 있는데, user 객체를 return하게 되어있다.
            # save는 그냥 폼에 존재하지 않는다. 모델 폼에만 존재.
            auth_login(request,user)
            # 회원 가입 축하 메세지를 
            # request 객체에 담아서 같이 보냅니다.
            messages.add_message(request, messages.SUCCESS, '회원가입을 축하합니다!')
            return redirect("articles:index")

    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html',context)

def login(request):
    if request.method =="POST":
        form = AuthenticationForm(request,request.POST) # 얘는 그냥 form이다.
        if form.is_valid():
            # 세션 생성 (==로그인)
            # 1. DB에 세션을 생성
            # 2. request 객체에 session 정보가 생성
            # => request.session을 이제부터 사용 가능.
            auth_login(request,form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context ={
        'form':form,
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    #request.session을 직접 삭제도 할 수 있다.
    auth_logout(request)
    # 세션삭제
    # 1. DB에 있는 세션 삭제
    # 2. request 객체에 담긴 session 삭제
    return redirect('articles:index')

def update(request):
    from .forms import CustomUserChangeForm
    if request.method =="POST":
        form = CustomUserChangeForm(request.POST,instance=request.user) # 우리가 지금 요청하는 유저의 정보는 request 안에 있다
        # request.POST로만 채워준다
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:        
        form = CustomUserChangeForm(instance= request.user)
    
    context = {
        'form':form,
    }
    return render(request,'accounts/update.html',context)

def password_update(request):
    from django.contrib.auth import update_session_auth_hash
    if request.method =="POST":
        form = PasswordChangeForm(
            user=request.user,data=request.POST
        ) # 근데 둘다 키워드는 생략 가능 / 지금은 그냥 명시적으로 표기
        if form.is_valid():
            form.save() # 이 시점에서 비밀번호가 변경
            # update_session_auth_hash(request,form.user)
            return redirect('articles:index')

    form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request,'accounts/password_update.html',context)