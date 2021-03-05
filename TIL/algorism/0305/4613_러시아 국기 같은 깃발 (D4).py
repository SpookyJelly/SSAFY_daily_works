#4613 러시아 국기 같은 깃발 (D4)

"""

먼저 창고에서 오래된 깃발을 꺼내왔다.
이 깃발은 N행 M열로 나뉘어 있고, 각 칸은 흰색, 파란색, 빨간색 중 하나로 칠해져 있다.

당신은 몇 개의 칸에 있는 색을 다시 칠해서 이 깃발을 러시아 국기처럼 만들려고 한다. 다음의 조건을 만족해야 한다.

위에서 몇 줄(한 줄 이상)은 모두 흰색으로 칠해져 있어야 한다.
다음 몇 줄(한 줄 이상)은 모두 파란색으로 칠해져 있어야 한다.
나머지 줄(한 줄 이상)은 모두 빨간색으로 칠해져 있어야 한다.

이렇게 러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의 최솟값을 구하여라.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 두 정수 N,M(3≤N,M≤50)이 공백으로 구분되어 주어진다.
다음 N개의 줄에는 M개의 문자로 이루어진 문자열이 주어진다.
i번 째 줄의 j번째 문자는 깃발에서 i번째 행 j번째 열인 칸의 색을 의미한다.
‘W’는 흰색, ‘B’는 파란색, ‘R’은 빨간색을 의미한다. ‘W’, ‘B’, ‘R’외의 다른 문자는 입력되지 않는다.


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,
러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의 최솟값을 구하여 T 줄에 걸쳐서 출력한다.

"""

import sys
from pprint import pprint
sys.stdin = open('4613_input.txt','r')


# idx = 색깔의 인덱스 # sub_sum = 중간 합
def perm(idx, sub_sum):
    global ans
    # 유망성 검사를 실시한다.
    # sub_sum이 N (국기 전체의 크기)보다 크다면, 더 볼 필요도 없다. 종료한다.
    if sub_sum > N:
        return

    if idx == 3:
        if sub_sum == N:
            cnt = 0
            st = sel[0]
            st2 = st+sel[1]

            # 흰색 칠하기
            for i in flag[:st]:
                for j in i:
                    if j != 'W':
                        cnt +=1
            # 파란색 칠하기
            for i in flag[st:st2]:
                for j in i:
                    if j != 'B':
                        cnt += 1
            # 빨간색 칠하기
            for i in flag[st2:]:
                for j in i:
                    if j != 'R':
                        cnt += 1
            if ans > cnt:
                ans = cnt
        return
    for i in range(1,N-1):
        sel[idx] = i
        perm(idx+1,sub_sum+i)


TC = int(input())

for tc in range(1,TC+1):
    N,M = map(int,input().split())
    flag = [list(input()) for _ in range(N)]
    # pprint(flag)

    sel = [0]*3 # 칠할 수 있는 색깔의 갯수만큼의 배열을 만들어주자.
    ans = 999999 # 적당히 큰 숫자

    perm(0,0)
    print('#{} {}'.format(tc,ans))