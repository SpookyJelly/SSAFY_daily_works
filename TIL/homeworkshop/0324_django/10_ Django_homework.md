### 10_ Django_homework

---



#### 1. LookUp

>지문의 코드에서 ‘__gt’ 부분을 lookup이라고 한다. 링크를 참고하여 Django에서 사용 가능 한 lookup 세가지와 그 의미를 작성하시오.

```python
Entry.objects.filter(pk__gt=4)
```



* lookup은 SQL의 where 절과 동일한 요소이다. lookup은 쿼리셋 메서드인 ```filter()``` ,```exclude()``` ,```get()``` 에 키워드 인자 꼴로 전달이 된다.



lookup의 기본 형태는 ```필드이름__룩업타입=조건값``` 이다.



##### 대표적인 lookup의 종류 3가지

1. gt (GreaterThan)

   조건값 이상인 값들과 매치된다.

2. exact

   조건값과 정확히 일치 (대소문자 구분, 포함요소 없음) 하는 값과 매치된다.

3. iexact

   조건값과 일치하는 (대소문자 구분 없음) 값과 매치된다.



##### 2. 1:N 관계 설정

> 지문은 1:N 관계 설정을 하기 위하여 정의된 모델이다. 링크를 참고하여 빈 칸에 들어갈 수 있는 값 세가지를 선택 후 그 의미를 작성하시오. https://docs.djangoproject.com/en/3.1/ref/models/fields/

```python
class Comment(models.Model):
    content = models.CharField(max_length=100)
    article = models.ForeignKey(Article, on_delete=(a))
```



1. CASCADE : Comment를 참조하는 테이블이 삭제되면 같이 삭제된다.
2. PROTECT : Comment를 참조하는 테이블이 삭제되면 ProtectedError를 raise한다.
3. DO_NOTHING : Comment를 참조하는 테이블이 삭제되어도 아무것도 하지 않는다.







##### 3 . comment create view

>지문은 댓글 기능을 작성하기 위한 코드이다. 빈 칸에 들어갈 코드와 의미를 작성하시오.

```python
def comment_create(request, pk):
    Article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(__(a)__)
            comment.article = article
            comment.save()
            return redirect('articles:index')
```



* (a) : commit=False



통상적으로 .save() 메소드는 commit 옵션이 True로 설정되어있다. 이 말인 곧 즉, .save() 명령이 실행됨과 동시에 DB에 업로드가 된다는 것이다. 하지만 commit = False로 해두면, .save()의 return인 인스턴스는 반환을 해주지만, DB에 업로드를 하지 않는다. 이로서 , 인스턴스에 반드시 채워줘야할 필드값(여기서는 Foreign Key)을 채울 시간을 부여 받게 되는 것이다. 



그러면 여기서  "아니 그러면 ```form = CommentForm(request.POST)``` 에서 미리 Foreign Key를 받으면 되지 않나?" 라는 의문이 들텐데, 사실 그게 안된다. CommentForm의 부모 클래스인 BasemodelForm이 foreign key를 생성자 parameter로 받지 않는다. 



또한, ForeignKey로 테이블간의 관계를 맺는 것은, DB의 영역이다. 따라서, ORM을 사용해서 DB와 정보를 교환할수 밖에 없는것이다. ORM을 사용해야해서 CommentForm에 넣을 수 없는 것인지, CommentForm에 넣을수 없어서 ORM을 사용하는건인지에 대한 선후관계는 사실 묘연한 감이 없잖아 있는데, 여하튼 요지는, Foreign Key를 이용한 **RDB(관계형 데이터 베이스)** 구축은 ORM을 사용해야한다는 것이다.






##### 4. 1:N DB API

>게시물 아래에 댓글을 출력하려고 한다. Article과 Comment 모델이 1:N으로 관계설정 이 되어 있다고 가정 할 때 아래의 빈칸에 적절한 코드를 작성하시오.

```django
<h1>{{ article.title }}</h1>
{% for comment in __(a)__ %}
	<p>
       {{ comment.content }}
	</p>
{% empty %}
<p>
    댓글이 없습니다.
</p>
{% endfor %}
```



* 뜯어서 생각해보면 1의 관계를 가진 Article이, N의 관계를 가진 Comment 모델에 접근해야하는 상황이다. 1이 N을 참조하는 것은 ```역참조``` 이므로, ```_set``` 으로 이름 붙여진 manger를 기용해야 한 후, queryset ```all()```로 article을 참조하는 모든 comment를 불러와야한다.



* (a) : article.comment_set.all()



---

라고 생각했는데, 생각해보니 ORM은 python에서만 통하는 것이다. 지금 문제에서 주어진 부분은 Django HTML의 일부이다.  따라서 article.comment_set.all()은 작동하지 않는다.



정황상 게시글의 상세 내용을 보여주는 Detail 페이지인 것 같은데, 그러면 이미 views.py 에서 context에 여러가지 변수를 담아왔을 것이다. 그 context에 해당 게시글에 달린 댓글을 전부 담아서 하나의 변수에 넣어왔어야한다. 즉, 아래와 같은 코드가 이미 views.py에 작성 되어있어야했을 것이다.



```python
# 전략 #

article = get_object_or_404(Article,pk = article.pk)
comments = article.comment_set.all()

context ={
	'article':article,
	'comments':comments,
}

# 후략 #

```

