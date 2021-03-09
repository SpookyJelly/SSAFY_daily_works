from django.shortcuts import render

# Create your views here.
def index(request):
    # 별도의 네임스페이스를 지정해주면, templates 이후의 경로도 지정해줘야한다.
    # 네임스페이스를 지정해주면, views를 수정한다. (urls.py 아님!)
    return render(request,'articles/index.html')