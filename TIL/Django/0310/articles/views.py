from django.shortcuts import render,redirect
from .models import Articles # 이건 장고 문법이다. .--> 현재 위치의 models로부터 불러온다

# Create your views here.

def index(request):
    # articles = Articles.objects.all()
    articles = Articles.objects.order_by('-created_at')
    context = {
        'articles' : articles,
    }
    return render(request,'articles/index.html',context)


def new(request):
    return render(request,'articles/new.html')

def write(request):
    # 1. form에 담긴 정보를 꺼낸다.
    title = request.GET.get('title')
    content = request.GET.get('content')


    # 2. 정보가 유효한지 검사한다 (오늘은 생략)
    # 3. 저장한다.
    article = Articles()
    article.title = title
    article.context = content
    article.save()

    return redirect('articles:index') #/articles/

    # context = {
    #     'article':article # article 객체 (title, context 속성 보유)

    # }
    # return render(request, 'articles/write.html',context)
