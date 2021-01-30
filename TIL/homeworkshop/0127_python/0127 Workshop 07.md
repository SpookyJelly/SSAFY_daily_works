# 0127 Workshop 07

> Faker는 개발시 활용할 수 있는 가상의 데이터를 생성해주는 파이썬 패키지이다. 워크샵에 등장하는 코드는 모두 Github(https://github.com/joke2k/faker) 문서의 예제이다. 지금까지 배운 파이썬 개념을 활용하여 해석 하시오.



### 1. pip

> 아래 명령어는 **(1) 무엇을 위한 명령인지 (2) 실행은 어디서 해야하는지**  작성하시오.

```python
$ pip install faker
```



* 정답

  1. faker 패키지를 설치하기 위한 명령어

  2. 실행은 cmd 터미널에서 하거나, VScode에서의 Python Powershell에서 실행해야합니다.

     --> 두 경우 모두 파이썬이 설치된 경로에서 실행해야합니다.(위치 상관 없음.)



### 2. Basic Usages

> Faker는 다양한 메서드를 통해 임의의 결과값을 반환해준다.
>
> 임의의 영문 이름을 반환하는 아래 코드에서 라인별 의미를 주석을 참고하여 작성하시오.



```python
from faker import Faker # 1 faker 패키지에서 Faker 모듈을 import 하기 위한 코드이다.
fake = Faker()			# 2 Faker는 클래스, fake는 인스턴스이다.
fake.name()				# 3 name()은 fake의 메서드이다.
```





### 3. Localization

> Faker는 다양한 언어의 Locale을 지원한다.
>
> ```python
> # 1. 인자 없이 호출 시에는 영문이 기본 설정이다 (en_US)
> 
> fake = Faker()
> fake.name()
> # => 'Shelly Wilcox' (랜덤이므로 결과 값이 다를 수 있다.)
> ```
>
> ```python
> # 2. Locale 정보를 포함하여 호출 시에는 해당 언어 설정을 따른다.
> 
> fake_ko = Faker('ko_KR')
> fake_ko.name()
> # => '박진우' (랜덤이므로 결과 값이 다를 수 있음)
> ```
>
> 직접 해당하는 기능을 구현한다고 하였을 때, 빈칸의 코드를 적절히 작성하시오.



```python
class Faker():
    def __init__(self,Locale):
        self.Locale = Locale
    
# Faker 클래스를 생성할 때, Locale이라는 언어 속성을 받으니까 생성자인 __init__를 구현해준다.
```





### 4. Seeding the Generator

> 컴퓨터 프로그래밍에서 임의의 값을 반환하는 경우(난수 생성 등) 시드라는 개념이 있다.
>
> 시드를 설정하게 되면 동일한 순서로 난수를 발생시킬 수 있어 일반적으로 디버깅을 위하여 활용된다.
>
> 이하 코드를 실행했을 때, # 1 , #2 출력결과를 작성하고 seed()는 어떤 종류의 메서드인지 작성하시오.

```python
from faker import Faker
import random

fake = Faker('ko_KR')
Faker.seed(4321) #0

print(fake.name())  #1

fake2 = Faker('ko_KR')

print(fake2.name()) #2


# 결과

# 1: 이도윤
# 2: 이지후

# 몇번을 반복해도 같은 결과임. #0을 주석 처리 하면 실행할때마다 다른 결과가 나오는것과 대조됨.

# seed는 Faker 클래스에 붙어있는 메소드. 즉 Class 메소드이다.

```



> 이하의 코드를 실행 했을 때, #1과 #2에서 출력되는 결과를 각각 작성하고, seed_instance()는 어떤 종류의 메서드인지 작성하시오.

```python
from faker import Faker
import random

fake = Faker('ko_KR')
fake.seed_instance(4321) #0
print(fake.name())  #1

fake2 = Faker('ko_KR')

print(fake2.name()) #2

# 결과

# 1: 이도윤
# 2: 나하철 (이후 반복 때마다 바뀜) 

# seed_instance()는 인스턴스 메소드이다.
# fake2는 .seed_instance에 의해 시드값이 고정되지 않았기에, 반복때마다 결과가 바뀐다
```





* seed()와 seed_instance()는 각각 어떠한 용도로 쓰일 수 있는지 작성하시오.

> seed()는 반복된 결과를 출력할때 클래스 단위로 시드를 고정시켜 사용할 수 있다.
>
> 반면 seed_instance()는 하나의 객체만 여러 난수가 필요할때 사용할 수 있을 것 같다.



> * 주로 테스팅할 때 사용
> * seed_instance는 특정 인스턴스만 시드 초기화가 필요할 경우 사용