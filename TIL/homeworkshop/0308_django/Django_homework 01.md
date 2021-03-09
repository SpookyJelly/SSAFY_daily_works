# Django_homework 01



1. Settings

   > 1-1. django 서버를 실행하고 첫 페이지에 접속했을 때 터미널에 출력된 서버 시간이 현재 한국 시간과 다른 시간으로 출력된다. 이를 한국 시간으로 바꾸려면 settings.py에 어떤 변수 그리고 어떤 값을 할당해야 하는지 작성하시오. 

   

   * TIME_ZONE 변수에 'Asia/Seoul'를 할당해야합니다.

   

   > 1-2. 추가로 settings.py에 "이 변수"가 False인 상태로 1-1번 변수를 설정하는 것은 error라 고 한다. "이 변수"는 무엇인가

   * USE_TZ = True

---

공식 문서에 따르면, 표준시간대 지원은 기본적으로 비활성화 되어 있어, 활성화 하려면 settings.py에서 수정을 해야한다고 합니다. 그런데 이 시간은 웹이나 터미널에서 확인하는 것이 아니라, 데이터베이스? 에서 확인이 가능하다고 하는데, 이것은 다음 웹엑스 시간에 자세히 배울 예정이라고 한다.. 



* 보충 설명 : 터미널에서는 시간이 정상적으로 뜬다. 근데 UTC로 설정하면 데이터베이스에 값을 저장할때 문제가 된다. 그래도 TIME_ZONE은 잘 알아두셔야하는게, 실무에서 시간관련한 이슈는 상당히 예민한 것이기 때문이다.





2. urls

   > 다음은 어떤 django 프로젝트의 urls.py의 모습이다. 주소 ’/ssafy’로 요청이 들어왔을 때 실 행되는 함수가 pages 앱의 views.py 파일 안 ssafy 함수라면, 요청에 응답하기 위해 빈칸 __(a)__에 추가되어야 할 코드를 작성하시오.



```django
from django.contrib import admin
from dajgo.urls import path
from pages import views

urlpatterns =[
	path('ssafy/',views.ssafy),{#여기가 (a) 위치입니다.  #}
	path('admin/',admin.site.urls),

]
```







### Django Template Language

---



1) menus 리스트를 반복문으로 출력하시오.

```django
{%for menu in menus%}
	<p>{{menu}}</p>
{% endfor %}
```



2) post 리스트를 반복문을 활용하여 0번 글부터 출력하시오.

```django
{% for post in posts%}
	<p>{{forloop.counter0}}번 글 :{{post}}</p>
{% endfor %}
```



3) users 리스트가 비어있다면 **현재 가입한 유저가 없습니다.** 텍스트를 출력하시오.

```django
{% for user in users %}
	<p>{{user}}</p>
{% empty %}
	<p>현재 가입한 유저가 없습니다.</p>
{% endfor %}
```



4) 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기처리하시오.

```django
{% if forloop.first%}
	<p>첫 번째 반복문입니다.</p>
{% else %}
	<p>첫번째 반복문이 아닙니다.</p>
{% endif %}
```



5) 출력된 결과가 주석과 같아지도록 하시오.

```
<!-- 5-->
<p>{{'hello | length'}}</p> # 필터 (|) 앞의 Value의 길이를 출력하는 태그
<!-- My Name Is Tom --> 
<p?{{'my name is tom | capfirst'}}</p> # 필터 앞의 Value의 첫번째 문자만 대문자로 출력하는 태그
```



6) 변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 하시오.

```django
<!-- 2020년 02월 02일 (Sun) PM 02:02 -->
{{ today | date:"Y B d (D) A g:i"}}
```



* 정답 : Y년 m월 d일 (D) A h:i





## Form tag

> 다음은 form tag 에 관한 문제이다. 올바른 답을 작성하시오.

```django
<form action = "/create/" method="">
    <label for="title"> Title : </label>
	<input type ="text" name="title" id="title">
    <label for = "content">Content : </label>
    <input type="text" name="content" id="content">
    <label for ="my-site">My-site : </label>
    <input type="text" name="my-site" id="my-site">
    <input type="submit"> 
</form>
```

1. 지문의 코드 중 form 태그의 속성인 action의 역할에 대해 설명하시오.

   > form이 제출(submit) 될 때 처리가 필요한 데이터를 전달받는 곳의 URL 주소를 알려주는 역할을 가진다.

2. 지문의 코드 중 method가 가질 수 있는 속성 값을 작성하시오.

   > GET. POST 등등 이 있다.

   * Form은 GET이랑 POST 밖에 못 쓴다.

3. input 태그에 각각 '안녕하세요','반갑습니다','파이팅' 문자열을 넣고 submit 버튼을 눌렀을 때 이동하는 url 경로를 작성하시오.

   > /create/?title=안녕하세요&content=반갑습니다&my-site=파이팅

* ?가 붙는 이유

  > ? 는 Qurey string이다. 이후에 key = value 값으로 출력되고, Get 요청일때 붙어서 나온다.

* method = "" 라고 해도 ? 가 붙는 이유

  > 디폴트가 GET이다. 근데 교수님은 명시적으로 표시하는 것을 좋아하셔서 표시한 것.
  >
  > 만약에 method = "POST"이면 달라진다.