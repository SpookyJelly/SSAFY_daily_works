### 07_Django_homework

---



### 1. Copiled Bootstrap

> CSS,JS 파일을 다운로드 받아 Django 프로젝트에 Static 파일로 추가하시오. 부트스트랩이 적용되기 위해 작성해야할 코드를 제출하시오.



1. setting.py 

   ```
   STATIC_URL = '/static/'
   
   STATICFILES_DIRS = [ BASE_DIR /'crud' /'static']
   ```

   

* 개별 앱에 'static' 폴더를 만들어도 되지만 하나의 폴더에서 관리하고 싶어서, 프로젝트 위치에 생성하였다.



2. 부트스크랩을 적용하고 싶은.html

```html

{% load static %}
~~~

<link rel="stylesheet" href="{% static '/css/bootstrap.css' %}"> 
```



* 여기서 중요한 것은, static을 load할 때 extend 보다 위에 가서는 안되고, (extend는 무슨 일 이 있어도 최상단에 위치해야한다.) link로 외부 파일을 연결할때, 상대 주소를 잘 고려해야한다는 것이다.