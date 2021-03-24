from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model() # 활성화 유저 모델 가져옴



class CustomUserCreationForm(UserCreationForm):
    '''
    UserCreationForm을 커스터마이징 하는 이유는 UserCreationForm이 장고
    내장 User 모델을 가리키기 때문입니다

    '''
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields +('email',)
        #       username,password,password_confirm <= email 추가




class CustomUserChangeForm(UserChangeForm):
    password = None # 부모 클래스인 UserChangeForm을 참조한것. 거기에 있는 password를 none으로 바꾼거시다.
    class Meta:
        model = User
        fields = ('email','first_name','last_name')