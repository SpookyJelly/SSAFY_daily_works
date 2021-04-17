#1244번 최대 상금

# 기본 아이디어
# 재귀 DFS를 이용한 swap

import sys
sys.stdin = open('1244_input.txt','r')


# N번 스왚... 재귀함수를 이용하자
# 아무리 생각해봐도 이건 내가 혼자서 풀수가 없다...
# 일단 정답을 참조하고, 알고리즘을 이해해보도록 하자
# 이게 왜 D3인지 이해가 안가네
def solve(cnt):
    global ans, L
    if cnt == 0:
        temp = int("".join(num))
        if ans < temp:
            ans = temp
        return
    for i in range(L):
        for j in range(i + 1, L):
            # for문 두개 쓰는 이유?? 내가 재귀때 쓰는 level parameter 대신에 쓰는거 같다. level을 parameter로 쓰면 종료 조건은 level == cnt 가 되는데
            # level이 전체 인덱스보다 큰 경우도 있을 수 있으니까, 인덱스 문제 때문에 level 파라미터 대신에,cnt가 작아지는 (swap횟수는 어떻게든 채우는) 방식을 이용한거 같다
            num[i], num[j] = num[j], num[i]
            temp_num = "".join(num)
            # 방문 체크 => 처음 등장한 조합이면, (temp_num, cnt - 1):1 꼴로 visit에 추가
            if visit.get((temp_num, cnt - 1), 1):
                # 이후 0으로 초기화. 만약에 다음에 cnt-1번째 재귀때, temp_num가 나오게 된다면, get 명령에 의해서 value = 0 을 가져오게 되고,
                # 곧 if 문을 통째로 생략하게 됨.
                visit[(temp_num, cnt - 1)] = 0
                solve(cnt - 1)
            # 원상복귀
            num[i], num[j] = num[j], num[i]


for tc in range(1, int(input()) + 1):
    num, change = input().split()
    ans = -1
    num = list(num)
    change = int(change)
    # 나중에 추가해준 거 def 위에 있어야 global 먹힘..! 주의할 것
    L = len(num)
    visit = {}
    solve(change)
    print("#{} {}".format(tc, ans))
