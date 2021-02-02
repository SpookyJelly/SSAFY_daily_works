# Web_02_HomeWork



### 1. Semantic Tag

> 보기 중 콘텐츠의 의미를 명확히 하기 위해 HTML5에서 새롭게 추가 된 시맨틱(semantic) 태그를 모두 고르시오.

```
div, header,h1,section,footer,a,form,span
```

``` 
<article>  :  내용을 정의한다.
<header> : 문서나 섹션의 머릿글을 지정한다.
<h1> : 각 웹 콘텐츠 영역에서 제목을 표시할때 사용한 태그. / 페이지당 한번만 사용되는 것이 권장.
<section> : <header>,<footer>와 함께 문서의 구역을 정의한다.
<footer> : 문서 또는 섹션의 바닥글을 지정한다. (주로 저작권, 연락처 정보 등 내용이 삽임됨)
<form> : 사용자 입력을 정의한다. (semantic tag 아님)
```

* 시맨틱 태그는 사용자가 레이아웃을 설정할 때 도움을 주는 태그들이다. 있으나 없으나 문서의 형태나 모습은 변하지 않지만, 유지보수 하거나 다른 사람이 이 코드를 봤을때, 어디서부터 어디까지가 이 영역 안에 있는 태그인지 확인하는것을 돕습니다.





### 2. input Tag

> 아래 이미지와 같이 로그인 Form을 생성하는 HTML 코드를 작성하시오.
>
> 단, UserName 글자를 클릭하면 아이디를 입력하는 input에 PWD 글자를 클릭하면 비밀번호를 입력하는 input에 focusing 되도록 하시오.

```css
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <form action="random address">
    <label for="UserName">USERNAME :</label>
    <input type="text" placeholder="아이디를 입력해주세요." style="color: black;" autofocus>
    <div>
    <label for="PWD">PWD:</label>
    <input type="password" autofocus>
    <button>로그인</button>
    </div>
  </form>
</body>
</html>
```

📗 보완해야할 점.

* 글씨를 클릭하면 자동으로 focus 되는 방법은 잘 모르겠다.





### 3. 크기 단위

> 크기 단위 em은 요소에 지정된 상속된 사이즈나 기본 사이즈에 대해 상대적인 사이즈를 설정한다. 즉, 상속의 영향으로 사이즈가 의도치 않게 변경될 수 있는데 이를 예방하기 위해 HTML 최상위 요소의 사이즈를 기준으로 삼는 크기 단위는 무엇인가??



* 정답 : rem

  > rem 단위는 문서의 최상위 요소, 즉 html 요소의 크기를 기준으로 크기가 정해집니다.

  ```em``` 단위는 상위 요소 크기를 기준으로 크기가 정해진다.





### 4. 선택자

> 다음 예제를 통해 '자손 선택자'와 '자식 선택자'의 차이를 설명하시오.

```html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    div p{
      color : crimson;
    }
    div >p{
      color:aqua;
    }
  </style>
  
</head>
<body>
  <div>
    <p>자식 선택</p>
    <span>
      <p> 자손 선택</p>
    </span>
  </div>

</body>
</html>
```

* 결과

  > 자식 선택은 aqua 색, 자손 선택은 crimson 색상으로 출력 되었다.



자손 선택자는, div를 뿌리로 가지는 모든 p을 지정한다. 따라서, span이 부모인 p에게도 crimson 색상이 지정된다. 반면, 자식 선택자는 div를 직계 부모로 가지는 모든 p를 지정한다. 따라서, 자식 선택은 aqua 색상으로 지정된다.