#5250번 최소비용


# 출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라
# 연료 소비량이 달라지기 때문에, 최적의 경로로 이동하면 최소한의 연료로 이동할 수 있다.
# 다음은 각 지역의 높이를 기록한 표의 예로, 항상 출발은 맨 왼쪽 위,
# 도착지는 가장 오른쪽 아래이며, 각 칸에서는 상하좌우 칸이 나타내는 인접 지역으로만 이동할 수 있다.
# (표에 표시되지 않은 지역이나 대각선 방향으로는 이동 불가.)
#
#
# 첫 줄에 테스트 케이스의 개수 T가 주어지고,
# 테스트 케이스 별로 첫 줄에 표의 가로, 세로 칸수N,
# 다음 줄부터 N개 지역의 높이 H가 N개의 줄에 걸쳐 제공된다.
# 1<=T<=50, 3<=N<=100, 0<=H<1000
#
# 최소 비용을 출력하시오

import sys
sys.stdin = open('5250_input.txt','r')
from collections import deque


def BFS(x, y, s):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque([[x, y, s]])

    while que:
        x, y, state = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # max 함수를 이용해서 0 이하로 나오는 경우 (가중치가) 0으로 고정시킨다
                weight = max(maps[nx][ny] - state,0) + 1
                if D[nx][ny]> D[x][y] + weight:
                    # 다음위치를 D에서 수정 / 수정 정도는 가중치 + 기본이동 1
                    D[nx][ny] = D[x][y] + weight
                    # 다음 state는 이전 위치에서의 연료소모량 + 가중치
                    # que.append([nx,ny,D[x][y]+weight])
                    que.append([nx, ny, maps[nx][ny]])

def BFS2(x, y):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque([[x, y]])

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # max 함수를 이용해서 0 이하로 나오는 경우 (가중치가) 0으로 고정시킨다
                if D[nx][ny] > D[x][y]:
                    # 다음위치를 D에서 수정 / 수정 정도는 가중치 + 기본이동 1
                    weight = max(maps[nx][ny] - maps[x][y], 0)
                    D[nx][ny] = D[x][y] + weight + 1
                    # 다음 state는 이전 위치에서의 연료소모량 + 가중치
                    # que.append([nx,ny,D[x][y]+weight])
                    que.append([nx, ny])
    return D[N-1][N-1]

TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    maps = [list(map(int,input().split())) for _ in range(N)]
    D = [[0xffff]* N for _ in range(N)]
    # print(D)
    D[0][0] = 0
    # print(maps)

    BFS(0,0,maps[0][0])
    # print(D)
    # print('#{} {}'.format(tc,BFS2(0,0)))
    print('#{} {}'.format(tc,D[N-1][N-1]))

# 제한시간 초과?
# deque로 바꾸니까 이번에는 런타임에러 🤬🤬🤬🤬🤬🤬🤬