### 05_Django_homework

---

* 아래 작성된 views.py의 코드 일부를 보고 문제에  알맞은 답을 서술하시오

```python
from django.shortcuts import render,redirect
from .forms import ArticleForm

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
   context={
       'form' = form,
   }
   return render(request,'articles/create.html',context)
```



1 . 왜 변수 context는 if else 구문과 동일한 레벨에 작성 되어 있는가?



- request가 POST 로 들어왔는데, 유효성 검사 ```is_valid()``` 를 통과하지 못한 경우, 해당 구문에서 에러 메시지를 binding 한 form 을 rendering 하여 return 하기 위해서이다.

  만약 해당 구문이 else 구문과 동일한 스위트에 있었다면, 유효성 검사를 통하지 못한 요청들은 return을 하지 못해 에러가 나던가, 같은 페이지만을 보여줄 것이다.



2. 왜 request의 http method는 POST 먼저 확인하도록 작성하는가?



* request 명령이 GET과 POST만 있는것이 아니기 때문이다. 만약에  else문에 POST 하도록 한다면, 다른 Fetch 등의 요청이 들어와도 DB를 수정할 수 있는 가능성이 생기기 때문이다.

