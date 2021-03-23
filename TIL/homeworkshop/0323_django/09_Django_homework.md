### 09_Django_homework

---



#### 1. User Model BooleanField

---

> django에서 기본적으로 사용하는 user 모델은 AbstractUser 모델을 상속 받아 정의된다.
>
> 링크 : (https://github.com/django/django/blob/main/django/contrib/auth/models.py)
>
> 여기의 models.py를 참고하여 User 모델에서 사용할 수 있는 칼럼 중 BooleanField 로 정의 된 컬럼을 모두 작성하시오.



1. is_staff
2. is_active
3. is_superuser



#### 2. username max length

---

>django에서 기본적으로 사용하는 User 모델의 username 컬럼이 저장할 수 있는 최대 길이를 작성하시오.



* 1의 문서에 따르면 max_length는 150자이다.





#### 3. login validation

---

>단순히 사용자가 ‘로그인 된 사용자인지’만을 확인하기 위하여 User 모델 내부에 정의된 속성의 이름을 작성하시오.



* .is_athenticated





#### 4. Login 기능 구현

---

> 다음은 로그인 기능을 구현한 코드이다. 빈 칸에 들어갈 코드를 작성하시오.

```python
from django.contrib.auth.forms import AuthenticationForm (a)
from django.contrib.auth import login (b) as auth_login


def login(request):
    if request.method =='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user()(c))
            return redirect('accounts:index')
        
   else:
    	form = AuthenticationForm()
  
   context ={
       'form':form,
   }
    return render(request,'accounts/login.html',context)
```



#### 5. Who are you?

---

>로그인을 하지 않았을 경우 template에서 user 변수를 출력했을 때 나오는 클래스의 이름을 작성하시오.



* AnonymousUser





#### 6. 암호화 알고리즘

---

>Django에서 기본적으로 User 객체의 password 저장에 사용하는 알고리즘, 그리고 함께 사용된 해시 함수를 작성하시오.



* 알고리즘 : pbkdf2 / 해쉬 함수 : sha256





#### 7. Logout 기능 구현

---

>로그아웃 기능을 구현하기 위하여 다음과 같이 코드를 작성하였다. 로그아웃 기능을 실행 시 문제가 발생한다고 할 때 그 이유와 해결 방법을 작성하시오



```python
def logout(request):
    logout(request) # 오류의 원인 : 여기서 재귀 호출이 발생하게 됨
    return redirect('accounts:login')
```



* 오류를 해결하는 방법은 logout 모듈을 다른 이름으로 바꿔주면 된다.

```python
from django.contrib.auth import logout as auth_logout


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

```

