### 10_Django_workshop

---

> 제공된 템플릿 프로젝트에 이어서 댓글 생성/조회/삭제 코드를 작성하시오.



#### 1. Model

> 댓글 작성을 위한 테이블을 정의한다.



```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

```



* Comment 모델은 입력은 CharField로 받고,  Article 모델을 참조하는 관계로 구성되어 있으므로, ForeignKey를 설정해주었습니다.



```python
# forms.py

from django import forms
from .models import Article,Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('article',)
```



* 달성 목표 중에서 Comment를 출력해야하는 부분이 있으므로, 미리 form을 만들어서 불필요한 정보 ( article 필드가 살아있으면, 댓글 창에 어떤 게시글에 댓글을 달것인지 유저에게 선택권을 줍니다. 이는 사용자 경험 측면에서도 부적절하니 삭제했습니다.)







### 2. Comment Create

> /articles/<article_pk>/comments/ 댓글 작성 기능을 구현한다.



* views.py 작성에 들어가기 전에 꼭 생각해야하는 것은, 이 함수는 POST만을 담당한다는 것입니다. 
* 작성된 댓글의 출력은 detail 함수에서 구현이 되므로 (detail.html을 렌더링하면서 같이 출력이 되어야하니) 이번 Comment Create 함수는 댓글 작성 버튼을 클릭했을때, url로 요청을 보내고, 서버에 등록하는 POST 기능만 갖추는 것임을 명심해야합니다.



```python
@require_POST
def comments(request,article_pk):
    # 1. 사용자가 이 함수를 거치는 시점 : 댓글 등록 버튼 누른 직후
    # 그래서 각종 데이터가 request에 담겨서 샬랄라라라 날아온 상태.
    
    # 지금 댓글이 달리는 글의 인스턴스를 가져온다. --> 이후 ORM과 article_pk 전달에 요긴히 사용될 예정
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == "POST":
        # 2. 댓글로 우다다다 친 내용의 데이터 저장, 이제 comment와 링크
        form = CommentForm(request.POST)
        if form.is_valid():
            # 3. 임시 저장하고 인스턴스로 받는다
            comment_form = form.save(commit=False)
            comment_form.article = article
            comment_form.save()
            return redirect('articles:detail', article_pk)

# 밑에 else문은 필요없다. 댓글 작성은 항상 POST이기 떄문에, 보안적으로만 신경 쓰자

```





### 3. Comment Read

----

> 댓글 읽기 기능을 구현한다.
>
> 상세 페이지 하단에 댓글 목록을 출력한다.



* 여기서 핵심은 **상세 페이지** 라는 단어입니다. 이 말은 곧, ```이미 만들어놓은 detail 함수에서 몇가지 요소를 더 삽입해, 댓글 목록이라는 요소를 출력하라는 것```입니다. 따라서, 따로 url을 만들거나, 함수를 만들거나 할 필요가 없습니다다.

* 항상 어떤 기능을 만들때마다 url과 함수를 만들다보니 이렇게 기존 함수를 수정해야겠다는 생각을 못했습니다. 어떻게 보면 머리가 굳어버린게 아닐까 라는 생각도 듭니다.

* 여하튼, detail 함수를 수정하는데, 또 하나 주의해야할 점이 있습니다

  

**Detail.html은 비어있는 댓글 작성 form을 보여줌과 동시에, 여태까지 작성된 댓글들을 동시에 보여준다** 



따라서, views.detail이 html로 context를 넘길때, 비어있는 Commentform과 여태까지 작성된 comment를 모두 넘겨줘야합니다.



```python
@require_safe
def detail(request, pk):
    # 1. 현재 조회중인 글을 객체화하여 가져옵니다.
    article = get_object_or_404(Article, pk=pk)
    # 2. 비어있는 CommentForm을 생성합니다 --> detail 페이지에서 보여줄 예정
    comment_form = CommentForm()
    # 3. 현재 글 객체를 이용하여, comment 모델에 역참조를 합니다. all() 쿼리셋을 이용하여
   	# 참조 중인 모든 댓글을 가져옵니다.
    comments = article.comment_set.all()
    
    # 4. 이것들을 context에 꽁꽁 싸맨 뒤 detail.html로 넘깁니다.
    context = {
        'article': article,
        'comment_form':comment_form,
        'comments': comments
    }
    return render(request, 'articles/detail.html', context)

```



* detail.html

```django
  <a href="{% url 'articles:update' article.pk %}" class="btn btn-primary">[UPDATE]</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <button class="btn btn-danger">DELETE</button>
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
  <hr>
  <h3>댓글 목록</h3>
  <ul>
    {% for comment in comments %}
    <li>
      <form action="{% url 'articles:comment_delete' article.pk comment.pk%}" method =='POST'>
        {% csrf_token %}
        {{ comment.content }} 
        <input type="submit" value="삭제">
      </form>
    </li>
    {% endfor %}
  </ul>
  <hr>
  <form action="{% url 'articles:comments' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <button>제출</button>
  </form>
```

* comments 는 저장되어 있는 댓글들을 for 태그를 통해서 뱉어 냅니다.
* 비어있는 comment_form은 최하단에 표시되며, 작성된 글은 제출 버튼을 누르는 순간 {% url articles:comments %} 를 통해 이동합니다.



#### 4. Comment Delete

> articles//comments//delete/ 댓글 삭제 기능을 구현한다.



```python
def comment_delete(request, article_pk, pk):
    # 1. 삭제 요청 POST를 받으면 일단 해당 아티클의 pk값에 맞는 객체를 가져온다.
    article = get_object_or_404(Article,pk=article_pk)
    # 2. 그 다음...댓글의 인스턴스를 뽑아야지 다만...현재 article에 속해있는 댓글 중 pk값이 일치하는것
    comment = article.comment_set.get(pk=pk)
    # 3. 삭제후 리턴
    comment.delete()
    return redirect('articles:detail', article_pk)
```



* detail.html

```django
	
	<form action="{% url 'articles:comment_delete' article.pk comment.pk%}" method =='POST'>
        {% csrf_token %}
        {{ comment.content }} 
        <input type="submit" value="삭제">
      </form>
```

* 문제 조건에 따라 인수가 2개 들어가니, 해당 부분만 신경 써서 잘 전달해주면 된다.