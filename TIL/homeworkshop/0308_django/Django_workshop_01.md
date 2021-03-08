## Django_workshop_01

❖ Django Project 

> 아래 제시된 정보를 참고하여 사용자가 /lotto로 요청을 보냈을 때, 로또 번호 6개를 무작위로 추천하여 보여주는 페이지를 만드시오.
>
>  1) intro/는 startproject 명령어로 생성되는 project 디렉토리이다. 
>
> 2) pages/는 startapp 명령어로 생성되는 application 디렉토리이다.



## 결과

![image-20210308220208479](%EC%BA%A1%EC%B2%98.JPG)



1. ```intro/urls.py```

   ```python
   from django.contrib import admin
   from django.urls import path
   # from . import views 하면 왜 에러나지??
   # 동일한 경로에 없어서 그런거 같은데...(intro와 pages가 같은 레벨에 있다는 말)
   # 라이브 수업시간에는 그냥 . 찍어도 되지 않았나??
   from pages import views
   
   # 1단계 url 매핑 
   # 중요한 포인트는 views.py를 내가 생성한 pages 라는 app에서 import 해야한다는 점 
   urlpatterns = [
       path('pages/', views.lottos),
       path('admin/', admin.site.urls),
   ]
   ```

   

2. ```pages/views.py```

   ```python
   import random
   from django.shortcuts import render
   
   # Create your views here.
   # 2단계. views.py 수정
   def lottos(request): 
       num = range(1,46) 
       #py 파일은 그냥 파이썬 문법이 전부 통한다! sample 메서드를 이용하면 리스트꼴로 반환되는것 까지 똑같다!!
       pick = random.sample(num,6) 
       context ={
           'pick' :sorted(pick),
       }
   
       # 변수를 보낼 때는 dic 꼴로 보내라.
       return render(request,'lotto.html',context)
   ```

   

3. ```templates/lotto.html```

   ```django
   {% comment %} 3단계. 실제 화면에 출력할 html 템플릿 다듬기 {% endcomment %}
   
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>lotto입니다</title>
   </head>
   <body>
     <h1>제 OOO회 로또 번호 추천</h1>
     <p>SSAFY님께서 선택하신 로또 번호는 {{pick}}입니다.</p>
   </body>
   </html>
   ```





### 후기

---

1. manage.py 파일도 없는 쌩 빈 폴더에서 프로젝트를 시작하는 방법이 궁금하다. 숙제를 따로 하나의 폴더에 모을 요량으로 빈 파일에서``` $ python manage.py startproject intro``` 를 쳤는데, 해당 폴더에 manage.py 파일이 없다고 작동이 안된다. ```pip list```로 Django가 깔려있는것도 확인해봤는데, 어떻게 해야할지 모르겠다 

   * 구글링을 해보니, 다른 예제들은 가상 환경을 구축해서 새 프로젝트를 시작한다. 혹시 가상환경이라는게 내 의문을 해결해줄 수 있지 않을까? 라는 생각이 든다.

2.  U -> V -> T 순서가 매우매우매우 중요하다는걸 알았다.

   * 강의보면서 따라하는거랑, 실제로 맨땅에서 머리 박치기 하는거는 하늘과 땅차이임을 다시 느꼈다.

     >1. urls.py (U)
     >
     >   - 사용자가 우리 서버로 요청할 수 있는 URL을 정의하는 파일
     >2. views.py (V)
     >   - 사용자의 요청을 처리하는 함수가 작성되는 파일
     >
     >- **모든 view 함수의 첫번째 인자에는 반드시 request 인자가 들어옵니다.**
     >
     >3. templates (T)
     >
     >   - 응답으로 보내줄 HTML 파일이 담기는 폴더
     >   - 폴더명은 **반드시 templates**로 작성해야 Django가 찾을 수 있습니다.

     *  이 순서를 반드시 외우자.





## 🎴오늘 숙제를 통해 배운점 (그리고 반드시 가지고 가야할 점)



1. py 파일에서는 파이썬 문법을 전부 사용할 수 있다
2. url 맵핑에서 url와 거기서 사용할 view.py에 있는 함수를 연결하는데, ```view. (도트)(함수명)``` 꼴로 연결해줘야한다!
3. **view.py 에서 render 모듈로 return할때는 변수들을 반드시 사전형으로 보내야한다**
   * 이거 몰라서 한동안 애를 먹었다.