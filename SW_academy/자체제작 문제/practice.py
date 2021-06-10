'''
풀이 과정 

1. 테스트 케이스마다 입력을 받는다.
2. 입력을 받으면서, 존재하는 물약과 바구니에 대한 정보 (종류 / 위치)를 저장한다.
3. (0,0) 위치를 초기값으로, 2에서 저장된 물약의 정보를 이용하여 초기위치에서 물약의 위치로 이동 할 수 있는지 확인한다.
    3.1 도달할 수 있다면, (0,0)에서 물약의 위치까지의 최단 거리와 물약의 위치를 변수화 한다.
    3.2 도달할 수 없다면, (0,0)에서 물약의 위치까지의 최단 거리와 물약의 위치를 None으로 변수화 한다.
4. 미로에 존재하는 모든 물약에 대하여 3을 수행한다.
5. 물약에 도달할 수 있는 경우 물약 위치까지의 최단거리를 저장하고, 현재 나의 위치를 물약의 위치로 변경한다.
6. 나의 새로운 위치와, 물약 위치까지의 최단거리를 초기 값으로 하고, 2에서 저장된 바구니의 위치로 이동 할 수 있는지 확인한다.
    6.1 바구니에 도달할 수 있는 경우, (시작위치 ~물약 위치)까지의 최단거리에 (새로운 내 위치 ~ 바구니)까지의 최단거리를 더하여 리스트에 저장한다.
7. 
8. 6과정으로 얻은 리스트의 최소값을 출력한다.
8.1 만약, 리스트가 비어있으면 IMPOSSIBLE을 출력한다.

'''

from collections import deque


def find_object_BFS(start:list,coor:tuple)->list:
    queue = deque()
    queue.append(start)
    visited = [[False] * 16 for _ in range(16)]

    while queue:
        x,y,step = queue.popleft()
        
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx,ny) == coor:
                return [(maze[nx][ny],step+1),(nx,ny)]

            if 0<=nx<16 and 0<=ny<16 and not(maze[nx][ny] == '1') \
                and not visited[nx][ny]:
                queue.append([nx,ny,step+1])
                visited[nx][ny] = True
    
    return [None,None]


TC = int(input())

for _ in range(TC):
    tc = int(input())
    maze = []
    potion_info = {}
    basket_info = {}

    for r in range(16):
        row = list(input())
        for c in range(16):
            if row[c] in ['r','g','b']:
                potion_info[row[c]] = (r,c)
            elif row[c] in ['R','G','B']:
                basket_info[row[c]] = (r,c)

        maze.append(row)

    MINIMUM_DISTANCE= []
    for elem in potion_info:

        potion_BFS_result = find_object_BFS([0,0,0],potion_info[elem])
        curr_location = potion_BFS_result[1]

        if curr_location:
            basket_color = potion_BFS_result[0][0].upper()
            basket_coor = basket_info.get(basket_color)
            potion_step = potion_BFS_result[0][1]
            my_coor = [curr_location[0],curr_location[1],potion_step]
            result = find_object_BFS(my_coor,basket_coor)

            if result[1] :
                MINIMUM_DISTANCE.append(result[0][1])

    if MINIMUM_DISTANCE:
        print('#{0} {1}'.format(tc,min(MINIMUM_DISTANCE)))
    else :
        print('#{0} {1}'.format(tc,'IMPOSSIBLE'))
