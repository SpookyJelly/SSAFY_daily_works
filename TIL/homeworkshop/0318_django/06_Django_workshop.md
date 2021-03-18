### 06_Django_workshop

---



### 1. Media file with HTML input

---

```html
<form action="#" method ="POST" enctype="multipart/form-data">
    <label for= 'data'>UPLOAD:</label>
	<input type='file' name='data' id='data' accept="image/*,.pdf">
</form>
```



1.  multipart 태그의 작동 원리가, 요청을 미디어 부분/ 문서 부분 두 part로 쪼개서 multipart라는 이름이 붙었다고 한다. 쓰면서 익숙해지자
2.  accept 태그의 속성 값: 
   * 닷 (.)으로 시작되는 파일 확장자  (ex.  .png, .hwp ...)
   * audio/* : 모든 타입의 오디오 파일
   * video/* : 모든 타입의 비디오 파일
   * image/* : 모든 타입의 이미지 파일
   * 미디어 타입 : parameter를 가지지 않는 유효한 미디어 타입