import sys
sys.stdin = open('input(1_50).txt','r')
from collections import deque


def find_object_BFS(start: list, coor: tuple) -> list:
    queue = deque()
    queue.append(start)
    visited = [[False] * 16 for _ in range(16)]

    while queue:
        x, y, step = queue.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx, ny) == coor:
                return [(maze[nx][ny], step + 1), (nx, ny)]

            if 0 <= nx < 16 and 0 <= ny < 16 and not (maze[nx][ny] == '1') \
                    and not visited[nx][ny]:
                queue.append([nx, ny, step + 1])
                visited[nx][ny] = True

    return [None, None]


TC = int(input())

for _ in range(TC):
    tc = int(input())
    maze = []
    potion_info = {}
    basket_info = {}

    for r in range(16):
        row = list(input())
        for c in range(16):
            if row[c] in ['r', 'g', 'b']:
                potion_info[str(row[c])] = (r, c)
            elif row[c] in ['R', 'G', 'B']:
                basket_info[str(row[c])] = (r, c)

        maze.append(row)

    MINIMUM_DISTANCE = []
    for elem in potion_info:

        potion_BFS_result = find_object_BFS([0, 0, 0], potion_info[elem])
        curr_location = potion_BFS_result[1]

        if curr_location:
            basket_color = potion_BFS_result[0][0].upper()
            basket_coor = basket_info.get(basket_color)
            potion_step = potion_BFS_result[0][1]
            my_coor = [curr_location[0], curr_location[1], potion_step]
            result = find_object_BFS(my_coor, basket_coor)

            if result[1]:
                MINIMUM_DISTANCE.append(result[0][1])

    if MINIMUM_DISTANCE:
        print('#{0} {1}'.format(tc, min(MINIMUM_DISTANCE)))
    else:
        print('#{0} {1}'.format(tc, 'IMPOSSIBLE'))
