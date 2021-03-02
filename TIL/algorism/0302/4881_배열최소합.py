#4881번_ 배열 최소 합 (D2)

"""
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다.
단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.

예를 들어 다음과 같이 배열이 주어진다.

이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고,
이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10
"""
# 기본 아이디어 : 순열을 만들고, 그 순열을 인덱스 삼아 최소값을 구하는데, 백트레킹 기법을 활용하여, 가망이 없으면 드랍한다.

# 이렇게하면 타임 오버 되서 안됨, 그래서 백트래킹 사용한다.
# def per(k):
#     global minV
#     if k == N:
#         #print(sel) 이건 그냥 출력하겠다
#         sumV = 0
#         for i in range(N):
#             idx = sel[i]
#             sumV += BRD[i][idx]
#         print(sel,sumV)
#         if minV > sumV:
#             minV = sumV
#     else:
#         for i in range(N):
#             if not visited[i]:
#                 sel[k] = i
#                 visited[i] = True
#                 per(k+1)
#                 # 여기에서 Depth 깊어진다.
#                 visited[i] = False

import sys
sys.stdin = open('4881_input.txt','r')


def per(k, midV):
    global minV
    if minV < midV: # 중간값이 이미 최소값을 넘었다? -> 더 볼 필요 없다.
        return # return해서 값 받을것도 없다. 반환값없이 그냥 끝낸다.
    if k == N:
        if minV > midV:
            minV = midV
        # 얘들도 필요 없다....
        # sumV = 0
        # for i in range(N):
        #     idx = sel[i]
        #     sumV += BRD[i][idx]
        # print(sel,sumV)
        # if minV > sumV:
        #     minV = sumV
    else:
        for i in range(N):
            if not visited[i]:
                sel[k] = i
                visited[i] = True
                per(k+1,midV+BRD[k][i]) # 이게 무슨 말이냐? 새로운 중간값이 된다.
                visited[i] = False




TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    BRD = [list(map(int,input().split())) for _ in range(N)]
    # print(BRD)
    visited = [False] * N
    sel = [-1] * N
    midV = 0
    minV = 1e10000
    per(0,midV)
    print('#{0} {1}'.format(tc,minV))