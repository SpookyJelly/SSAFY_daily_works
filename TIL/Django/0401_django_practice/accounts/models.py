from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 팔로우/ 팔로워는 M:N 관계 성립
    # 자기 자신을 넣을수도 있다고 들었고, symmetrical을 꺼줘야지 일방적인 관계가 된다고 한다.
    followings = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        )

