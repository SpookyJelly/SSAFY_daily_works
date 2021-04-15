# 5202번 화물 도크

# 24시간 운영되는 물류센터에는 화물을 싣고 내리는 도크가 설치되어 있다.
# 0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면,
#  최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.
# 신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고,
#  앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.
# 예를 들어 앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능하다.

import sys
sys.stdin = open('5202_input.txt','r')


TC = int(input())

# 기본 아이디어.
# 각 시간표 대상으로 검증.
# 뒤에서 부터해야하나? 
for tc in range(1,TC+1):
    N = int(input())
    application_lst = [list(map(int,input().split())) for _ in range(N)]
    # 먼저 끝나는 녀석이 뒤로 가게끔 정렬. --> 최후미 친구는 가장 먼저 끝나는 녀석이 될 것이다.
    # 이렇게 정렬해야지 시작은 이른데, 종료가 늦는 쓰레기 작업들을 쳐낼 수 있다.
    application_lst.sort(key= lambda x : (x[1]),reverse=True)
    # 가장 먼저 끝나는 녀석의 작업 종료 시간
    end_time = application_lst.pop()[1]
    cnt = 1

    while application_lst:
        start,finish = application_lst.pop()
        # 일정을 하나 씩 살펴서, 다음 작업 시간 시간이 현재 작업종료시간 보다 크다면, 
        # 종료 시간을 갱신해주고, 도크 카운터를 하나 올린다. ( 작업 완료했다는 뜻)
        if end_time <= start:
            end_time = finish
            cnt += 1
    print('#{0} {1}'.format(tc,cnt))
        