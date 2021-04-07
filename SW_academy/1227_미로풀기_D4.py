# #아래 그림과 같은 미로가 있다. 100*100 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.

# 가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.

# 주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.
#
# [입력]
#
# 각 테스트 케이스의 첫 번째 줄에는 테스트케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
#
# 총 10개의 테스트 케이스가 주어진다.
#
# 테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.

import sys
sys.stdin = open('1227_input.txt')
from collections import deque

def bfs(start:list):
    queue = deque([start])
    #델타 무브 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x,y = map(int,(queue.popleft()))
        if [x,y] == goal:
            return 1


        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0<=new_x<100 and 0<=new_y<100 and maze[new_x][new_y] != '1':
                queue.append([new_x,new_y])
                maze[new_x][new_y] = '1' # 방문처리

    return 0


for _ in range(1,11):
    tc = int(input())
    maze,start,goal = [], [], []

    for row in range(100):
        tem = list(input())
        if '2' in tem:
            start = [row,tem.index('2')]
        if '3' in tem:
            goal = [row,tem.index('3')]
        maze.append(tem)
    print('#{0} {1}'.format(tc,bfs(start)))