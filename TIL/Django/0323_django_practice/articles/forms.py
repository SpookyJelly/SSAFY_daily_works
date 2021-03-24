from django import forms
from .models import Article,Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article # 지금 이 게 가지고 있는 필드가 author, title, content 그래서 all 하면 다 튀어나온다.
        # 아 맞아 author 를 추가해줬지
        fields = ('title','content',)
        # exclude = ('title',)
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',) # comma please hehehe



