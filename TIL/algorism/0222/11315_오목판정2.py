# 11315 오목판정

"""

N X N 크기의 판이 있다.
판의 각 칸에는 돌이 있거나 없을 수 있다.
돌이 가로, 세로, 대각선 중 하나의 방향으로
다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하라.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(5 ≤ N ≤ 20)이 주어진다.
다음 N개의 줄의 각 줄에는 길이 N인 문자열이 주어진다.
각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미한다.



[출력]

각 테스트 케이스 마다 돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”를 출력한다.
"""

# 2차원 배열 문제인데. 일단 값부터 받아보고 생각하자
# 입력을 받아야한다.

import sys
sys.stdin = open('11315_input.txt','r')


TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    # 문자열이라서 인덱싱하려면 그대로 input()으로만 받아도 되지만, 리스트로 받는게 더 나을 거 같다
    arr = [list(input()) for __ in range(N)]
    # 돌댕이 갯수 count해주는 cnt 변수를 리스트 순회하면서 받게 한다. 5개 이상이면 결과값을 +1 한다.
    result = 0
    cnt = 0

    # 행에 대한 검사
    for row in range(N):
        cnt = 0
        for col in range(N):
            if arr[row][col] == 'o':
                cnt += 1
            else:
                cnt = 0

            if cnt >= 5:
                result = 1
                break



    # 열에 대한 검사
    for c in range(N):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 'o':
                cnt += 1
            else:
                cnt = 0

            if cnt >= 5:
                result = 1
                break
    #print('열 검사 결과',result)
    # 대각선 모양 검사를 찾아내는데에, 굉장한 에로가 있었던 부분이다.
    # N의 크기에 따라, 오목이 완성되는 대각선이 여러개가 있을 수도 있다는 것!!
    # 그래서 a for문을 이용해서, N-4번 대각선을 검사해줘야한다...
    # 이 과정 때문에 괜히 잘 만들어진 행/열 검사 루틴만 건들였다.
    # 대각선이 하나만 존재할 것이라는 생각때문에 틀렸던 문제다.
    for a in range(N - 4):
        # 대각선 (정방) 검사
        cnt_up = 0
        cnt_down = 0
        for x in range(N - a):
            if arr[x][x + a] == 'o':
                cnt_up += 1
            else:
                cnt_up = 0
            if cnt_up >= 5:
                result = 1

            if arr[x + a][x] == 'o':
                cnt_down += 1
            else:
                cnt_down = 0
            if cnt_down >= 5:
                result = 1

    for a in range(N - 4):
        # 대각선(역방) 검사.
        cnt_up = 0
        cnt_down = 0
        for x in range(N - a):
            if arr[x + a][N - x - 1] == 'o':
                cnt_up += 1
            else:
                cnt_up = 0
            if cnt_up >= 5:
                result = 1

            if arr[x][N - x - 1 - a] == 'o':
                cnt_down += 1

            else:
                cnt_down = 0
            if cnt_down >= 5:
                result = 1



    if result:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
