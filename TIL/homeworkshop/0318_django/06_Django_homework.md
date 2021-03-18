### 06_Django_homework

---



### 1. static 파일 기본 설정

---

> 개발자가 작성한 CSS 파일이나 미리 업로드 한 이미지 파일 등이 Django 프로젝트 폴터 (my_pjt) 내부 assets 폴더에 있다. 이처럼 기존 static 파일 경로 외에 추가 경로를 정의해야 할 경우, settings.py에 추가해야 하는 설정과 값을 작성하시오.



* 기본적으로 정적 파일은 

```python
# settings.py
STATIC_URL = '/static/' 
```

의 경로로 지정되어있다. 하지만 개발자가 유지보수 용이 등의 목적으로 추가 경로를 정의해야할 경우는 아래와 같이 추가 경로를 지정해 줄 수 도 있다.



```python
# settings.py
STATICFILES_DIRS = [ BASE_DIR /'my_pjt'/ 'assets']
```





**추가로 이후 배포를 위해서는 각 추가 경로등에 퍼져있는 정적 파일들을 모아야하는데, 그때 설정 해야하는 것이 STATIC_ROOT이다 **

```python
# settings.py
STATIC_ROOT = BASE_DIR / 'staticfiles'
```





### 2. Media 파일 기본 설정

---

> 사용자가 업로드 파일의 저장치를 Django 프로젝트 폴더 (my_pjt) 내부 uploaded_files 폴더로 지정하고자 한다. 이 때, settings.py 에 작성해야하는 설정과 값을 모두 작성하시오.



```python
#settings.py

MEDIA_URL = '/media/'

#MEDIA_ROOT
# 실제 업로드 되는 파일이 저장되는 경로를 지정
MEDIA_ROOT = BASE_DIR / 'uploaded_files'

```



* 이후 처리해줘야하는 과정



```python
#my_pjt > urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

* urlpatterns 뒤에 다음과 같이 추가적으로 + 를 해줘야한다.







### 3. Serving files uploaded by user during development

---

> setting.py에 MEDIA_URL 값이 작성되어 프로젝트에 사용자가 업로드한 파일이 업로드 될 수 있게 되었다. 하지만 사용자가 실제 웹 페이지 내에서 이 파일을 조회 할 수 있도록 하기 위해선 업로드 된 파일에 대한 URL을 생성해주는 설정이 필요하다. 빈칸을 채우시오



```python
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



* 앞선 문제에서 말했듯, settings.py 설정 이후에  URL에서도 설정을 해줘야한다.



* Django 공식 문서를 참고하면 아주 좋다 : https://docs.djangoproject.com/ko/3.1/howto/static-files/