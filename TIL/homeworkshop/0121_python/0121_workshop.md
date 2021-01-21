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





# 4. 일기

* 재귀함수가 쉽지 않았다.