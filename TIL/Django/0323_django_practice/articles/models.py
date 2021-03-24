from django.db import models
from django.conf import settings

# User 모델을 가져오는 방법
# 1. get_user_model() 호출 -> models.py 제외하고 모두 사용
# 2. settings.AUTH_USER_MODEL -> models.py에서만 사용
# 3. 직접 accounts.models에서 import (무시하세요. 전혀 쓸모없음)


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) # settings 자리가 유저 테이블 자리
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    # N : child Table
    content = models.TextField()
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
    )# article의 PK 저장
    
