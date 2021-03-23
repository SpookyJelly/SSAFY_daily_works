from django.contrib.auth.forms import ( 
    UserChangeForm,
    AuthenticationForm,
    UsernameField,
    UserCreationForm,
    )
from django.contrib.auth import (
    get_user_model,
    )
from django import forms
# from django.utils.translation import gettext, gettext_lazy as _
class CustomUserChangeForm(UserChangeForm):
    password = None
    # 헐 맙소사...여기서 form 커스터마이징이 된다고???
    # widget 사용법을 좀 더 알아야겠는데.. // widget은
    first_name = forms.CharField(
        label='성',
        widget=forms.TextInput(
            attrs={
                'class': 'my-content form-control',
            }
        )
    )
    last_name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'my-content form-control',
            }
        )
    )
    email = forms.CharField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'class': 'my-content form-control',
            }
        )
    )    

    class Meta:
        User = get_user_model()
        model = User # 상위 클래스(UserChangeForm의 것)을 그대로 사용..하면 안된다?
        # UserChange에서 상속 받는건 그냥 유저 클래스 전체를 말한다.
        # 지금 나는 현재 활성화 중인 유저 모델을 넣어야하는거니까, get_user_model()이 필요한것!
        fields = (
            'email',
            'first_name',
            'last_name',
            ) # 보여줄 필드 찾는건 상속 부모 타고 올라가서, AbstractUser를 보면 있다.



class CustomAutheticationForm(AuthenticationForm):
    # UsernameField는 django.contrib.auth.forms 안에 있는 class이므로, 해당 주소에서 import하면 끝
    username = UsernameField(
        label='아이디',
        widget=forms.TextInput(
            # 굳이 widget에 attrs를 만드는 이유? 커스터마이징을 더 편하게 하기 위해서
            attrs={
                # 'autofocus': True, <-- 이 속성 주석처리해도 부모 클래스에서 상속 받고 있기에, 굳이 쓸 필요 없다.
                'class': 'form-control',
            }
            
            )
            
        )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                    'class': 'form-control',
                }
            ),
        )

    # # 이상하다...왜 에러메시지가 안뜰까...
    # error_messages = {
    #     'invalid_login': _(
    #         "Please enter a correct %(username)s and password. Note that both "
    #         "fields may be case-sensitive."
    #     ),
    #     'inactive': _("This account is inactive."),
    # }

    class Meta:
        User = get_user_model()
        fields = ('__all__')

class CustomUserCreationForm(UserCreationForm):
    username = UsernameField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )

    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                    'class': 'form-control',
                }
            ),
        )
    password2 = forms.CharField(
        label='비밀번호 재입력',
        widget=forms.PasswordInput(
            attrs={
            'class': 'form-control',
            }
        ),
    )

    class Meta:
        model = get_user_model()
        fields = ('username','password1','password2',)