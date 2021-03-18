from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # media 파일 새로 로드
    # 근데 이대로 다시 설계도 짜버리면, 기존에 올라가 있던 (그러니까 업데이트 전에) 게시글들은 사진 파일이 없어서
    # null 비슷하게 됨. 그래서 디폴트로 blank = True 옵션으로 빈값이라도 넣어준다.
    image = models.ImageField(upload_to="uploads/%Y/%m/%d",blank=True)