from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout # view 함수의 이름과 임포트하는 함수의 이름이 겹침 --> 둘 중 하나를 바꿔야한다.
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
# 쟝고가 미리 만들어 놓은 인증 폼 이걸 그냥 가져다 쓰는거 내장 폼을 사용하기 때문에 forms.py 를 안만들어오 되든ㄴ거
from .forms import CustomUserChangeForm

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        #로그인이 되어있다면 메인으로 리다이렉트
        return redirect('articles:index')

    if request.method=='POST':
        form = AuthenticationForm(request,request.POST)
        # form = AuthenticationForm(request,data = request.POST) // 명시적 작성
        # 모델 폼이 아닌 이유, 굳이 어떤 모델을 가져올 필요 가 없어서 모델폼은 파라미터로 데이터가 들어간다
        if form.is_valid():
            # 세션 CREATE
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next')or'articles:index') #request의 GET에 달려있는 키인 'next'의 밸류 주소로 보내주던가. 아니면 index로 보낸다
            # next의 주소 ?next=/articles/create/
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request,'accounts/login.html',context)

@require_POST
def logout(request):
    auth_logout(request) # 세션에 연결되어있는 데이터를 모두 삭제
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
        pass
    else:
        form = UserCreationForm()
    context={
        'form':form,
    }
    return render(request,'accounts/signup.html',context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context ={
        'form': form,
    }
    return render(request,'accounts/update.html',context)
