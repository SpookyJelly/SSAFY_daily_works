from django import template

register = template.Library()

@register.filter
def hashtag_check(article):
    """
    article의 content를 파싱해서
    #으로 시작하는 단어들을 a 태그로 감싸줍니다.
    ex) {{ article.content|hashtag_check }} <-- 이런식으로 사용될것
    """
    content = article.content
    hashtags = article.hashtags.all()

    # hashtag를 잘 캐치를 못하는데, 이걸...개선해야할 필요가 있다
    # 여러 문자열이 겹치거나, 숫자가 들어가던가
    for hashtag in hashtags:
        content = content.replace(
            hashtag.content, 
            f"<a href='/articles/{hashtag.pk}/hashtag/'>{hashtag.content}</a>",
            )

    return content
