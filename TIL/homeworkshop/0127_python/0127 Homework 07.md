# 0127 Homework 07

### 1. Type Class

> 파이썬은 객체 지향 프로그래밍 언어이다. Python에서 기본적으로 정의 되어있는 클래스를 최소 5가지 이상 작성하시오.

```python
int()
str()
list()
range()
dict()


'''
여태까지 그저 built-in 함수인줄 알았는데, 이게 다 Class 였구나...

'''
```





### 2. Magic Method

> 아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오

```python
def __init__(self,....)
#생성자라고도 불리며, 클래스가 생성될때 자동으로 실행되는 메서드이다. 주로, 인스턴스의 속성을 할당하는데 씀

def __del__(self)
# 소멸자라고도 불리며, 인스턴스가 사라질 때 자동으로 실행되는 메서드이다.

def __str__()
# __str__ 매직 매서드는 출력타입에 영향을 준다. 전달받은 인자를 문자열 타입으로 전환하여 돌려준다 
# 어떤 객체를 사용자 친화적인 문자열로 표현하기 위한 매직 메서드
# 사용자를 위한 문자열

def __repr__()
# __repr__는 객체를 사용자가 이해할 수 있는 평문으로 반환한디.
# 어떤 객체를 문자열로 표현했을 때, 그 자체로 객체를 완전히 설명하기 위한 메서드
# 파이썬 또는 개발자를 위한 문자열

'''
__str__ 와 __repr__의 공통점 : 객체의 문자열 표현을 반환한다.
					 차이점 : str는 서로 다른 자료형 간에 인터페이스를 제공 / repr는 사용자가 이해할 수 있는 표현으로 나타내기 위한 용도이다.

'''


```



### 3. Instance Method

> .sort()와 같이 문자열, 리스트, 딕셔너리 등을 조작 할 때 사용하였던 것들은 클래스에 정의된 메서드들이었다. 이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 최소 3가지 이상 그 역할과 함께 작성하시오.



```python
# 평소에 점 호출로 사용했던 메소드들이 인스턴스 메소드이다.

'''
1. str.lstrip() / str.rstrip() / str.strip()
# str 타입의 객체의 공백을 제거 한다 (왼쪽 / 오른쪽 / 양쪽)

2. str.split(x)
# 문자열을 x를 기준으로 나눈 후 리스트에 넣어준다. 

3. 'x'.join(str)
# 문자열 str 사이사이에 x를 삽입해준다.

4. list.append(object)
# list의 최후미에 object를 넣어준다.

5. list.extend(iterable)
# iterable 객체를 list에 appending 해준다.


'''



```



### 4.Module Import

> ```python
> #fibo.py
> 
> def fibo_recursion(n):
>     if n < 2:
>         return n
>     else:
>         return fibo_recursion(n-1) + fibo_recursion(n-2)
> ```
>
> 위와 같은 코드가 같은 폴더 안의 fibo.py 파일에 작성되어 있을 때, 아래와 같은 형태로 함수를 실행 할 수 있도록 하는 import 문을 빈칸을 채워넣어 완성하시오
>
> ```python
> from (a) import (b) as (c)
> 
> recursion(4)
> ```



* 정답

```python
from fibo import fibo_recursion as recursion
```

