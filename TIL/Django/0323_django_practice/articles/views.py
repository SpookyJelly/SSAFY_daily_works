from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm ,CommentForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid(): # meta에 지정한 fields만 검사함
            article = form.save(commit=False) # 근데 서버측에서는...전체를 본다. author는 어디 있니?를 물어보는데 # 사용자에게 보여주지 않았으니까 에러
            # title(ok)
            # content(ok)
            # author(????)
            # 그래서 commit = False 옵션을 주는 것. 실제 DB에 저장은 하지 않지만
            # form에 담긴 인스턴스를 반환합니다.
            article.author = request.user
            article.save() # DB에 이제야 저장
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm() # Comment 폼 생성

    comments = article.comment_set.all()
    context = {
        'article': article,
        'form':form,
        'comments':comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)

    # 게시글 작성자만 삭제할 수 있게 설정
    if article.author == request.user:
        article.delete()
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if article.author != request.user:
        return redirect('articles:index')

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
        

@require_POST
def create_comment(request,article_pk):
    # 1. 댓글을 가리킬 게시글을 가져옵니다.
    article = Article.objects.get(pk=article_pk)
    # 2. 사용자 입력값을 (댓글)을 꺼내서
    form = CommentForm(request.POST)
    # 3. 유효성 검사를 하고
    if form.is_valid():
    # 4. 저장합니다.
        comment = form.save(commit=False) # commit = False를 설정시 DB 저장 X
        comment.article = article
        comment.save() # 이시점에 DB 반영
    return redirect('articles:detail',article.pk)