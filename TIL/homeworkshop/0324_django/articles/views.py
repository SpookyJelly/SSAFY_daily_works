from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article,Comment
from .forms import ArticleForm,CommentForm

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
        if form.is_valid():
            article = form.save()
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
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form':comment_form,
        'comments': comments
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
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
def comments(request,article_pk):
    # 1. 가져와야해... 사용자에게 보여줄 빈 폼을, <-- 이건 detail // 여기는 진짜 댓글 올리는 부분
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == "POST":
        # 2. 댓글로 우다다다 친 내용의 데이터 저장, 이제 comment와 링크
        form = CommentForm(request.POST)
        if form.is_valid():
            # 3. 임시 저장하고 인스턴스로 받는다
            comment_form = form.save(commit=False)
            comment_form.article = article
            comment_form.save()
            return redirect('articles:detail', article_pk)

# 밑에 else문은 필요없다. 댓글 작성은 항상 POST이기 떄문에, 보안적으로만 신경 쓰자

def comment_delete(request, article_pk, pk):
    # 1. 삭제 요청 POST를 받으면 일단 해당 아티클의 pk값에 맞는 객체를 가져온다.
    article = get_object_or_404(Article,pk=article_pk)
    # 2. 그 다음...댓글의 인스턴스를 뽑아야지 다만...현재 article에 속해있는 댓글 중 pk값이 일치하는것
    comment = article.comment_set.get(pk=pk)
    # 3. 삭제후 리턴
    comment.delete()
    return redirect('articles:detail', article_pk)