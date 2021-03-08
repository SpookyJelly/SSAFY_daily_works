from django.shortcuts import render

# Create your views here.

def index(request):
    # 랜더는 첫번째 인자로 request, 두번째로는 HTML 경로를 적어줘야한다.
    
    # html 파일은 반드시 templates 폴더 안에 위치해야한다.
    # 근데 templates/index.html이라고 안해도 된다. templates는 자동으로 찾아줌
    articles =[
        {'title' : '1번 게시글',
        'content' : '1번 게시글 내용'},
        {'title' : '2번 게시글',
        'content' : '2번 게시글 내용'},
        {'title' : '3번 게시글',
        'content' : '3번 게시글 내용'},
    ]


    return render(request, 'index.html', {'articles' : articles,})

def detail(request,article_id):
    # article_id를 확인해보자
    # print('article_id ->',article_id)
    return render(request,'detail.html',{'article_id' : article_id})


def write(request):
    """
    form 태그가 담긴 
    게시글 작성페이지를 사용자에게 응답해줍니다.
    """
    return render(request, 'write.html')

def save(request):
    '''
    사용자가 작성한 게시글을 받아서 저장합니다.
    '''
    # print(request)
    # print(dir(request))
    # GET 요청으로 들어온 사용자 입력 정보가 담겨있는 유사 사전
    print(request.GET)
    title = request.GET.get('title')
    content = request.GET.get('content')
    context ={
        'title' : title,
        'content' : content,
    }
    return render(request,'save.html',context)