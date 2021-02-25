#2805번 농작물 수확하기 (D3)

"""

N X N크기의 농장이 있다.

이 농장에는 이상한 규칙이 있다.

규칙은 다음과 같다.


   ① 농장은 크기는 항상 홀수이다. (1 X 1, 3 X 3 … 49 X 49)

   ② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.

농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구하여라.


[제약 사항]

농장의 크기 N은 1 이상 49 이하의 홀수이다. (1 ≤ N ≤ 49)
농작물의 가치는 0~5이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 농장의 크기 N과 농장 내 농작물의 가치가 주어진다.


"""

# 접근방법 : 델타를 이용해서 이동. 가운데는 핀 포인트로 찍어서 한 열 통째로 더하기
# 그 이후로부터는 델타 이동할때마다 위 한 칸, 아래 한칸 자르기, 언제까지? 델타 이동이 N 끝까지 갈때까지

import sys
sys.stdin = open('2805_input.txt','r')

def BrokenArrow(arr):

    # 델타 이동 좌/우
    dr = [0,0]
    dc = [-1,1]
    mid = N//2
    result = 0
    for i in range(2):
        nx = mid
        ny = mid
        j =0
        while 0<=nx<N and 0<=ny<N:
            total = 0

            for idx in range(j,N-j):
                total += arr[idx][ny]
            if j == 0:
                first = total

            nx += dr[i]
            ny += dc[i]


            j+=1
            result += total

    return result-first






TC = int(input())

for tc in range(1,TC+1):
    N = int(input()) # 농장의 크기
    arr = [list(map(int,input())) for _ in range(N)]

    ans = BrokenArrow(arr)
    print('#{0} {1}'.format(tc,ans))



