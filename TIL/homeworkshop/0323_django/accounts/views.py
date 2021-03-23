from django.shortcuts import render,redirect

from django.views.decorators.http import require_http_methods,require_safe

from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm,
    )
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# 내가 만든거
from .forms import (
    CustomUserChangeForm,
    CustomAutheticationForm,
    CustomUserCreationForm,
    )
# Create your views here.
def index(request):
    return render(request,'accounts/index.html')

# 회원가입
@require_http_methods(['GET','POST'])
def signup(request):
    if request.method =="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            messages.add_message(request, messages.SUCCESS, '회원가입을 축하합니다!')
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    
    context ={
        'form':form,
    }
    return render(request,'accounts/signup.html',context)

@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

    # 그럼 request 채워서 왔을때는?
    if request.method =="POST":
        # args 위치에 request.POST가 오는데(위치 인자),이 상위 클래스까지 살펴보면 request는 상위 data에 바인딩 된다.
        # 그리고 request.POST는 request 객체가 아니라, request객체의 POST 속성이라고 해석해야하나?
        form = CustomAutheticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
            return redirect('accounts:index')
    # 이건 그냥 클릭했을때, 빈 폼 주는거
    else:
        form = CustomAutheticationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/login.html',context)

@login_required
@require_safe
def logout(request):
    # auth의 logout은 request만 받는다.
    auth_logout(request)
    return redirect('accounts:index')

@login_required
@require_http_methods(['POST'])
def delete(request):
    #세션이랑 계정을 지워야하니까
    #현재 활성화 중인 유저 모델을 가져와야지
    # 아니 유저를 가져오ㅑ아하나? <-- 유저를 가져오는 것이 맞다.\
    # TODO: 이건 DB 건드리는거니까, POST만 받도록할까? 근데 밖에서는 get으로 들어오잖아
    # 밖에서는 get이고 안에서는 POST로 처리하게 하는게 있었는데,..
    user = get_user(request)
    # 지금 user.delete() 만 쓰니까 위치 인수가 하나 더 필요하다고 한다.<-- get_user_model()로 잘못 사용해서 그럼
    user.delete()
    return redirect('accounts:index')

@login_required
@require_http_methods(['GET','POST'])
def update(request):
    # 일단 저장되어있는 양식을 가져와야지
    # UserChangeForm 사용 <-- Custom버젼 써야하는데 일단 이거부터 써보자
    
    # 지금 인스턴스로 회원 그 자체가 들어와야하잖아..
    # 일단 post 마저 업그레이드 하자.
    user = get_user(request) # 기존의 회원 정보 담고 있는 변수 / 이걸 전달해줘야지 원래 내 정보가 뭐였는지 알 수 있다.
    if request.method =="POST":
        # 여기서 request.POST는 'data' 키워드 인자이다. (최상위 클래스인, BaseModel에 근거하여)
        # 근데, 위치 인자상으로 data는 2번째에 오니까, 굳이 명시 안해줘도 되는거임.
        # 인스턴스는 저 뒤에 있으니까 키워드를 사용해서 넣어줘야하고 
        form = CustomUserChangeForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=user)
    
    context = {
        'form': form,
    }

    return render(request,'accounts/update.html',context)

@login_required
@require_http_methods(['GET','POST'])
def password(request):
    user = get_user(request)
    if request.method =='POST':
        form = PasswordChangeForm(user,request.POST) # *arg로 request.POST를 넣어줘야지 form이 갱신된다.
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, '비밀번호가 변경되었습니다. 다시 로그인 해주십시오.')
            return redirect('accounts:index')

    else:
        form = PasswordChangeForm(user)
    context ={
        'form':form
    }
    return render(request,'accounts/password.html',context)