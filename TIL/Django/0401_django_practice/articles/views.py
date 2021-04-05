from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.http import HttpResponse, HttpResponseForbidden
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # hashtag
            
            for word in article.content.split():
                # word : ex) 오늘 #장고 #많이 # 힘들다
                # 만약 #으로 시작하는 단어라면...해쉬태그!
                if word.startswith('#'):
                    # 해쉬 태그 테이블에 우선 새로운 데이터를 생성하고
                    # 근데 바로 create 해주면, 같은 해쉬 태그가 생기는 경우에는 UNIQUE함을 침해해서 에러가난다.
                    # 그래서 get_or_create라는 메서드를 써야한다.
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    # 방금 생성된 해쉬태그와 현재 게시글을 관계 지어준다.
                    article.hashtags.add(hashtag)

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
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()
                #update에서는 hashtage 관계를 초기화해줘야한다.
                article.hashtags.clear()
                for word in article.content.split():
                    if word.startswith('#'):
                        hashtag, created = Hashtag.objects.get_or_create(content=word)
                        article.hashtags.add(hashtag)
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
        # return HttpResponseForbidden()
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
        

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('articles:detail', article.pk)
        context = {
            'comment_form': comment_form,
            'article': article,
        }
        return render(request, 'articles/detail.html', context)
    return redirect('accounts:login')
    # return HttpResponse(status=401)


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        # return HttpResponseForbidden()
    return redirect('articles:detail', article_pk)
    # return HttpResponse(status=401)

def like(request, pk):
    # 1. 좋아요 누른 게시글 가져오기
    article = get_object_or_404(Article,pk=pk)
    
    # 2. 해당 게시글의 like_user에 add 하기
    # 2.1 게시글 좋아요 누른 유저 목록에 내가 없다면 추가하기

    # 여기서 filter로 받는 pk 는 누구 pk이냐...
    # like_users 매니저를 통해서 받기 때문에 user를 참조한다?
    if article.like_users.filter(pk = request.user.pk).exists(): # .exists() <-- 존재한다면
        article.like_users.remove(request.user) # like_user는 그럼 속성인가? 아니면 매니저인가?
        # like_users는 클래스 변수인데, descriptor라는 것을 써서 필드에 매니저를 추가 -> 장고가 내부적으로 처리해줘서
        # 클래스 변수를 매니저처럼 활용할 수 있게 해준다. 덕분에 ORM 처럼 사용할수도 있다.


    # 3. 게시글 좋아요 누른 유저 목록에
    # 내가 있다면 제거하기
    else:
        article.like_users.add(request.user)

    # 중계 테이블만 가져오기
    # 우리가 모델을 만들때는 안썼기에 장고가 알아서 through 옵션을 주는데,
    # 이렇게...메서드로도 활용 할수도 있다고?

    # article.like_users.through.objects.all()
    #        중개 테이블        #
    
    return redirect('articles:detail', article.pk)

def hashtag(request, hash_pk):
    tag = get_object_or_404(Hashtag,pk=hash_pk)

    context ={
        'tag': tag,
    }
    return render(request, 'articles/hashtag.html', context)