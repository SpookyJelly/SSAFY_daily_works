### 15_django_homework

---

#### 1. MTV

>Django는 MTV로 이루어진 Web Framework다. MTV가 무엇의 약자이며 Django에서 각각 어떤 역할을 하고 있는지 작성하시오.

Model : 데이터의 구조를 잡아줌

Templates: 화면에 어떻게 띄워줄지를 결정한다.

View: 내부적으로 어떻게 동작을 하는지를 결정



#### 2. 404 Page not found

>기본적으로 ‘/ ’ 페이지에 접속하게 되면 아래 사진처럼 Page not found 에러가 발생한다.  ‘/ ’ 페이지에 접속했을 때 index.html를 렌더링 하고자 한다. 아래 빈칸에 알맞은 코드를 작성하시오. (프로젝트의 이름은 crud 이며 app 이름은 articles이다. index.html 파일을 렌더링 하는 view 함수의 이름은 index라고 가정한다.)



```
from django.contrib import admin
from django.urls import path, include
from articles import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('articles/', include('articles.urls')),
	path('', views.index)
]
```



* a :articles

* b: views

* c: views.index





#### 3. templates and static

>Django 프로젝트는 기본적으로 render 할 html과 같은 template 파일과 css, js와 같은 static 파일을 앱 폴더 내부의 templates와 static 이름의 폴더에서 찾는다.  만약 해당 위치가 아닌 임의의 위치에 파일을 위치 시키고 싶으면 __(a)__ 파일의 __(b)__ 와 __(c)__ 라는 변수에 담긴 리스트의 요소를 정의하면 된다.  빈칸 (a), (b), (c)에 들어갈 내용을 작성하시오. 



a: settings.py

b: STATIC_ROOT

c: STATICFILES_DIRS







#### 4. migration

> 아래는 그림과 같이 Django에서 선언한 Model을 Database에 반영하는 과정에서 사용하는 명령어에 대한 설명이다. 각 설명에 해당하는 명령어를 작성하시오.  (app 이름은 articles이다.)



1) python manage.py makemigrations articles

2) python manage.py showmigrations articles

3) python manage.py  sqlmigrate articles # + migration name 도 붙을 수 있다.

4) python manage.py migrate articles



* 뒤에 앱 이름을 안 붙이면 모든 앱에 대해 실행된다.



### 5. ModelForm True or False

> 각 문항을 읽고 맞으면 T, 틀리면 F를 작성하시오.

1) T : 데이터가 어디에 담기느냐의 차이지, 동작 방식은 동일하다

2) T : 우리가 자주 사용하던 User_auth 관련 form들은 model이 User 인것을 알고 있었기에, 별도의 커스터마이징 없이도 바로 사용할 수 있었다. 또한 그렇기 때문에, User model이 변경되면 다시 한번 모델을 지정해줬어야하는 것이다.

3) T : 상동

4) T : 반드시 작성해야한다. 안그러면 에러난다!





#### 6. media 파일 경로

> 사용자가 업로드한 파일이 저장되는 위치를 Django 프로젝트 폴더 (crud) 내부의 /uploaded_files 폴더로 지정하고자 한다. 이 때, settings.py에 작성해야 하는 설정 2가지를 작성하시오.



1. MEDIA_URL = '/media/'
2. MEDIA_ROOT = BASE_DIR / 'crud' / 'uploaded_files'





### 7. DB True or False

> 각 문항을 읽고 맞으면 T, 틀리면 F를 작성하시오.
>
> 1) RDBMS를 조작하기 위해서 SQL문을 사용한다. 
>
> 2) SQL에서 명령어는 반드시 대문자로 작성해야 동작한다. 
>
> 3) 일반적인 SQL문에서는 세미콜론( ; )까지를 하나의 명령어로 간주한다. 
>
> 4) SQLite에서 .tables, .headers on과 같은 dot( . )로 시작하는 명령어는 SQL문이 아니다.  
>
> 5) 하나의 데이터베이스 안에는 반드시 한 개의 테이블만 존재해야 한다.



1) T

2) F : 소문자를 써도 동작하나, 대문자로 쓰는 것을 권장한다.

3) T 

4) T : . 명령어는 sqlite3 명령어이다.

5) F  : 한개의 테이블만 있는 경우도 있겠지만, 대부분의 경우에 수많은 테이블이 이루어져있다.



### 8. on_delete

> 게시글과 댓글의 관계에서 댓글이 존재하는 게시글은 삭제할 수 없도록 즉, ProtectedError를 발생시켜 참조 된 객체의 삭제를 방지하는 __(a)__를 작성하시오.



```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete = models.__(a)__)
```



* PROTECT



#### 9.  Like in models

>Article 모델과 User 모델을 M:N 관계로 설정하여 ‘좋아요’ 기능을 구현하려고 한다. __(a)__와 __(b)__에 들어갈 내용을 작성하시오. 추가적으로 아래의 상황에서 __(b)__를 반드시 작성해야 하는 이유를 함께 작성하시오.

a) ManyToManyField

b) related_name 



* related_name 을 설정하는 이유는 지금 user 필드와 like_users가 모두 타겟 모델로 settings.AUTH_USER_MODEL, 즉 현재 활성화된 유저모델인데, 유저모델 측에서 Article을 역참조하게 되면, 기존의 _set 매니저로는 user와 like_users 둘 다를 참조하게 된다. 따라서 related_name을 지정해줘서 그러한 혼란을 막아야한다.



#### 10. Follow in models

>follow 기능을 구현하기 위해 accounts app의 models.py에 아래와 같은 모델을 작성하였다. Migration 작업 이후에 Database에 만들어지는 중개 테이블의 이름을 작성 하고 이 테이블의 id를 제외한 컬럼 이름을 각각 작성하시오.

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name = 'followers')
```



* accounts_user_followings : 테이블 네임

* from_user  //  to_user : 컬럼



테이블 네임 규칙 :  ```앱 이름 _ 클래스 이름 _ 필드 이름``` (전부 소문자)

재귀 필드네임 규칙 : ```from_클래스 이름``` // ```to_클래스 이름``` 

