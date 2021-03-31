### 12 Django_homework

---



#### 1. 1:N True or False

>  각 문항을 읽고 맞으면 T, 틀리면 F를 작성하고 틀렸다면 그 이유도 함께 작성하시오. 
>
> 1) ForeignKey는 부모 테이블의 데이터를 참조하기 위한 키이다. 
>
> 2) 1:N 관계에서 1은 N의 데이터를 직접 참조 할 수 있다. 
>
> 3) on_delete 속성은 ForeignKey 필드의 필수 인자이다.
>
>  4) 1:N 관계에서 외래 키는 반드시 부모 테이블의 PrimaryKey여야 한다.





1) T :  자식 테이블에서 부모 테이블의 유일한 값을 참조하기 위한 키로 사용된다

2) F : 1에서는 N과 관계를 맺고 있다는 필드(Foreign Key 필드)가 없기때문에 역참조를 해야한다. 이를 위해서는 ```[소문자 모델명 ]_set``` 꼴로 생긴 매니저를 이용해야한다.

3) T : 필수 인자이다. 대표적인 인자로는 models.CASCADE가 있다.

4) F : 반드시 부모 테이블의 PK일 필요는 없지만, 유일한 값을 참조해야한다는 규칙은 지켜야한다.





#### 2. ForeignKey column name

> 다음과 같이 이름이 articles인 app의 models.py에 작성된 코드를 바탕으로 테이블이 만들어 졌을 때, 데이터베이스에 저장되는 ForeignKey 컬럼의 이름과 테이블의 이름이 무엇인지 작성하시오.



```python
from django.db import models

class Quetion(models.Model):
    title = models.CharField(max_length = 50)
    
class Comment(models.Model):
    answer = models.ForeignKey(Quetion, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
```



Comment에 따로 related_name이 지정되지 않았으므로, 필드 이름은 quetion_id로 지정될 것이다

* 수정 : 필드 네임은 외래키 속성을 소문자_id 꼴로 지정되고, 테이블 이름은 앱 네임과 외래키를 사용하는 class를 소문자와의 조합으로 이루어진다.
* 따라서 정답은 , **fieldname = answer_id // tablename = article_comment**가 된다





#### 3. 1:N model manager

>  위 2번 문제 모델 관계를 바탕으로 어느 template 페이지가 다음과 같이 작성되어 있을 때, 질문(Question)에 작성된 모든 댓글(Comment)을 출력하고자 한다. 해당 template에서 Question 객체를 사용할 수 있다면 빈칸 __(a)__에 들어갈 알맞은 코드를 작성하시오.



* 해당 템플릿으로 따로 comment의 묶음을 보내주지 않았다면, 역참조를 이용해서 출력해야한다.

  models.py에서 사용하는 역참조 매니저 (ORM)을 태그로 쓸 수 있다는 사실에 주목해라



```django
{% for comment in Question.comment_set.all %}
	<p>{{ comment.content }}</p>
{% endfor %}
```



#### 4. next parameter

>다음과 같이 게시글을 삭제하는 delete 함수와 로그인을 위한 login 함수가 작성되어 있다. 
>
>만약 비로그인 사용자가 삭제를 시도한다면 django는 해당 사용자를 url에 next 파라미터가 붙은 login 페이지로 redirect 한다. 
>
>▪ /accounts/login/?next=/articles/1/delete/ 
>
>1) redirect된 로그인 페이지에서 로그인에 성공했을 때 발생하는 HTTP response status  code를 작성하고 발생한 원인과 해결을 위해 코드를 수정하시오. 
>
>▪ 게시글 삭제는 HTTP POST method로만 가능하다. 
>
>▪ 인증되지 않은 사용자는 메인페이지로 redirect 되어야 한다







* 문제는, delete 함수가 GET 요청을 처리하지 못한다는 것이다. next 쿼리로 처리되는 명령은 GET으로 처리되는데, login을 끝마치고 delete 함수를 시행하려고 하면, @require_POST 때문에 405 에러가 뜰 수 밖에 없는 것이다. 
* 문제 조건에 따르기 위해서는 (게시글 삭제는 POST로만, 비인가 사용자는 메인페이지로 redirect) 사용자 인증 하는 파트를 delete 함수 내부로 집어넣어야한다. 그렇기에, 다음과 같이 에러를 수정했다.



```python
@require_POST # 게시글 삭제는 POST로만 가능하기 때문에 유지
def delete(request, article_pk):
    if request.user.is_authenticated: # 사용자가 인증 되었다면, 삭제
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
    return redirect('articles:index') # 인증 된 사용자든, 안된 사용자든 결국 메인 화면으로 나간다.

```













