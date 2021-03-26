### 11_Django_practice

---



#### SQL ORM 비교하기

> 주어진 정보를 활용하여 작성된 SQL문과 대응하는 ORM문을 작성하고 실행하시오.



* SQL 기본
  * SELECT : 내가 선택하고 싶은것  
  * FROM : 그걸 어디서 선택하고 싶은가?
  * WHERE : 어떤 조건으로 선택하고 싶은가?
  * LIKE : (문자열 검사에서만 등장) 이 요소와 유사한 조건으로 선택하고 싶어.



* 자주 쓰이는 문법

  * COUNT() : () 조건에 만족하는 것들을 전부 포함하여 count한 값을 반환한다.
  * LIKE :  _ 와 % 와 같이 쓰이는 조건으로, 각각 문자열 와일드 카드에 대응된다. LIKE가 나타내는 문자열들과만 매치해준다
  * UPDATE / SET : UPDATE 이하의 테이블의 뭔가를 (아마도 조건에 맞는 데이터)를 SET 조건에 맞게 설정해준다.  

  * DISTINCT : 중복을 제거해준다.(중복없는 조회) //ORM에서도 .distinct() 형태로 쓴다
  * AVG() : 평균을 구해준다

* Django ORM

  * aggregate()  : ( ) 안의 필드의 총합을 구한다. --> Max,Avg,Min 등의 함수를 이용해서 각 최대값 , 평균값, 최소값까지 같이 구할수 있다.
  * annotate () : 필드 하나를 만들고 거기에 (  )안에 맞는 내용을 채운다.

* 테이블 이름이 정해지는 방식 

  ```bash
  $ sqlite3 db.sqlite3
  SQLite version 3.35.2 2021-03-17 19:07:21
  Enter ".help" for usage hints.
  sqlite> .mode csv
  sqlite> .import users.csv users_user
  ```

  * 처음에 이 과정에서 users.csv를 users_user로 이름 붙였다.



1) user 테이블 전체 데이터를 조회하시오

```sql
SELECT * FROM users_user;
```

```python
User.objects.all()
```



2) id가 19인 사람의 age를 조회하시오

```sql
SELECT AGE FROM users_user WHERE id= 19;
```

```python
User.objects.filter(id=19).values('age')[0]
```

**주의! QuerySet이 가지고 있는 값을 보는 메서드는 values이다**. **value 아님!**



3) 모든 사람의 age를 조사하시오

```sql
SELECT age FROM users_user
```

```python
User.objects.all().values('age')
```

* ORM을 이용해서  각 QuerySet의 age 키 값의 Value를 꺼내려고 다음과 같은 시도를 해봤다.

  ```python
  User.objects.all().values('age')[:]['age']
  
  -->TypeError: QuerySet indices must be integers or slices, not str.
  ```

  * QuerySet은 리스트안에 딕셔너리가 잔뜩 들어가 있는 꼴과 유사하므로, 슬라이싱으로 다 복사한다음에 value를 꺼내려고 했는데, TypeError가 났다. 
  * 생각해보니까 Python에서도 이건 for문을 통해 각 Value를(숫자만 나오도록) 꺼냈었다. 지금 코드를 다시 보니까, 복사한 리스트에서 인덱싱을 문자열로 하려는 꼴이다. 당연히 될리가 없다.

  * 아쉽게도, count나 데이터 값 보는 것은 하나씩만 할 수 밖에 없다.

4) age가 40 이하인 사람들의 id와 balance를 조회하시오

```sql
SELECT id,balance FROM users_user WHERE age<=40;
```

```python
User.objects.filter(age__lte=40).values('id','balance')
```

* ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

  ``` 부등호 는 ORM에서 못 쓴다```



5) last_name이 '김'이고 balance가 500 이상인 사람들의 first_name을 조회하시오

```sql
SELECT first_name FROM users_user WHERE last_name ='김' AND balance >=500;
```

