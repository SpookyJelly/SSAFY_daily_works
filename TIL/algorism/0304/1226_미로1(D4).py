# 1226번 미로 1

"""
아래 그림과 같은 미로가 있다. 16*16 행렬의 형태로 만들어진 미로에서
흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.

가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여,
가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.

주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
총 10개의 테스트케이스가 주어진다.
테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).
"""

# 핵심 : 델타 무브, DFS , 백트래킹 (DFS)로 구현, 움직일때마다 arr 자체를 수정

import sys

sys.stdin = open('1226_input.txt', 'r')


def DFS(maze, start):
    # stack 필요

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack = [start]

    # 이동하면서 maze 자체를 바꿀꺼라 visited는 필요 없다
    while stack:
        (r, c) = stack.pop()
        if maze[r][c] == '3':
            return 1

        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]

            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1':

                # 현재 코드는 다음 delta move 칸이 '1'이 아닌 경우, 다음 칸을 '1'로 바꾸고 이동한다.
                # 만약 바꾸는 부분이 '0'이라면 관계 없지만, 만약에 '3'이라면, 문제가 된다. 그래서 다음칸이 '3'인 경우는 pass를 해준다.
                if maze[nr][nc] == '3':
                    pass
                else:
                    maze[nr][nc] = '1'
                stack.append([nr, nc])

    return 0


"""
    for 이하의 구문은 아래와 같이 사용할 수 도 있다.

        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]

            # 이동한 칸을 '1'로 바꾸기 전에, 이 칸이 '3'인지 확인하는 과정이다.
            # 이 조건문으로 인하여, goal이 maze[nr][nc] = '1' 으로 바뀌는 것을 막을 수 있다.
            if maze[nr][nc] == '3':
                return 1


            if 0<=nr<N and 0<=nc<N and maze[nr][nc] == '0':

                    maze[nr][nc] = '1'
                stack.append([nr,nc])


"""

for _ in range(10):
    tc = int(input())
    maze = []
    N = 16
    for i in range(N):
        tem = list(input())
        if '2' in tem:
            start = [i, tem.index('2')]
        maze.append(tem)

    print('#{0}'.format(tc), end=' ')
    print(DFS(maze, start))
