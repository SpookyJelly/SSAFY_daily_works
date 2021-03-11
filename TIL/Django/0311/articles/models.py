from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):

    #     '''
    #     객체의 표현식을 바꿔주는 메서드입니다.
    #     Admin 페이지에서 편하게 보기 위해 정의합니다.
    #     '''


    #     return f'{self.title} {self.content}'
    