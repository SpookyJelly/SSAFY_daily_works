from django.shortcuts import render
import requests
import random


# Create your views here.
def index(request):
    # 기본주소
    lotto_address = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='
    # 여기에 몇회차를 뜻하는 변수를 더해서 하나의 url로 만들자
    time = '953' # 이것도 웹에서 가져올 수 있을거 같은데...일단 넘어가자
    response = requests.get(lotto_address+time).json()

    # 미리 넣어둡시다. 몇번 당첨되었는지
    context = {
        '1st_cnt' : 0,
        '2st_cnt' : 0,
        '3st_cnt' : 0,
        '4st_cnt' : 0,
        '5st_cnt' : 0,
        'boom' : 0,
    }
    
    # 그럼 response는 dict꼴인데...
    # 로또 번호 정보는 drwtNo ~~ : 꼴의 키에 담겨있다.
    # 일단 확인해보자
    # 항상 뒤에 .json()을 붙였던거 같은데 안되서 text 해보니까 text도 되었다.
    ## 아 json() 맞다! 아까 출력 안된 이유는 .json으로 괄호 안붙이고 해서 임

    # response에서 필요한 정보만을 추려서 가져오는 과정.
    # for 문을 사용해서 context로 바꿔주자
    # 정규표현식 한번 써보고 싶었는데, 아쉽네
    for key in response:
        if 'drwtNo' in key or key == 'bnusNo':
            context[key] = response[key]


    lotto_num = [context['drwtNo1'],context['drwtNo2'],context['drwtNo3'],context['drwtNo4'],context['drwtNo5'],context['drwtNo6']]
    bouns_num = context['bnusNo']


    for _ in range(1000):
        ran_lst = random.sample(range(1,46),6)
        cnt = 0
        bouns = False
        # 여기까지 함수로 뺄 수 있을듯
        for idx in range(len(ran_lst)):
            if ran_lst[idx] in lotto_num:
                cnt += 1
            if ran_lst[idx] == bouns_num:
                bouns = True

        # 여기서 등수 체크 < -- 이걸 함수로 빼면 되겠다
        # 1등은 메인 6개 / 2등은 메인 5개 + 보너스 
        if cnt == 6:
            context['1st_cnt'] += 1
        elif cnt == 5 and bouns:
            context['2st_cnt'] += 1
        elif cnt == 5:
            context['3st_cnt'] += 1
        elif cnt == 4:
            context['4st_cnt'] += 1
        elif cnt == 3:
            context['5st_cnt'] += 1
        else:
            context['boom'] +=1
        


    # 가져와야할 번호 
    """
    1번 번호 : 4
    2번 번호 : 12
    3번 번호 : 22
    4번 번호 : 24
    5번 번호 : 33
    6번 번호 : 41
    보너스 : 38
    """
    # render는 기본적으로 경로에서 template/ 까지는 인식한다 자동으로
    return render(request,'lottos/index.html',context)

