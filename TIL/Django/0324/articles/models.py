from django.db import models

# Create your models here.
class Article(models.Model):
    # 1
    title = models.CharField(max_length=100)
    content = models.TextField()


class Comment(models.Model):
    # N : Child Table
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # article의 pk 저장 // 필요 옵션 : 참조할 부모, on_delete : 데이터 무결성 위해서