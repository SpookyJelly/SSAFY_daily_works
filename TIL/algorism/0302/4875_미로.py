# 4875번 미로 (D2)

"""
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지
확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.

주어진 미로 밖으로는 나갈 수 없다.
다음은 5x5 미로의 예이다.


13101

10101

10101

10101

10021



마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐
미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

[출력]


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,
계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

"""

import sys

sys.stdin = open('4875_input.txt','r')

# 기본 아이디어.
# 스택에 현재 위치 넣기 -> 스택의 마지막 값 뽑기 -> 뽑은 위치 방문표시하기 -> 현재위치에 대해 4방향 탐색 -> 갈수 있으면 그 위치 스택에 넣기

def delta(stack):
    # 상 하 좌 우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    stack.append(S) 
    visited[S[0]][S[1]] = True
    while stack:
        way = stack.pop()
        # 가독성 향상 방안
        #(nr,nc) = stack.pop() <-- pop 뽑으면 튜플로 나오기 때문에
        nr= way[0]
        nc= way[1]
        # 뽑은 값 체크
        if maze[nr][nc] == '3':
            return 1

        for i in range(4):
            # 여기 방향 바뀔때마다 다시 원래 값으로 돌아오도록 설계해야한다.
            nr = way[0] # 처음에 이 두줄 빼먹었더니, 위로 이동한 그 지점에서 아래로 내려와서, 아래로 안 움직이는것 처럼 보임
            nc = way[1]
            nr += dr[i]
            nc += dc[i]
            # 가독성 향상 방안
            # nr = way[0] + dr[i] < --- 이렇게 합칠 수도 있다.

            # 가독성 향상 방안
            # 밑에 두 if를 합칠 수 있다.
            if 0<=nr<N and 0<=nc<N: #and not visited~~~:
                if not visited[nr][nc] and maze[nr][nc] != '1':
                    visited[nr][nc] = True
                    stack.append([nr,nc])


    return 0



TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    # 내포 쓰지 말고, for문으로 돌리면서 시작지점의 index를 받자
    Sf = False

    maze = []
    for i in range(N):
        tem = list(input())
        if not Sf and '2' in tem:
            S = [i, tem.index('2')]
            Sf = True

        maze.append(tem)


    stack = []
    visited = [[False]*N for _ in range(N)]
    ans = delta(stack)
    print('#{0} {1}'.format(tc,ans))


# 앞으로 더 생각해볼 부분 -> 코드 가독성 높이기