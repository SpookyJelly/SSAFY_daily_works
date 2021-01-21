# 0120 homework

# 1. Built-in 함수

> python에서 기본으로 사용할 수 있는 bulit-in 함수를 최소 5가지 이상 작성하시오.

```python

#1. print(objects) : object를 출력하여 화면에 보여주는 bulit-in 함수
#2. int(object) : number 혹은 string을 정수형으로 바꿔주는 bulit-in 함수 (단, string이 들어갈때는 정수형으로 반환 될 수 있는 string이 들어가야한다.)
#3. str(object) : 주어진 object를 string object로 생성하여 돌려주는 bulit-in 함수
#4. len(object) : object내에 있는 item의 갯수를 반환하는 bulit-in 함수
#5. range(start,stop,step) : start부터 시작하여 step의 보폭으로 stop-1까지 끝나는 시퀀스형 자료을 반환하는 bulit-in 함수

```

* int,str,list는 함수가 아니라고? 클래스인가? 그런가? 맞는거 같은데??



# 2. 정중앙 문자

> 문자열을 전달 받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를 작성하시오.
>
> 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다.

```python
def get_middle_char(word):
    ruler = len(word)
    if ruler % 2 == 0: # 문자의 개수가 짝수일 경우
        return word[(ruler//2)-1]+word[(ruler//2)] 
    		# word가 string이므로, "연결하기" 가능
    
    else: # 문자의 개수가 홀수일 경우
        return word[ruler//2]
```

```python
# 슬라이싱을 활용한 방법

def get_middle_char(word):
    n = len(word)
    if n % 2 :
        return word[n//2]
    else :
   		middle = len(word) //2
    	middle_left = len(word) // 2 -1
    	return word[middle_left:middle+1]
```



```python
#result
get_middle_char('ssafy') --> 'a'
get_middle_char('coding') --> 'di'
```



# 3. 위치 인자와 키워드 인자

> 다음과 같이 함수가 선언되어 있을 때, 보기 (1) ~ (4) 중에서 실행 시 오류가 발생하는 코드를 고르시오.

```python
def ssafy(name, location = '서울'):
    print(f'{name}의 지역은 {location}입니다.)
    
          
       
#(1)
ssafy ('허준')  # 오류 안 남 / location 기본 인자로 지정 되어있어서
          			# ssafy('허준', '서울')와 동일함

#(2)
ssafy(location = '대전', name = '철수') # 오류 안 남 / 키워드 인자만 사용함
          
          
#(3)
ssafy ('영희',location='광주') # 오류 안 남 / 위치 인자를 사용함, location은 '서울'에서 								# '광주'로 바뀜

#(4)
ssafy(name='길동','구미') #  오류 발생 / keyword 인자 사용 후 위치 인자가 올 수 없다.
```



* 따라서 정답은 4번이다.



# 4. 나의 반환값은?

> 다음과 같이 함수를 선언하고 호출하였을 때, 변수 result에 저장된 값을 작성하시오.

```python
def my_func(a,b):
	c = a+b
    print(c)
result = my_func(3,7)
```

* 반환값이 없으므로, 변수 result에는 None이 저장된다.



# 5. 가변 인자 리스트

> 가변 인자 리스트를 사용하여, 갯수가 정해지지 않은 여러 정수들을 전달 받아 해당 정수들의 평균값을 반환하는 my_avg 함수를 작성하시오

```python
def my_avg(*args): # *을 사용해 여러 정수들이 tuple 형태로 전달된다.
    total = 0
    for num in args: # tuple은 시퀀스형 자료이므로, 인덱싱이 가능하다. 
        			 # 따라서, args 내에 있는 리터럴을 참조 사용해, 정수들의 합을 구한다.
        total += num
    return total / len(args) #args는 1개의 튜플이기 때문에, len(object)가 사용가능하다

```

```python
# result
my_avg(77,83,95,80,70) --> 81.0
```







# 6. 교수님께 전하고 싶은 말

* 0120 workshop.md에 적었습니다.



