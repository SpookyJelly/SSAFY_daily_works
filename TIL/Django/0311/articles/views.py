from django.shortcuts import render,redirect
from .models import Article


# Create your views here.
def index(request):
    article= Article.objects.all()
    context ={
        'articles' : article,
    }
    return render(request, 'articles/index.html',context)

def detail(request,article_id):
    # 1. article_id에 해당하는 게시글을 가져온다.
    # 2. context에 담아서 넘겨준다

    article = Article.objects.get(id=article_id)
    context ={
        'article' : article,
    }

    return render(request,'articles/detail.html',context)

def new(request):

    """
    사용자에게 게시글 작성 Form을 반환합니다.
    
    """

    return render(request, 'articles/new.html')

def write(request):
    """
    게시글 정보를 받아서 저장합니다.
    """
    # 1. form에 담긴 정보를 꺼낸다.
    title= request.POST.get('title') # new.html에서 작성한 name =title로 건너가는 내용들이 여기서 잡힌다
    content= request.POST.get('content') # new.html에서 작성한 name=content로 건너가는 내용들이 여기서 잡힌다
    # 2. 유효성 검사를 실시한다. (skip)
    # 3. 저장 후 응답
    article = Article(title=title, content= content)
    article.save()
    content = {
        'article' : article,
    }
    return redirect('articles:index') # 왼쪽에 있는건 app name / 오른쪽 이름은 name
    # return render(request, 'articles/write.html',content)

def delete(request,article_id):
    # 1. 삭제할 게시글을 불러온다.
    article = Article.objects.get(id=article_id)
    print(article)
    # 2. 삭제한다.
    article.delete()
    # 3. 메인 페이지로 리 다이렉트
    return redirect('articles:index')

def edit(request,article_id):
    # 1. 수정할 게시글을 가져온다.
    article = Article.objects.get(id=article_id)

    # 2. context에 담아서 보여준다.
    context ={
        'article':article,
    }
    return render(request,'articles/edit.html',context)

def update(request, article_id):
    # 1. 새로운 게시글 내용을 form에서 꺼냅니다.
    title = request.POST.get('title')
    content = request.POST.get('content')

    #2. 업데이트할 기존 게시글을 가져옵니다.
    article = Article.objects.get(id=article_id)

    #3. 기존의 게시글을 새로운 내용으로 바꿔줍시다.
    article.title = title
    article.content = content
    article.save() # DB 반영!
    return redirect('articles:detail', article.id)