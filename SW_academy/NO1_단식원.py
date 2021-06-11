import sys
sys.stdin = open('no1_input.txt','r')

# T씨발 시간 초과 원인이 뭐지
from copy import deepcopy

def DFS(duplicated_room,r,c):
    # if duplicated_room[r][c] == 2:
    #     for i in range(4):
    #         nr = r+ dr[i]
    #         nc = c+ dc[i]
    #         if 0<=nr<N and 0<=nc<M:
    #             if duplicated_room[nr][nc] == 0:
    #                 duplicated_room[nr][nc] = 2
    #                 DFS(duplicated_room,nr,nc)
    stack = [(r,c)]
    while stack:
        r,c = stack.pop()
        for i in range(4):
            nr = r+ dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M:
                if duplicated_room[nr][nc] == 0:
                    duplicated_room[nr][nc] = 2
                    stack.append((nr,nc))


def make_wall(start,wall):
    global max_zero
    if wall == 3:
        duplicated_room = deepcopy(room)
        for idx in range(len(chicken_list)):
            r,c= chicken_list[idx]
            DFS(duplicated_room,r,c)
        zeros = sum(i.count(0)for i in duplicated_room)
        max_zero = max(max_zero,zeros)

    
    for i in range(start , N*M):
        row = i // M
        col = i % M

        if room[row][col] == 0:
            room[row][col] = 1
            make_wall(i,wall+1)
            room[row][col] = 0


TC = int(input())

for tc in range(TC):
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    max_zero = 0
    chicken_list = []
    room = []
    N,M = map(int,input().split())
    for r in range(N):
        row = list(map(int,input().split()))
        for c in range(M):
            if row[c] == 2:
                chicken_list.append((r,c))
        room.append(row)
    make_wall(0,0)
    print('#{0} {1}'.format(tc+1,max_zero))