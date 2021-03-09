from django.shortcuts import render

# Create your views here.
def signup(request):
    """
    1. 사용자가 장고 서버로 "회원 가입 폼"을 요청한다.
    2. 장고가 사용자에게 "회원가입 폼"을 응답한다.
    3. 사용자가 장고서버로 "회원가입 폼을 작성해서" 요청한다.
    4. 장고가 사용자에게 "회원가입 성공!" 페이지를 응답한다.
    """


    return render(request,'accounts/signup.html')

def result(request):
    # 1. 사용자가 Form 에 담아서 보낸 정보를 꺼낸다.
    username = request.GET.get('username')
    password = request.GET.get('password')
    password_confirm = request.GET.get('password_confirm')

    # 2. 사용자가 보낸 정보가 올바른지 확인한다.
    # (유효성 검사 == validation)
    # - 둘 다 빈 값이면 안됩니다.
    # - 아이디는 이메일 형식이어야 합니다.
    # - 비밀번호는 비밀번호 확인과 같아야 합니다.
    
    message = '회원가입에 실패했습니다'
    if (username and password and 
        password_confirm and password == password_confirm):
        message = '회원가입에 성공했습니다!'

    
    # 3. HTML 응답.
    context = {
        'message' : message,
    }
    """
    """
    return render(request,'accounts/result.html',context)