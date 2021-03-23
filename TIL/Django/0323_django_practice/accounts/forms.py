from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model() # 활성화 유저 모델 가져옴

class CustomUserChangeForm(UserChangeForm):
    password = None # 부모 클래스인 UserChangeForm을 참조한것. 거기에 있는 password를 none으로 바꾼거시다.
    class Meta:
        model = User
        fields = ('email','first_name','last_name')