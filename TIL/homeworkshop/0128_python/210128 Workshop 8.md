# 210128 Workshop 08

### 도형 만들기

> 아래의 명세를 읽고 Python 클래스를 활용하여 점(Point)과 사각형(Rectangle)을 표현하세요



# **설명 생략**



```python
class Point:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
```



* 결과(수정 전)

```python
class Point:
    def __init__ (self,x,y):
        self.x = x
        self.y = y

class Rectangle(Point):

    def status(self):
        print(f'x 값 :{self.Point1.x},{self.Point2.x}')
        print(f'y 값 :{self.Point1.y},{self.Point2.y}')
        pass
    
    def __init__(self,Point1,Point2):
        self.Point1 = Point1
        self.Point2 = Point2
        pass
    
    def get_area(self):
        Point1_x = self.Point1.x
        Point1_y = self.Point1.y
        Point2_x = self.Point2.x
        Point2_y = self.Point2.y
        print(abs(Point2_x - Point1_x) * abs(Point2_y - Point1_y))

    def get_perimeter(self):
        Point1_x = self.Point1.x
        Point1_y = self.Point1.y
        Point2_x = self.Point2.x
        Point2_y = self.Point2.y
        length = abs(Point2_x - Point1_x)
        height = abs(Point2_y - Point1_y)
        print(2*(length + height))

    def is_square(self):
        Point1_x = self.Point1.x
        Point1_y = self.Point1.y
        Point2_x = self.Point2.x
        Point2_y = self.Point2.y
        length = abs(Point2_x - Point1_x)
        height = abs(Point2_y - Point1_y) 
        if length == height:
            return True
        return False


p1 = Point(4,3)
p2 = Point(1,2)
print(p1.x,p1.y)
print(p2.x,p2.y)
R1 = Rectangle(p1,p2)
R1.status()
print(R1.get_area())
print(R1.get_perimeter())
print(R1.is_square())
```



* 출력은 잘 되는데, 코드가 중복되는 부분도 많고, 너무 길다!
* 그래서 이걸 어떻게 줄일수 있을까...고민을 하면서 여러가지 실험을 해봤다



* 수정 코드

```python
class Point:
    def __init__ (self,x,y):
        self.x = x
        self.y = y

class Rectangle(Point):
    def status(self):
        a = self.x
        b = self.y
        print(f'x 값 :{a.x},{b.x}')
        print(f'y 값 :{a.y},{b.y}')
    
    
    def get_area(self):
        a = self.x
        b = self.y
        return abs(a.x - b.x) * abs(a.y - b.y)

    def get_perimeter(self):
        a = self.x
        b = self.y
        length = abs(a.x - b.x)
        height = abs(a.y - b.y)
        return 2*(length + height)

    def is_square(self):
        a = self.x
        b = self.y
        length = abs(a.x - b.x)
        height = abs(a.y - b.y) 
        if length == height:
            return True
        return False


p1 = Point(1,3)
p2 = Point(3,1)
r1 = Rectangle(p1,p2)
r1.status()
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3,7) # 1️⃣
p4 = Point(6,4) # 2️⃣
r2 = Rectangle(p3,p4) #3️⃣
r2.status()
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

```

>Rectangle 클래스가 Point 클래스의 상속을 받는다는 점을 생각해봤다.
>
>Rectangle가 Point 클래스를 끌어오면서 *__init__* 도 가져온다. 근데, point의 init은 초기 변수로 (x,y)를 받고,
>
>그 x,y가 각각 인스턴스 변수가 된다.



>코드를 해석하자면, Point 클래스는 (self,x,y)의 매개변수를 받는 클래스이다.
>
>1️⃣은 p3 --> p3.x = 3 , p3.y =7 을 가진 객체이다.
>
>2️⃣는 p4 --> p4.x = 6, p4.y =4 를 가진 객체이다.
>
>Rectangle은 Point를 상속 받으므로 __init__ 에서 (self,x,y)의 매개변수를 받는 클래스가 된다.
>
>근데, 3️⃣에서 x자리에 p3, y자리에 p4가 들어간다.
>
>그러므로, 3️⃣의 init은 아래 코드와 같다고 할 수 있다.
>
>```python
>class Rectangle:
>    def __init__ (self,p3,p4):
>        self.x = p3
>        self.y = p4
>       
>        
>        '''
>        p3는 Point 클래스이므로, 이미 .x / .y 라는 값을 가지고 있음.
>        마찬가지로, p4도 이미 .x / .y 라는 값을 가지고 있음
>        
>        p3.x --> 1️⃣에 따라 3
>        p3.y --> 1️⃣에 따라 7
>        p4.x --> 2️⃣에 따라 6
>        p4.y --> 2️⃣에 따라 4
>        
>        
>        '''
>```
>
>* 말이 자꾸 빙빙 도는데, 결국 내가 생각하기에는, Point를 상속받은 Rectangle 클래스의 변수로 Point 클래스가 들어가는것 같다. 그래서 타이핑을 줄일수 있었다고 생각.
>*  상당히 혼란스럽다...



### 더 알아봐야 할 점

```python
        a = self.x
        b = self.y
        
        # 얘들도 반복되는데, 얘들도 한번만 타이핑 할 수는 없을까?
```



* 클래스를 사용하는 이유

  1) 구조화 된 프로그램 설계 가능

  2) 설계가 잘 된 프로그램은 유지보수, 기능 추가가 용이

