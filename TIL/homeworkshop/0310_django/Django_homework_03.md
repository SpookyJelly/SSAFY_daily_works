# Django_homework_03

### 1. Model 반영하기

> "Django가 Model에 생긴 변화를 DB에 반영하는 방법" 을 뜻하는 용어를 작성하시오.

* Migrate



### 2. Model 변경사항 저장하기

---

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() # 문제 오타인듯
```

> 위에서 작성한 Model의 변경 사항을 저장하기 위한 명령어를 작성하시오. 이로 인해 생성된 파일에 대응되는 SQL문을 확인하는 명령어와 출력 결과를 작성하시오.



* 명령어 : python manage.py makemigrations

  ---

  -> 결과 : migrations 폴더 내에 0001_initial.py 가 생성된다.



* 대응되는 SQL문을 확인하는 명령어 : python manage.py sqlmigrate "앱 이름" 00014

  ---

  * 출력 결과

  ```
  BEGIN;
  --
  -- Create model Article
  --
  CREATE TABLE "pages_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL);
  COMMIT;
  ```

  

### 3. Python Shell

> Django에서 사용 가능한 모듈 및 메서드를 대화식 Python Shell에서 사용하려고 할 때, 어 떠한 명령어를 통해 해당 Shell을 실행할 수 있는지 작성하시오.



```
# 일반 셀을 호출하는 명령어 (bash에서 실행)
python manage.py shell

# 확장 셀을 호출 하는 명령어
# settings -> Installed_apps에서 'django_extension'을 추가해줘야한다.

python manage.py shell_plus
```





### 4. Django Model Field

---

> Django에서 Model을 정의할 때 사용할 수 있는 필드타입을 5가지 이상 작성하시오



1. CharField(max_length= 10) : 문자열 타입 데이터를 받는 필드 / 문자열 제한을 뜻하는 max_length가 반드시 들어가야 한다. 보통 제목에 사용된다.
2. TextField() : 문자열 타입 데이터를 받는 필드 / 문자열 제한이 없음
3. DateTimeField() : 시간 타입 데이터를 받는 필드. Python의 datetime.datetime 인스턴스로 표현된다.
4. JSONField() : Django 3.1 버전에서부터 추가된 필드로, JSON 인코딩된 데이터들을 받는 필드이다.
5. BooleanField : 참 거짓 타입을 받는 필드