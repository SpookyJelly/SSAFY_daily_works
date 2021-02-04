# Web_01_workshop

### 1.img tag

> 아래 그림과 같은 폴더 구조가 있다. resume.html에서 코드를 작성 중일 때, image 폴더 안의 my_photo.png를 보여주는 <img> tag를 작성하시오. 단, 이미자가 제대로 출력되지 않을 때는 ssafy 문자열이 출력 되도록 작성하시오.



```html
<--!> 절대경로 사용 방식</--!>
<img src = "C:\Users\Windows 10\Desktop\TIL\ssafy\image\my_photo.png" alt ="ssafy">

```

1. html 에서는 주소를 표시할 때는, \가 아닌 /를 사용한다.

   1.5 이 이야기가 나온 배경이 윈도우가 경로 구분할때 ￦ 표시를 쓰는데, 리눅스가 \를 사용한다.

   ​		그래서 나온 것 같다. 요지는 상대 경로를 사용할때 / 를 사용해라...

2. 절대주소는 전체의 주소를 다 적어 경로를 표시하는 방식이다. 현재 파일의 위치에 영향을 받지 않는다는 장점이 있지만, 작성하기에 불편함이 있다.



```html
<--!> 상대경로 사용 방식</--!>
<img src = "../image/my_photo.png"
```

* 현재 실행중인 파일의 위치를 기준으로 목적지의 위치까지만을 서술하는 방식이다
* 상대 주소는 작성의 간편함이 장점이지만, 파일의 위치가 변하게 되면 오류가 난다.





### 2. 파일 경로

> 위와 같이 경로를 (a) : 절대 경로 로 작성할 시, github에 업로드 하거나, 전체 폴더의 위치가 변경 되었을 때 이미지를 불러 올 수 없게 된다. 이를 해결하려면 이미지 경로를 (b) : 상대 경로로 바꾸어 작성하면 된다.



* 상대경로로 변경한 코드 : 상기 기재



### 3.Hyper Link

> 출력된 my_photo.png 이미지를 클릭하면 ssafy.com으로 이동하도록 하시오.



```html
<--!> 상대경로 사용</--!>
<a href ="www.ssafy.com"><img src = "../image/my_photo.png"></a>
```





### 4. 선택자

> 1) 아래의 코드를 작성하고 결과를 확인하시오.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    #ssafy > p:nth-child(2){
      color :red;
    }
  </style>
</head>

<body>
  <div id ="ssafy">
    <h2>어떻게 선택 될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>
  </div>
</body>
</html>
```

* ""첫번째 단락" 이 붉은 색으로 표시 된다.



> 2) nth-child를 nth-of-type으로 변경하고 결과를 확인하시오.

```html
  <style>
    #ssafy > p:nth-of-type(2){
      color :red;
    }
  </style>
```



* "두번째 단락"이 붉은색으로 표시된다



> 3) 작성한 코드를 참고하여 nth-child()와 nth-of-type()의 차이점을 작성하시오.

* nth-child()는 부모의 n번째 자식인 요소를 선택하는 선택자이고.
* nth-of-type()은 같은 유형의 n번째 형제를 선택합니다.



```nth-of-child```

* 부모의 n번째 자식을 찾고 해당 element 선택
* 다른 element 모두 자식으로 선택하여 자식들 중 n번째를 찾음
* 부모의 n번째 자식이 해당 element가 아니면 선택되지 않음



```nth-of-type```

* 부모의 n번째에 해당하는 element 선택
* 다른 element들이 있어도 모두 자식으로 선택되지 않고, 해당 element만 선택되어 n번째를 찾음



