from django.db import models
from django.conf import settings

# Create your models here.

class Hashtag(models.Model):
    content = models.TextField(unique=True)



class Article(models.Model):
    hashtags = models.ManyToManyField(
        'Hashtag',
        related_name='articles',
        blank=True, # 유효성 검사에서 제외하겠다는 의미...
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField( # 근데 ManyToManyField를 사용하지 않고 따로 중계 테이블만 달랑 만들어주면 .add .remove 같은 편하고 재미있는 메소드를 못쓴다. 그러니까 
        settings.AUTH_USER_MODEL, # M :N with models 
        related_name='like_articles', # For User Model
        through= 'Like', # 어떤 중계 테이블 이름을 직접 지정하겠다. // string으로 지정해줘야한다.
    )

    def __str__(self):
        return self.title

class Like(models.Model):
    """
    좋아요 기능을 위한 Aritcle과 User 모델 사이의 중계 테이블입니다.
    """
    # 뭐야, 여기 따옴표 안 써도 되네??

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)

class Comment(models.Model):
    # 따옴표 안쓰는 경우 : 모델 클래스를 직접 지원
    # 따옴표 쓰는 경우 : 재귀 관계가 필요할 때,
    # 아직 정의되지 않은 모델 참조할때,
    # 다른 응용 프로그램에서 모델을 참조하는 바로가기.
    # 따옴표 꼭 써줘야하는 경우: 위치상 아직 정의되지 않은 모델을 지정할 때 이다.
    # 그니까 여기서는 Article에서 comment가 들어가는 경우겠네
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
