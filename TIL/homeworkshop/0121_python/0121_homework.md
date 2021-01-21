# 1. 이름 공간 (Namespace)

> Python에서 변수를 찾을 때 접근하는 이름 공간을 순서대로 작성하시오.

```python
# LEGB Rule을 따른다.
# *L : local scope
# *E : enclosed scope
# *G : global scope
# *B : Built-in scope


# 위에서 아래 순서로 이름공간에 저장된 변수를 찾는다.
```



# 2. 매개변수와 인자, 그리고 반환

> 아래의 보기 (1) ~ (4) 중에서 , 옳지 않은 것을 고르시오.
>
> (1) 함수는 오직 하나의 객체만 반환 할 수 있으므로 'return a,b' 와 같이 쓸 수 없다.
>
> (2) 함수에서 return을 작성하지 않으면 None 값을 반환한다.
>
> (3) 함수의 매개변수 (parameter) 는 함수를 선언할 때 설정한 값이며, 전달 인자(argument) 는 
>
> ​	함수를 호출할 때 넘겨주는 값이다.
>
> (4) 가변 인자를 설정할 때는 인자 앞에 * 을 붙이고, 이 때는 함수 내에서 tuple로 처리된다.

```python
# 1) 함수가 오직 하나의 객체만을 반환할 수 있는 것은 사실이나, return에 2개 이상의 변수를 전		달하면, 하나의 tuple 형태로 처리 되어 전달된다. 따라서 (1)은 오답이다.

# 2) return을 작성하지 않으면, None 값을 반환한다. print() 함수로 object가 출력되는것과, 	반환값이 있다는 것은 서로 다르다.
# 3) 
	def fuc (x): #x = parameter
        return x
   
fuc(2) # 2 = argument

# 4) 가변인자를 tuple 꼴이 아닌, dictionary 꼴로 받고 싶다면 ** 을 사용한다.
```



# 3. 재귀함수

> 재귀함수를 사용했을 때 얻을 수 있는 장점과 단점을 반복문과 비교하여 작성하시오.

```python
# 팩토리얼을 계산하는 함수 (ver. recursive)
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

```

```python
# 팩토리얼을 계산하는 함수 (ver.loop )
def fac_loop(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
        
```

* 장점 : 간단한 알고리즘 문제에 적용하면 쉽고 빠르게 만들 수 있음.
* 단점 : 직관적인 이해가 어려운 경우가 있고, 메모리 스택이 넘치거나, 실행속도가 느려지는 경우도 있음.

