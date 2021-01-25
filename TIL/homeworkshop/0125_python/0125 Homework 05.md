# 0125 Homework 05



## 1. 모음은 몇 개나 있을까?

> 문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는 count_vowels 함수를 작성하시오. 단, .count()메서드를 활용하여 작성하시오.

```python
# 접근방법
# 1. vowels 라는 모음으로 이루어진 리스트 생성
# 2. input으로 들어오는 word의 각 리터럴에 접근(string은 시퀀스 형 자료이기 때문에 형변환 없어도 됨)
# 3. 모음의 갯수를 count할 변수 cnt 생성
# 3. word.count(x)메서드를 이용하여, x 자리에 vowels의 리터럴이 순회하도록 설계
# 4. 모음 등장시 마다 cnt += 1. return cnt

def count_vowels(word):
    cnt = 0
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        cnt += word.count(vowel) 
    return cnt
```

* 결과

```python
print(count_vowels('apple')) # --> 2
print(count_vowels('banana')) # --> 3
```





## 2. 문자열 조작

> 다음 중, 문자열(string)을 조작하는 방법으로 옳지 않은 것을 고르시오.

```
(1) .find(x)는 x의 첫번째 위치를 반환한다. 없으면 -1을 반환한다.
	#True
	# .index(x)는 x가 존재하지 않으면 error를 낸다.
	
(2) .split([chars])은 특정 문자를 지정하면 문자열을 특정문자를 기준으로 나누어 list로 반환한다.
	특정 문자를 지정하지 않으면 공백을 기준으로 나눈다.
	#True
	
(3) .replace(old,new[,count])는 바꿀 대상 문자를 새로운 문자로 바꿔서 반환한다.
	# True
	# count 매개변수는 몇번 반복할지 정하는 변수이다. (생략가능/ 생략시 모든 문자열에 대해 적용)
	
(4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를 찾아 제거한다. 특정 문자를 지정하지 않	으면 오류가 발생한다.
	#False
	#chars.strip() 꼴로 사용한다. .strip 메소드는 양쪽에서 공백을 제거하는 역할을 한다.




```





## 3. 정사각형만 만들기

> 각각 너비와 높이의 값으로 이루어진 2개의 list를 전달 받아, 각각의 값들을 조합하여 만들 수 있는 정사각형 만의 넓이를 담은 list를 반환하는 only_square_area 함수를 작성하시오.



```python
# 접근방법
#1번. 2중 for문
#2번. set 자료형으로 중복 제거, 각각 추리기

# 1번 풀이법은 너무 자주했으니까, set자료형을 통해 문제를 해결하겠다.

def only_square_area(list_1,list_2):
    area_list = [] # 정사각형만의 넓이를 담을 list
    all_set = list(set(list_1) & set(list_2))
    #0. 정사각형 --> 가로/세로가 같은 도형 --> 두 리스트의 공통된 값을 추릴수 있다면, 
    #   굳이 두개의 리스트에 접근할 필요가 없다.
    #1. input으로 들어오는 list를 set으로 바꿔 중복을 없앤다.
    #2. 두 set의 교집합을 받는 변수인 all_set에 할당한다.
    #3. 시퀀스 형 자료인 list 자료형으로 바꿔, 이후의 for문에서 사용할 수 있게 한다. 
    for context in all_set: 
        area_list.append(context**2) # 가로 == 세로 일때 , 가로*세로 == 가로(세로) **2 이다.
    return area_list #리스트 째로 반환
```

* 결과

```python
only_square_area([32,55,63],[13,32,40,55]) # -->[1024, 3025]
```

