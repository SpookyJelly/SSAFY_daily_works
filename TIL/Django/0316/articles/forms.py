#Django의 form은 크게 3부분을 처리해줍니다
# 1. 렌더링을 위한 데이터 준비
# 2. 데이터에 대한 HTML form 태그 생성
# 3. 클라이언트 (사용자)로부터 받은 데이터 수신 및 처리

# Django Form 시스템의 핵심은 재사용과 유효성 검사입니다.
# 1. 재사용 가능한 HTML Form을 자동으로 만들어줍니다.
# 2. 폼에 담긴 데이터 (사용자 입력값)을 알아서 검증해줍니다.

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    '''
    field : 실제 HTML input 태그의 데이터 타입을 지정
    widget : 실제 HTML input 태그의 모습
    
    ModelForm은 이미 정의한 Model을 이용하여 Forms 시스템을 더욱 쉽게 사용하게 해주는 기능입니다.
    '''
    # Django의 클래스 // ModelForm 이랑 세트이다. 
    # 변수명은 model / field로 해줘야지 쟝고가 인식한다.


    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': "my-title",
                'placeholder': '제목을 입력해주세요~!',
            }
        )
    )
    
    content = forms.CharField(
        label = '본문',
        widget=forms.Textarea(
            attrs={
                'class': "my-content",
                'placeholder': '본문도 입력해주세요~!',
            }
        )
    )


    class Meta:
        model = Article # 어떤 모델인지 명시
        fields = ('title','content',) # 위에 작성한 모델(클래스)의 필드 중에서 보여줄것만 작성
        # '__all__'을 fields에 집어넣어도 장고가 잘 인식한다.

    # # 변수 이름이 그대로 label이 된다
    # title = forms.CharField(max_length=100)

    # # 파이썬이 한글 변수명을 지원하니까 한글 변수로 하면 그대로 web에 한글이 뜬다!
    # # 근데 이게 Form의 변수가 되니까, form 가져다 쓴 곳에서는 잘 확인해야한다.
    # content = forms.CharField(widget=forms.Textarea)
