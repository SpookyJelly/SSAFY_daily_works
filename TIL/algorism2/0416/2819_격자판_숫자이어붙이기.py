#2819번 격자판 숫자 이어붙이기

# 4×4 크기의 격자판이 있다. 격자판의 각 격자칸에는 0부터 9 사이의 숫자가 적혀 있다.

# 격자판의 임의의 위치에서 시작해서, 
# 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서, 
# 각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다.

# 이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며,
# 0으로 시작하는 0102001과 같은 수를 만들 수도 있다.

# 단, 격자판을 벗어나는 이동은 가능하지 않다고 가정한다.
# 격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램을 작성하시오.

import sys
sys.stdin = open('2819_input.txt','r')

# def close_room_searcher(arr):
#     V_lst = [0]*16
#     # 델타 무브 상하좌우
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#     cnt = -1
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             cnt +=1
#             for idx in range(4):
#                 n_x = i + dx[idx]
#                 n_y = j + dy[idx]
#                 if 0<=n_x<4 and 0<=n_y<4 and arr[n_x][n_y] == arr[i][j]+1:
#                     V_lst[cnt] += 1
#     return V_lst

# 기본 아이디어 : 재귀하면서 얻은 value와 점핑 횟수를 다음 재귀에 계승하면서 값 찍어보기
# base case는 점핑을 6번 하였을때 == 여태까지 모은 value를 set 자료형에 집어넣는것.
# 이것을 모든 element에 대해서 시행하면 된다.
def snake(row,col,value,level):
    # 큐에 순회 횟수까지 넣어야겠는걸
    if level == 6:
        em.add(value)
        return
    # 상
    if 0<=row-1<4:
        snake(row-1,col,value+ square[row-1][col],level+1)
    # 하
    if 0<=row+1<4:
        snake(row+1,col,value+ square[row+1][col],level+1)
    # 좌
    if 0<=col-1<4:
        snake(row,col-1,value + square[row][col-1],level+1)
    # 우
    if 0<=col+1<4:
        snake(row,col+1,value + square[row][col+1],level+1)

TC = int(input())

for tc in range(1,TC+1):
    square = [list(input().split()) for _ in range(4)]
    em =set()
    for i in range(4):
        for j in range(4):
            snake(i,j,square[i][j],0)
    print('#{0} {1}'.format(tc,len(em)))