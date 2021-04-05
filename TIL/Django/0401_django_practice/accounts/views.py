from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm,
)
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)

def profile(request, username):
    # 1. 현재 요청을 보낸 유저가 보고자 하는 유저를 가져온다.
    User = get_user_model()

    profile_user = User.objects.get(username = username)
    # 2. 그 사람에 대한 정보를 추출하기
    context ={
        'profile_user': profile_user,
    }
    print(request.user)
    print(profile_user)
    print(type(profile_user))
    print(profile_user.username) # 113번 줄이랑 뭐가 다르지?
    print(type(profile_user.username)) # 아, 113번은  class이고, 115는 str이다.
    print(type(request.user))
    return render(request, 'accounts/profile.html',context)



# def follow(request, user_pk):
#     # User 직접 참조하지 않기
#     User = get_user_model()
#     f_user = get_object_or_404(User,pk=user_pk)
#     # 만약에 f_user가 User.following 에 있다면...없다면...으로 구분
    
#     if f_user.followers.filter(pk=request.user.pk):
#         f_user.followers.remove(f_user)
#     else:
#         f_user.followers.add(f_user)

#     # 이렇게 하면 typeError :argument of type 'ManyRelatedManager' is not iterable
#     # filter 씌워서 쓰면 해결이 되긴하는데..
#     # if f_user not in ff_user.following:
#     #     ff_user.following.add(f_user)
#     # else:
#     #     ff_user.following.remove(f_user)

    
#     return redirect('accounts:profile', f_user.username)

def follow(request,pk):
    User = get_user_model()
    you = User.objects.get(pk=pk) # 요청을 받는 너
    me = request.user # 요청을 보내는 나


    if you.followers.filter(pk=me.pk).exists():
        you.followers.remove(me)
    else:
        you.followers.add(me)
    return redirect('accounts:profile', you.username)


# 해쉬 태그... M:N 테이블로 구현이 가능하다고?