from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 1. 모델 정의
    # 2. python manage.py makemigrations
    # 3. python manage.py migrate
    # 4. 마이그레이션 반영 최종확인
    # - python manage.py showmigrations