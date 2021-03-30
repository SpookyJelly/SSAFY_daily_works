from django.shortcuts import render,redirect
from .models import Question,Answer
from random import randrange

# Create your views here.
def index(request):
    all_question = Question.objects.all()
    my_pk = randrange(1,len(all_question)+1)

    # 질문과 그에 알맞는 답변을 꺼내는 단계
    question = Question.objects.get(pk=my_pk)
    answers = Answer.objects.filter(question=my_pk)

    # 투표의 총합을 정수형으로 구하고, 각 답변에 대한 투표율을 리스트화
    total = 0
    vote_values = answers.values('vote')
    vote_lst = [0 for _ in range(len(vote_values))]
    for idx in range(len(vote_values)):
        total += vote_values[idx]['vote']
        vote_lst[idx] = vote_values[idx]['vote']

    def percents(child,total):
        if child == 0:
            return 0
        else:
            return round((child*100)/total,2)

    # 각 정답에 대한 백분율을 구한 후, 그것을 percent 칼럼에 할당
    # 이때 주의 사항은 쿼리셋 데이터를 조작할 때는 변수로 저장한 다음에
    # 써야하는 것이다.
    percent_lst =[0 for _ in range(len(vote_values))]
    for idx in range(len(vote_lst)):
        answer_tem = answers[idx]
        percent_lst[idx] = percents(vote_lst[idx],total)
        answer_tem.percent = percent_lst[idx]
        answer_tem.save()

    context = {
        'question':question,
        'answers':answers,
        'total': total,
    }
    return render(request,'vote/index.html',context)


def counter(request,question_pk,answer_pk):
    if request.method =="POST":
        answer = Answer.objects.get(pk=answer_pk)
        answer.vote += 1
        answer.save()

        return redirect('vote:index')