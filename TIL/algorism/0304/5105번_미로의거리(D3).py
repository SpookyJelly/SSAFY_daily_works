# 5105번 미로의 거리(D3)

"""
NxN 크기의 미로에서 출발지 목적지가 주어진다.

이때 최소 몇 개의 칸을 지나면
출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를,
경로가 없는 경우 0을 출력한다.

다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.

"""

import sys

sys.stdin = open('5105_input.txt', 'r')


# bfs와 dfs는 구조적으로 동일하다....(스택/큐의 경우)
# dfs는 재귀로도 구할 수 있음을 기억하자.
def bfs(graph, start, goal):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 몇 단위로 왔는지 확인하는 변수를 만들까?
    # 변수를 만들어도 좋고, visited 자체를 0 행렬로 만든 후, 거기에 단위 이동을 새기는 식으로 운용해도 된다.
    visited = [[False for _ in range(N)] for __ in range(N)]

    # queue의 시작형태가 굉장히 이상한데, [[r,c,counter]]꼴을 만들기 위해서 설계한 것이다.
    # counter는 함수 내에서 정의된 변수라, 이를 외부에서 잡은 arugment와 합치는데 조금 애로했다.
    counter = 0
    queue = [start + [counter]]

    visited[start[0]][start[1]] = True

    while queue:

        # 튜플 꼴로 만들면, 각 요소에 대해 이름을 붙일 수도 있고, 변하지 않는 값으로 지정하기 용이하다
        (r, c, counter) = queue.pop(0)

        if [r, c] == goal:
            # -1 해주는 이유는, 문제 조건에 따라, 몇개의 칸을 지나야 3에 도달하는 지를 파악하기 위해서이다.
            # 3까지 도달하는데 움직이는 횟수를 구하는 것이 아니다
            return counter - 1

        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            # 방문한적이 없고, 그래프에서도 벽이 아니라면
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and graph[nr][nc] != 1:
                queue.append([nr, nc, counter + 1])  # [nr,nc,counter+1]
                visited[nr][nc] = True
    return 0


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    maze = []
    for i in range(N):
        tem = list(map(int, input()))
        if 2 in tem:
            start = [i, tem.index(2)]
        if 3 in tem:
            goal = [i, tem.index(3)]
        maze.append(tem)

    print('#{0}'.format(tc), end=' ')
    print(bfs(maze, start, goal))
