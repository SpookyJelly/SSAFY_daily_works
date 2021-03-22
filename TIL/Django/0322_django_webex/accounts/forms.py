from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

#get_user_model() 함수는 현재 장고 프로젝트에서
# 활성화된 유저 모델을 반환합니다.
User = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name')