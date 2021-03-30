### 12_ Django_workshop

---

>Django Project 사전 제공되는 프로젝트를 사용해 아래 해당하는 조건을 모두 구현 하시오. 
>
>1) 대체한 User model을 사용한다.
>
> 2) 회원가입이 정상적으로 동작한다. 
>
>3) 메인 페이지에서 각 게시글의 작성자 정보가 출력된다. 
>
>4) 게시글 작성자 본인만 게시글을 수정 및 삭제할 수 있다. 
>
>5) 각 댓글에는 댓글 작성자 정보가 출력된다. 
>
>6) 댓글 작성자 본인만 댓글을 삭제할 수 있다.





#### * 구현 과정



#### 1) 대체한 User model을 사용한다.

---

* User model을 대체하려고 했으니, migrations 폴더에 이미 ```0001_inital.py``` 파일이 있어서, 해당 파일을 삭제하고 진행하였다. **0001_inital.py 삭제 **

1) accounts/model.py에 커스텀 유저 모델을 지정하자

```python
accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass

```



2) settings.py에 AUTH_USER_MODEL을 사용할 것임을 명시하자

```python
#settings.py

AUTH_USER_MODEL = 'accounts.User'

```



3) Models.py에서 User를 참조하는 모델이 있다면, settings.AUTH_USER_MODEL을 참조하도록 해주자.

-> 해당 없음 , 패스



4)admin page에서도 사용할 수 있게 등록

```python
# accounts/ admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
admin.site.register(User, UserAdmin)
```





#### 2) 회원가입이 정상적으로 동작한다.

---

* 현재 Views.py를 보면 UserCreationForm으로 유저를 생성하고 있다. 유저 모델이 바뀌었으니, 이 모델을 사용하면 에러가 나므로, 커스텀 시킨 다음 사용하자.

1)  forms.py에서 Custom 화

```python
# accounts/ views.py
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth import get_user_model
from django.conf import settings

## 중략 ##

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('username','email','first_name','last_name','password1','password2')
        # 쓸 데 없는 정보를 차단하고, 사용자에게 꼭 받아야하는 부분만 생성했다.

```



2) views.py 에서 UserCreationForm 대신 Custom한 Form 사용하도록 함

```python
# articles / views.py
# 전략
from .forms import (
    CustomUserChangeForm,
    CustomUserCreationForm,
    )
```



* 같은 방식으로 AuthecticationForm도 수정해주자



#### 3) 메인 페이지에서 각 게시글의 작성자 정보가 출력

---

* 게시글에 유저 정보를 출력하게 하려면, 게시글과 유저 모델간에 관계를 맺어야한다.

  유저 한명이 (1) 여러개의 게시글(N)을 작성할 수 있으니, 1:N 관계이다. 이 관계를 기본으로 Article 모델에 외래키를 부여하자.



1) articles/ models.py

```python
from django.db import models
from django.conf import settings
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 유저와의 외래키 관계를 형성해준다. 또한 모델에서 user를 참조할때는
    # settings을 import 하여 settings.AUTH_USER_MODEL을 참조하도록 한다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	
    def __str__(self):
        return self.title

```



2) articles/ views

외래키는 사용자가 직접 저장하는것이 아닌, 백엔드 영역에서 이루어져야한다.

따라서, .save()의 커밋 옵션을 이용하여 DB에 업데이트하기 전에, author 속성 값을 부여 해준다.

```python
@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False) 
            # commit 옵션으로 DB 업데이트전에 인스턴스만 받을 수 있다
            article.author = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```



3) index.html

마지막으로, 프론트 영역에 표시되도록 하면 된다.

```django
{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">[CREATE]</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요.]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>글쓴이 : {{ article.author }}</p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <p>글 내용 : {{ article.content }}</p>
    <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
    <hr>
  {% endfor %}
{% endblock %}

```





#### 4) 게시글 작성자 본인만 게시글을 수정 및 삭제할 수 있다.

---

* 크게 어렵지 않다. 수정하는 함수와 삭제하는 함수에 , 게시글에 저장되어있는 author 속성과 현재 request.user가 동일한지 확인하기만 하면 된다.



1) 삭제 

```python

@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.author: 
        article.delete()
    return redirect('articles:index')
```



2) 업데이트

```python
@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.author:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'form': form,
            'article': article,
        }
        return render(request, 'articles/update.html', context)
    else:
        return redirect('articles:index')
```





#### 5) 각 댓글에는 댓글 작성자 정보가 출력된다.

---

1) 댓글 모델도 유저와 관계를 맺을 수 있도록 외래 키를 설정해준다.

```python
# articles/ models.py
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.content
```



2) views에서 commit 옵션을 이용하여 author 속성을 부여해준다

```python
@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.author = request.user # 현재 글을 작성하는 유저 정보를 author 필드를 채움
            comment.save()
            return redirect('articles:detail', article.pk)
        context = {
            'comment_form': comment_form,
            'article': article,
        }
        return render(request, 'articles/detail.html', context)
    return redirect('accounts:login')
```



3) 프론트 영역에서 수정해준다.

```django
  # 전략 #
<p>글쓴이 : {{ article.author }}</p>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성시각 : {{ article.created_at }}</p>
  <p>수정시각 : {{ article.updated_at }}</p>

# 후략 #
```





#### 6) 댓글 작성자 본인만 댓글을 삭제할 수 있다.

---

* 게시글 때와 동일한 요령으로 접근한다. 현재 사용자가 게시글에 저장된 유저 정보와 일치할 때만 삭제할 수 있게 한다.

```python
@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user== comment.author:
        comment.delete()
    return redirect('articles:detail', article_pk)
```

