# 재귀를 이용해서 풀었다.

import sys
sys.stdin = open('1861_input.txt','r')


# 상하좌우로 이동할 수 있어야하며,
# 이동하려는 방이 존재하는 것은 물론
# 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
# 어떤 방에 있어야 가장 많이 개수의 방을 이동할 수 있는지 구하라
def find_room(r, c, cnt, s):
    global ans # 가장 많이 지날 수 있는 방의 갯수
    global start_point # 방을 가장 많이 지나기 위해 시작해야할 지점

    # base case 1 : 여태까지 지나온 방이 가장 많이 지날 수 있는 방보다 커졌다
    if cnt > ans:
        ans = cnt # 그러면 ans랑 start_point 갱신해준다
        start_point = s
    
    # base case 2: 여태까지 지나온 방이 가장 많이 지난 방이랑 같다
    elif cnt == ans:
        # start_point를 비교하여, 시작했던 위치가 start_point보다 작다면 start_point 경신
        if start_point >= s:
            start_point = s
    for di in range(4):
        nr = r + dr[di]
        nc = c + dc[di]
        # 범위를 넘지 않으면서, 인접한 방이 현재 내 방 보다 딱 1 더 크다면
        if 0 <= nr < N and 0 <= nc < N and data[nr][nc] == data[r][c] + 1:
            # 재귀에 들어갈 자격이 생긴다.
            find_room(nr, nc, cnt+1, s)
 
 
for tc in range(1, int(input())+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
 
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
 
    ans = -1
    start_point = 0x9999999
 
    for i in range(N):
        for j in range(N):
            find_room(i, j, 1, data[i][j])
 
    print("#{} {} {}".format(tc, start_point, ans))