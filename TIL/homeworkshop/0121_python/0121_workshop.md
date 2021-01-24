# 1. 숫자의 의미

> 정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 get_secret_word 함수를 작성하시오. 단, list는 65 이상 90 이하. 그리고 97 이상 122이하의 정수로만 구성되어 있다.

```python
# 1. 리스트의 각 리터럴에 접근
# 2. chr() 함수를 이용해 아스키 변환
# 2.5. list를 직접 수정해야하므로, 인덱스를 통해 값 변경한다.
# 3. 아스키 변환 된 리스트를 형식에 맞게 출력

def get_secret_word(int_list): 
    for num in range(len(int_list)): # 1. num in range(len) 을 사용해 int_list의 각 인덱스를 지칭할 수 있게 됨
        int_list[num] = chr(int_list[num])
        '''
        2.5 리스트의 요소 직접 변환. 만약에 인덱스 접근이 아니라 for num in int_list를 사용했다면, num = chr(num)을 하더라도, 
        int_list가 바뀌는게 아니라, 매개변수만 바뀔 뿐이다. 그래서 변환이 잘되어도 그 값이 return 되지는 않는다.
        
        '''
    string = ''.join(int_list) #3. 이 단계에서 int_list == ['S','s','A','f','Y']이다. .join() 메서드를 이용해 형식을 변경한다.
    return string
```

```python
get_secret_word([83,115,65,102,89]) # 'SsAfY'
```

```python
# 3.을 join 메서드 말고 다른 방식으로 처리

def get_secret_word(int_list):
    a= '' # 비어있는 문자 객체 a를 생성
    for num in range(len(int_list)): 
        int_list[num] = chr(int_list[num])
        a +=int_list[num] # a에 chr()로 전환된 int_list[num]을 이어 붙임
    return a # a 반환

```

``` python
get_secret_word([83,115,65,102,89]) # SsAfY
```



###  2.5의 과정을 잘못 알고 있어서 수정. (for num in int_list 사용)

---



```python
def get_secret_word(int_list):
    a = ''
    for num in int_list:
        num = chr(num)
        a +=num
   return a
	# 이런 식으로 chr(num)의 결과를 다른 변수에 저장하면 for num in int_list 꼴을 사용할 수 있다.
        # num = chr(num) 이 과정에서 num은 분명히 chr()에 의해 전환되는데,
        # 여기서의 num은 실제 int_list에 저장된 값들이 아니다. int_list를 참조하는 다른 변수일뿐이다.
        # 그래서 나중에 int_list를 출력해보면 아무것도 안바뀌어서 나오는 것.
        # 실제로는 num만 줄창 바뀌고, int_list에는 아무런 변화가 없었으니까.
        # 그래서 처음 제출한 답안처럼, 아예 int_list의 요소를 지정해서 변환하던가.
        # chr(num)의 결과를 다른 곳에 저장해서 그를 반환 해야하는 것이다.
```



# 2. 내 이름은 몇일까?

> 문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는 get_secret_number 함수를 작성하시오. 단, 문자열은 A~Z, a~z로만 구성되어 있다.

```python
# 1. string을 list 타입으로 바꿔, 각 member를 수정할 수 있게 함
# 2. ord() 함수를 이용해 아스키 변환
# 3. 아스키 변환된 숫자들의 합 출력
# 1번 문제와 동일한 아이디어로 접근 하면 된다.

def get_secret_number(name):
    total = 0
    name_list = list(name) #1. 리스트로 바꾸지 않으면 각 member의 값을 바꿀수 없다.// (A -->65) 이게 안된다는 뜻
    for num in range(len(name_list)):#2 ord() 함수 이용
        name_list[num] = ord(name_list[num])
        total += name_list[num]
    return total # 3. 아스키 변환 된 숫자들의 합 출력

```

```python
get_secret_number('tom') # 336
```



```python
# map 함수를 이용해 더 줄인 방식

def get_secret_number(name):
    name_list = list(name) 
    a = list(map(ord,name_list)) 
    '''
    map(function, Iterator) --> 반복 가능한 객체(Iterator)에 대해 
    function을 순차적으로 적용하고 그 결과를 반환함. 
    이후 list로 바꾸어, 정수형 리스트로 계산을 용이하게 한다.
   
   '''
    total = sum(a)
    return total
```

```python
get_secret_number('tom') # 336
```

### 교수님 코드

---

