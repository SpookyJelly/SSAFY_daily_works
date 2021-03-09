# 02_Django_homework



### 1. MTV

>Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의 약자이며, 각각 MVC 디자인 패턴과 어떻게 매칭이 되며, 각 키워드가 Django에서 하는 역할을 간략히 서술하시오.



```
# Django #							#Other Framework#			
M : Model							M : Model
T : Templates						V : View
V : View							C : Controller

```



* Model -Model : 데이터베이스 관리
* Template- View : 인터페이스 또는 화면 담당
* View - Controller : Model과 Template 사이의 중개자
  * HTTP 요청을 수신하고 HTTP 응답을 반환
  * Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
  * 그리고 템플릿에게 응답의 서식 설정을 맡긴다. 



### 2.URL

> __(a)__는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을 의미한다. __(a)__는 무엇인지 작성하시오.



* Variable Routing



### 3.Django

> template path Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에 등록된 각 앱 폴더 안의 __(a)__ 폴더 내부를 탐색한다. __(a)__에 들어갈 폴더 이름을 작성하시오.



* Templates 폴더 내부를 탐색



### 4. Static web and Dynamic web

> Static web page와 Dynamic web page의 특징을 간단하게 서술하시오.



* 정적인 웹 : 미리 만들어진 것
* 동적인 웹 : 사용자가 요청했을 때 만들어지는 페이지

---

static web : 사용자의 요청에 따라 서버 안에 이미 저장되어 있는 문서 자체를 사용자에게 보여준다.

Dynamic web : 사용자의 요청이 들어오면 web application 서버에서 상황에 맞는 문서를 생성해 제공한다.