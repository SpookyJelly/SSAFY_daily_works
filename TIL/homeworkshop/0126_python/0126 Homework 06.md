# 0126 Homework 06

### 1. Built-in 함수와 메서드

> sorted()와 .sort()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

```python
'''
sorted() --> Built-in 함수 / iterable 객체를 받아, 새로운 정렬된 리스트를 "반환"한다.
.sort() --> list 모듈의 메서드 / list 객체를 받아,오름차순 혹은 내림차순으로 정렬한다.(반환 X) 

'''
a = [3,2,1,5,4]

#a를 deep copy
b = a[:]
a.sort()
print(a)
# sorted 함수를 이용하여 c를 생성
c = sorted(b)
print(b)
print(c)

# 여담 : 파이썬에서 사용하는 정렬 알고리즘 : Tim Sort
```

```python
# 결과
a = [1, 2, 3, 4, 5] #.sort()는 원본 리스트가 변함
b = [3, 2, 1, 5, 4] # sorted는 원본 리스트가 변하지 않음 
c = [1, 2, 3, 4, 5]
```



### 2. .extend()와 .append()

> .extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

```python
'''
.extend()는 iterable한 객체를 받아, 하나씩 순회하면서 list에 추가해준다. 연결하기와 유사하다 ( += ) 

반면 .append()는 들어오는 객체를 list의 새로운 요소로 넣어준다. (리스트 가장 마지막에)

받는 객체의 자료형을 구분한다는 것이 두 메소드의 가장 큰 차이인것 같다.

'''

a = []
b = []
c = []

a.extend([1])
b.append(1) #b.extend(1) 이면 에러 난다. (typeError)
c.append([1]) 
print(a , b, c)


```

```python
# 결과
[1] [1] [[1]]
```





## 3. 복사가 잘 된 건가?

> 아래의 코드를 실행 하였을 때, 변수 a와 b에 담긴 list의 요소가 같은지 혹은 다른지 여부를 판단하고, 그 이유를 작성하시오.

```python
a = [1,2,3,4,5]
b = a

a[2] = 5

print(a)
print(b)
```

```python
# 결과 
[1, 2, 5, 4, 5]
[1, 2, 5, 4, 5]

'''
두 리스트가 같은 이유는, b 객체는 a를 복사한 것이 아니라, a가 참조하고 있는 곳의 주소를 복사 한 것이기 때문이다. 비유하자면, a라는 사람이 룸메이트 b에게 자기 집 열쇠를 줘서 같이 살고 있었다. 근데, a가 집 인테리어를 바꿨다. 다음에 b가 집에 왔을때는, 아무것도 하지 않았지만, 바뀐 a의 집을 보게 되는 것이다.

이는 list가 mutable 해서 일어나는 일인데, 다른 mutable한 자료형인 dicitionary, set의 경우는 어떨까?

'''

```



```python
# dicitionary의 경우.

a = {1:2,2:3,4:5} # keys = 1,2,4 // values = 2,3,5
b = a

a[1] = 5 # a[1]의 value를 2-->5로 바꿈

print(a)
print(b)

```

```python
# 결과 

{1: 5, 2: 3, 4: 5}
{1: 5, 2: 3, 4: 5}

#리스트와 동일하게, 두 객체가 모두 바뀌었다.
```



```python
# set의 경우

a = {1,2,3,4,5}
b = a

a[1] = 5

print(a)
print(b)

```

```python
#결과

TypeError: 'set' object does not support item assignment

'''
TypeError가 발생했다. set 객체는 item 할당을 지원하지 않는다고 하는데, set의 특성을 생각해보면 당연하다. set은 순서가 없다. 따라서 인덱싱을 통한 리터럴 접근 (a[1])이 안된다.(not subscriptable)
그렇기에 어떤 한 요소를 찍어서 값을 변경하는 item assignment도 당연히 되질 않는다.

'''
```

