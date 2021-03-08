import random
from django.shortcuts import render

# Create your views here.
# 2단계. views.py 수정
def lottos(request): 
    num = range(1,46) 
    #py 파일은 그냥 파이썬 문법이 전부 통한다! sample 메서드를 이용하면 리스트꼴로 반환되는것 까지 똑같다!!
    pick = random.sample(num,6) 
    context ={
        'pick' :sorted(pick),
    }

    # 변수를 보낼 때는 dic 꼴로 보내라.
    return render(request,'lotto.html',context)