from django.shortcuts import render

# Create your views here.
def index(request):
    # 네임스페이스 별도 지정했으니, 경로 재지정
    return render(request,'pages/index.html')