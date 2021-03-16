from django.shortcuts import render,redirect, get_object_or_404 # get_object_or_404 : 객체를 반환하던가 404 페이지를 보여줘라..이거야
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    # 1. DB에서 게시글 전부 가져옵니다
    article_list = Article.objects.order_by('-pk')
    # article_list = Article.objects.all()[::-1] 와 동일. 그러나 성능은 더 빠르다 (내림차순 정렬)

    # 2. context에 담아서 index.html으로 넘겨줍니다.
    context ={
        'article_list' : article_list,
    }
    
    return render(request,'articles/index.html',context)

def detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    get_object_or_404(Article,pk=article_pk) # 첫번째 인자는 클래스, 두번째 인자는 pk
    context = {
        'article' : article
    }
    return render(request,'articles/detail.html',context)


# new랑 create를 합친다?
def new(request):

    # request가 POST로 들어왔을때.
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터로 채운다 (binding)
        form = ArticleForm(request.POST)
        # form에 바인딩 된 데이터가 유효한지 검사한다
        # is_valid() 메서드는 참 거짓을 반환한다.
        # 만약 is_vaild()를 통과못하면, 자동으로 에러메시지가 바인딩 된다.
        if form.is_valid():
            # form.cleaned_data에서 검증된 데이터를 꺼냅니다.
            # cleaned_data는 유효성 검사를 통과한 데이터가 담긴 딕셔너리
            
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # Article.objects.create(title=title, content=content)

            # 근데 modelform을 만들어바리면 한줄에 된다고??
            # .save()는 인스턴스를 뱉어낼수도 있다. (모델 폼이기에 가능. 그냥 폼은 안된다.)
            article = form.save() # model form이기 때문에 가능하다
            return redirect('articles:detail', article.pk)

    # request가 GET으로 왔을때.
    else:
        # 비어있는 form 인스턴스를 생성한다.
        form = ArticleForm()

    context = {
        'form' : form,
    }
    return render(request,'articles/new.html',context)


#UPDATE
def update(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    # 으음.. 사용자가 진짜 수정하기 버튼 누르면 여기로 올라고 하는구나
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article) # instance로 수정할 게시글
        # 여기서 유효성 검사
        if form.is_valid():
            form.save()
            return redirect('articles:index')

        # 새로 작성도니 게시글 정보를 꺼내준다.
        # title = request.POST.get('title')
        # content = request.POST.get('content')



        # 기존 게시글의 내용에 덮어 쓰운다
        # article.title = title
        # article.content = content
        # article.save()
        # return redirect('articles:index')
    else: # form 태그의 요청이 GET일때 여기로 온다. // 사실 request.method == 'GET'과 동일한 부분이다.
        form = ArticleForm(instance=article)

    # 기존의 내용을 가져와서 넘겨준다.
    context ={
        'form' : form,
        'article' : article, #이렇게 update.html에 인자를 넘겨주던가
    }
    return render(request,'articles/update.html',context)



