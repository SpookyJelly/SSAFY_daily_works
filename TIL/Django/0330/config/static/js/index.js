
function react1(){

  var myRect = document.querySelector("#rect1");
  myRect.addEventListener("mouseover", function() {  // mouseover 이벤트 처리
    myRect.style.backgroundColor = "crimson";  // myRect 요소의 배경색 
  });
  myRect.addEventListener("mouseout", function() {  // mouseout 이벤트 처리
    myRect.style.backgroundColor = "";  // myRect 요소의 배경색 지우기 
  });
}
function react2(){

  var myRect = document.querySelector("#rect2");
  myRect.addEventListener("mouseover", function() {  
    myRect.style.backgroundColor = "Cyan";  
  });
  myRect.addEventListener("mouseout", function() {  
    myRect.style.backgroundColor = "";  
  });
}

function react3(){

  var myRect = document.querySelector("#rect3");
  myRect.addEventListener("mouseover", function() {  
    myRect.style.backgroundColor = "green";  
  });
  myRect.addEventListener("mouseout", function() {  
    myRect.style.backgroundColor = "";  
  });
}

function init(){

  react1();
  react2();
  react3();

}

init();