```python
User.objects.filter(last_name='김',balance__gt=500).values('first_name')
```



6) first_name이 '수'로 끝나면서 행정구역이 경기도인 사람의 balance를 조회하시오

```sql
SELECT balance FROM users_user WHERE country ='경기도' AND first_name LIKE '%수'
```

```python
User.objects.filter(first_name__endswith='수', country = '경기도').values('balance')
```

* endswith 룩업 쓰면 된다 // 뜻 :  ~~로 끝나는 케이스들과 매치 됨



7) balance가 2000 이상이거나 age가 40 이하인 사람의 총 인원수를 구하시오

```sql
SELECT COUNT(*)
FROM users_user
WHERE balance >=2000 OR age <= 40;
```

```python
User.objects.filter(Q(balance__gt=2000)|Q(age__lte=40)).count()
```

* or 조건을 ORM에서 사용하려면 Q 객체를 이용해야한다. or은 | 로 표시되고, 필터링 할 조건을 Q()안에 집어넣으면 된다. 
* 원래는 Q 모듈도 import 해줘야하지만, Shell_plus를 사용한다면, 알아서 해주기 때문에 필요없다.



8) phone 앞자리가 '010'으로 시작하는 사람의 총원을 구하시오.

```sql
SELECT COUNT(*) FROM users_user WHERE phone LIKE '010-%';
```

```python
User.objects.filter(phone__startswith='010-').count()
```



9) 이름이 '김옥자'인 사람의 행정구역을 경기도로 수정하시오.

```sql
UPDATE users_user SET country='경기도' WHERE first_name = '옥자' AND last_name = '김'; 
```

```python
user = User.objects.get(first_name='옥자', last_name='김')

user.country = '경기도'
```



10) 이름이 '백진호' 인 사람을 삭제하시오

```sql
DELETE FROM users_user
WHERE first_name = '진호' AND last_name = '백';
```

```python
user = User.objects.get(first_name='진호',last_name='백')

In [98]: user.delete()
Out[98]: (1, {'users.User': 1})
```



11) balance를 기준으로 상위 4명의 first_name,last_name,balance를 조회하시오

```sql
SELECT first_name,last_name,balance FROM users_user ORDER BY balance DESC LIMIT 4;
```

```python
User.objects.order_by('-balance').values()[0:4]
```



12) phone에 '123'을 포함하고 age가 30미만인 정보를 조회하시오

```sql
SELECT * FROM users_user WHERE phone LIKE '%123%' AND age<=30;
```

```python
User.objects.get(phone__contains='123',age__lt=30)
```



13) phone이 '010'으로 시작하는 사람들의 행정 구역을 중복 없이 조회하시오.

```sql
SELECT DISTINCT country FROM users_user WHERE phone LIKE '010%';
```

```python
User.objects.filter(phone__startswith='010').values('country').distinct()
```

* 말도 안되게 복잡한거 같다.



14) 모든 인원의 평균 age를 구하시오

```sql
SELECT AVG(age) FROM users_user;
```

```python
User.objects.all().aggregate(Avg('age'))
```



15) 박씨의 평균 balance를 구하시오

```sql
SELECT AVG(balance) FROM users_user WHERE last_name = '박';
```

```python
User.objects.filter(last_name='박').aggregate(Avg('balance'))
```



16) 경상북도에 사는 사람 중 가장 많은 balance의 액수를 구하시오

```sql
SELECT MAX(balance) FROM users_user WHERE country ='경상북도';
```

```python
User.objects.filter(country='경상북도').aggregate(Max('balance'))
```



17) 제주 특별자치도에 사는 사람 중 balance가 가장 많은 사람의 first_name을 구하시오.

```sql
SELECT first_name FROM users_user WHERE country = '제주특별자치도' ORDER BY balance DESC LIMIT 1;
```

```python
User.objects.filter(country='제주특별자치도').order_by('-balance')[0].first_name
```

