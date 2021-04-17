### 13_django_homework

---

> Modeling 편의점 상품 관리 프로그램을 제작하기 위해 모델링을 해야하는 업무가 주어졌다. 
>
> “모델링”은 개발해야 할 소프트웨어의 밑그림으로써 반드시 먼저 고려해야 할 중요한 요소 중 하나이다
>
>다음 조건을 참고하여 ERD와 models.py를 자유롭게 작성하고, 
>
>작성한 모델링에 대한 소개와 작성하게 된 이유에 대해 간략히 설명하시오
>
> 1) 지점별 편의점들이 존재한다.
>
> 2) 각 상품들은 특정 조건별로 분류 할 수 있다. 
>
>3) 단, User는 고려하지 않는다.
>
>



![](E:%5CGit%5CSSAFY_daily_works%5CTIL%5Chomeworkshop%5C0330_django%5C13_django_homework.JPG)





먼저 편의점 상품들은 크게 3가지로 나눌 수 있다고 생각했습니다.

1. 일반 상품들
2. 판촉물
3.  지점 한정 품목

세 품목은 모두 하나의 큰 군을 형성할것이기에 Charfield로 설정했습니다.

이 세가지를 베이스로 하여 추가 데이터 베이스를 확장했습니다.





1. 일반 상품

   일반 상품의 종류는 크게 5가지가 있다고 판단하였고, 각각은 부여된 로트 번호로 관리할 예정이므로, textfield를 사용했습니다.

   상품군 하나에 많은 통상품목들이 포함되므로 , 1:N 관계가 성립합니다

2.  판촉물은 있을수도 있고, 없을 수도 있기 때문에,  메인 테이블과 0-many 로 구성하였습니다.

   한편, 판촉물은 통상적으로  품목 재고 처리, 1등 상품에 대한 시장점유율 확보 목적 ,단기수익을 노린 한정 제품들을 위주로 푸시되므로,  일반 상품 중에서도 행사 상품이 나옵니다. 그렇기 때문에, 일반 상품 테이블과도 M:M 관계를 형성했습니다.

3. 한정품목

   한정품목은 일부 특수한 지점에서만 판매하는 품목들입니다. 시외지역에서 민가에 필요한 생필품등을 파는 경우도 있지만, 도시지역의 편의점은 취급하지 않기에, 0-1 line으로 구성하였습니다.