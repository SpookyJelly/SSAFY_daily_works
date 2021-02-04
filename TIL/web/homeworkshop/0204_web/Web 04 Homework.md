# Web 04 Homework

### 1. CSS flex-direction

> Flex box의 주축을 변경하는 flex-direction의 4가지 값과 각각의 특징을 작성하시오



```
* <style> display :flex 로 요소 타입을 flex로 설정한 후, flex-direction 속성으로 Flex box의 주축을 변경할 수 있다.

1. Flex-direction: row;
Flex container 내부의 item들을 X축 방향으로 정렬한다. item들은 정뱡향으로 정렬된다.

2. Flex-direction: row-reverse;
Flex container 내부의 item들을 X축 방향으로 정렬한다. item들은 역순으로 정렬된다.

3. Flex-direction : column;
Flex container 내비의 item들은 Y축 방향으로 정렬한다.(글이 쌓이는 방향) item들은 정방향으로 정렬된다.

4. Flex-direction : column;
Flex container 내부의 item들을 Y축 방향으로 정렬한다. item들은 역순으로 정렬된다.

```





### 2. Bootstrap flex-direction

> flex-direction의 4가지 요소와 대응하는 bootstrap 클래스를 작성하시오.



```
1. Flex-direction:row; 대응

- Class:"flex-row"

2. Flex-direction:row-reverse; 대응

- Class:"flex-row-reverse"

3. Flex-direction:column; 대응

- Class:"flex-column"

4. Flex-direction:column-reverse; 대응

- Class:"flex-column-reverse"
```





### 3. align-items

> align-items 속성의 4가지 값과 각각의 특징을 작성하시오



```
1. align-items:flex-start; : 플렉스 요소는 플렉스 컨테이너의 위쪽에 배치됩니다.

2. align-items:flex-end; : 플렉스 요소는 플렉스 컨테이너의 아래쪽에 배치됩니다.

3. align-items:center; : 플렉스 요소는 플렉스 컨테이너의 가운데에 위치합니다.

4, align-items:baseline; : 플렉스 요소는 플렉스 컨테이너의 기준선에 배치됩니다.

5. align-items:stretch; (기본) :플렉스 요소의 높이가 컨테이너와 동일하게 설정된 후, 연이어 배치됩니다.


```





### 4. flex-flow

> flex-flow 속성은 두가지 속성의 축약형이다. 올바르게 짝지어 진 것을 고르시오.



```
flex-flow는 flex-wrap과 flex-direction 속성을 한 줄에 표현하는 식이다.

flex-direction의 속성은 row,row-reverse,column,column-reverse 4가지가 있으며,

flex-wrap의 속성은 wrap, nowrap, wrap-reverse 3가지가 있다.
```





### 5. Bootstrap Grid System

> 하단 코드에 Bootstrap Grid System을 적용시키고자 할 때, A/B 각각에 입력해야할 클래스 이름을 작성하시오.



```html
<div class="container"> (a)
    <div class="row"> (b)
        <div class="col-(c)-(d)"></div>
    </div>
    
</div>
```





### 6.Breakpoint prefix

> Bootstrap Grid System에서 요소의 크기를 지정하기 위해서는 상단 코드와 같은 형태로 클래스 이름을 지정해야한다.
>
> 1) (c)에 들어갈 수 있는 값과 그 값들이 가지는 의미를 작성하시오.
>
> 2) (d)에 들어갈 수 있는 값과 그값들이 가지는 의미를 작성하시오.



1) (c)에 들어갈 수 있는 값은 grid-tier이다. 화면의 breakpoint가 들어가는 값으로, viewport가 일정 픽셀 이하가 되면 (d)의 크기로 바꾸라는 뜻이다.



2) (d)는 실제 item이 viewport에서 차지하는 영역을 수치화 한 것이다. Bootstrap의 Grid는 총 12개로 구성 되어있는데, 전체를 12개로 쪼개었을때, 몇 칸의 범위를 가질 것인지 명시하는 부분이다.