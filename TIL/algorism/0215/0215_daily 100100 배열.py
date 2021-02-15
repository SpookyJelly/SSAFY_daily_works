# 문제해결 기본 2일차 - Sum
"""
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합,
각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
다음과 같은 5X5 배열에서 최댓값은 29이다.

"""


import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    t = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    # value2, value3 ==> 대각선 합을 받아주는 변수
    value2,value3 = 0,0
    N = len(arr)

    # 행 열 합중에서 최고값을 구하는 식
    # 대각선 합은 한칸씩 격자로 움직이므로, r과 함께 움직여도 무방하다
    # 가로 세로 구할때 maxi를 밖으로 빼라.. r/c 안에 넣으면 계속 초기화 된다.
    # r/c 한 루틴을 돌아야지 전체 행/열에 대한 최대값을 확인할 수 있는 것이다.
    # 혹여나 for r 문 안에 집어넣으면, 마지막 행/열 값만 나온다.

    maxi = 0
    for r in range(N):
        # value는 행의 합 / value1는 열의 합
        value,value1 = 0,0
        value2 += arr[r][r]
        value3 += arr[r][(N-1)-r]
        for c in range(N):
            value += arr[r][c]
            value1 += arr[c][r]
        if value > maxi:
            maxi = value
        if value1 > maxi:
            maxi = value1
        if value2 > maxi:
            maxi = value2
        if value3 > maxi:
            maxi = value3

    print(f'#{t} {maxi}')