```python
#내 코드와의 차이는?
'''
나는 주어진 변수 자체를 변환하려고 애를 썼는데,
교수님은 주어진 변수를 참조만 해서 가공했다.

'''
def get_secret_number(word):
    total = 0

    # 1. 문자열을 순회하면서 (문자열은 리스트, 딕셔너리와 마찬가지로 for문을 이용하여 순회가능하죠.)
    for letter in word:
        # 2. tom이라면 t, o, m 하나씩 letter라는 이름으로 나올테니
        # ord() 함수를 이용하여 숫자로 바꿔줍니다.
        number = ord(letter)
        # 3. 바깥에 변수를 하나 만들어놓고 거기에 다 더해줍니다.
        total += number #🔴 total에 number를 더해주는 것을 매 루프 반복함으로서, input된 단어가
        				#   변환된 결과를 실시간으로 update하였다.

    # 4. 반복문 종료 후 다 더해진 total값 반환해줍니다.
    return total

print(get_secret_number('tom'))



```





# 3. 강한 이름

> 문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.

```python
# 1. 입력값을 분리
# 2. 분리된 입력값에 대해 각 아스키 전환
# 3. 전환값의 대소 비교
# 4. 전환값이 큰 전달인자의 원본을 반환
# 조건에서 문자열 2개가 들어온다고 하였으니, 굳이 가변인수를 쓸 필요 없이. parameter를 2개 만들면 된다.
def get_strong_word(a,b): # a,b,가 튜플 꼴로 들어온다.
    ab_list = [list(a),list(b)] #1. 튜플을 list로 변환하고 분리한다. (튜플은 immutable 해서 일부 수정이 안되기 때문에 list로 변환한다.)
    a_power = list(map(ord,list(a))) # 2. 분리된 입력값에 대해 각 아스키 전환 (2번 문제와 같은 코드)
    b_power = list(map(ord,list(b)))
    if a_power > b_power: # 3. 전환값의 대소 비교.
        return a # 4. 전환값의 큰 전달인자의 원본을 반환
    elif a_power == b_power: # 3.5 문제에 없는 조건이지만, 만약에 같다면 두 합이 같다고 알려준다.
        print("아스키 합이 같습니다.")
    else :
        return b


```



### 3번 수정

---

* 3번은 주어진 예제에 대해서는 올바른 출력이 나오나, 그 이외의 입력 값에 대해서는 오답을 출력하게 됨.

  > 원인은 다음과 같다.
  >
  > 1. 단어 a,b를 리스트로 전환한 후, 리스트의 요소들을 합치지 않았음
  > 2. 그 결과 리스트의 비교연산이 되어버림

  * 이번 실수를 통해 리스트, 문자열에서도 비교연산자를 사용할 수 있다는 사실을 알게 되었음.
  * 리스트, 문자열에서의 비교연산자 동작은 아래와 같다.

```python
list_a = [1,2,3,5]
list_b = [1,2,3,4]

# 결과
list_a > list_b --> True

# 작동 과정
list_a[0] / list_b[0]를 대소비교
list_a[0] == list_b[0]이면,
list_a[1] / list_a[1]를 대소비교
... 계속 

만약에 list_a[n] > list_b[n] 이면
list_a > list_b ==True가 반환됨.

string_a = 'abcd'
string_b = 'abz'

#결과 
string_a < string_b --> True

# 작동 과정

string_a[0] / string_b[0]를 대소비교 (ord() 사용한 후 비교 하는 듯)
string_a[0] == string_b[0]이면
string_a[1] / string_b[1]를 대소비교
... 계속
string_a[2] < string_b[2] 이므로
string_a <string_b --> True가 반환됨.

비록 string_a가 3번째 요소까지 가지고 있지만, 해당 요소는 비교도 하지 않음.
그래서 길이가 다른 리스트/ 문자열은 올바른 비교를 할 수 없는 것이다.
입력되는 변수의 길이가 같다는 전제하에는 맞는 풀이가 되는데, 그렇다는 보장이 없으니,
큰 의미에서는 오답이 된 것.

하지만, 시퀀스형 자료형에서도 (list, tuple, string) 비교연산자를 사용할 수 있다는 사실을 알게 되었다.
```



* 수정한 답안

  ```python
  def get_strong_word(a,b):
      a_power = 0
      b_power = 0
      for letter in a:
          letter = ord(letter)
          a_power += letter
      for letter in b:
          letter = ord(letter)
          b_power += letter
      if a_power > b_power:
          return a
      elif a_power == b_power:
          ment = "아스키 파워가 같습니다."
          return ment
      else :
          return b
  print(get_strong_word('z', 'a')) # z
  print(get_strong_word('tom', 'john')) # john
  ```

* 수정한 답안 2 ( 기존 양식 유지)

  ```python
  def get_strong_word(a,b):
      ab_list = [list(a),list(b)]
      a_power = list(map(ord,list(a))) 
      b_power = list(map(ord,list(b)))
      if sum(a_power) > sum(b_power): 
          return a
      elif sum(a_power) == sum(b_power):
          print("아스키 합이 같습니다.")
      else :
          return b
  ```

  



# 4. 일기

* 재귀함수가 쉽지 않았다.