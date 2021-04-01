### 14_django_homework

---



#### 1. M:N True or False

> 각 문항을 읽고 맞으면 T, 틀리면 F를 작성하고 틀렸다면 그 이유도 함께 작성하시오. 
>
> 1) Django에서 1:N 관계는 ForeignKeyField를 사용하고 M:N 관계는 ManyToManyField를 사용한다. 
>
> 2) ManyToManyField를 설정하고 만들어지는 테이블 이름은 “앱이름 _ 클래스이름_지정한 필드이름”의 형태로 만들어진다.  
>
> 3) ManyToManyField의 첫번째 인자는 참조할 모델, 두번째 인자는 related_name이 작성 되는데 두 가지 모두 필수적으로 들어가야 한다.





1. T. ManyToManyField는 기본세팅으로 만들어졌을 때,  ForeignKeyField 두 개로 이루어진 테이블을 새로 만들어준다.
2. T. 다만, 모두 소문자로 작성된다.
3. F. related_name의 경우에는 역참조시 매니저 이름이 중복되지 않는다면, (소스 모델이 두 개 이상의 타겟 모델을 가르키지 않는다면) 지정하지 않아도 무방하다. 하지만 대부분의 경우, M2M 필드에는 related_name을 지정하는데, related_name을 지정함으로서, 데이터에 더 직관적으로 접근 할 수 있기 때문이다. 



#### 2. Like in templates

> 아래 빈 칸 (a) 와 (b)에 들어갈 코드를 각각 작성하시오.



a) request.user

b) article.like_users.all







#### 3. Follow in views

> 모델 정보가 다음과 같을 때 빈칸 a와 b에 들어갈 코드를 작성하시오



a)  user_pk

b)  followings

c) filter

d) remove

e) add





#### 4. User AttributeError

> 아래와 같은 에러 메시지가 발생하는 이유와 이를 해결하기 위한 방법과 코드를 작성하시오.
>
> Manager isn't available; 'auth.User' has been swapped for 'accounts.User'



유저 모델을 커스텀하고 나서도, 모델 .py 에서 User를 참조하는 주소를 바꾸지 않아서 발생한 에러입니다. 유저모델을 커스텀한 이후에는 settings.py에서 AUTH_USER_MODEL 을 명시해주고, models.py에서도 통상적인 User 모델 대신 setting을 import 한 뒤 settings.AUTH_USER_MODEL 을 해줘야합니다.

#### 5 . Related+name

> 아래의 경우 related_name 을 필수적으로 설정해야한다. 그 이유를 설명하시오.

역참조 충돌이 일어나서 입니다. user 필드와 like_users 모두 커스텀 Usermodel을 사용하는데, related_name을 설정하지 않으면 나중에 User 모델에서 Article을 역참조 할 때, article_set 매니저를 사용하게 되면, user 필드와 like_users 필드 둘 다를 지칭하게 되어 충돌이 일어납니다. 그러한 일을 막기 위해서 related_name을 설정해준 것입니다.





#### 6. follow templates

> person 변수에는 view 함수에서 넘어온 유저 정보가 담겨 있고, 모델 정보가 아래와 같을 때, 빈칸 a b c d e 에 들어갈 알맞은 코드를 각각 작성하시오



a : person.followings.all // person 변수를 참조하는 유저 객체의 집합

b : person.followers.all // persona 변수가 참조하는 유저 객체의 집합

c : request.user // 요청을 보낸 유저 자신을 지칭

d:  person // 이게 왜 동작하는지는 모르겠는데, 현재 요청을 보낸 유저와, person 변수와의 비교를 한다.

e: person.pk