# 4875번 미로 (D2)

# 기본 아이디어.
# 스택의 마지막 값 뽑기 -> 정답인지 체크하기 ->
# 뽑은 위치 방문표시하기 -> 현재위치에 대해 4방향 탐색 -> 갈 수 있으면 그 위치 스택에 넣기

import sys

sys.stdin = open('4875_input.txt', 'r')


def delta(stack):
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 스택에 초기값 셋팅해준다.
    stack.append(S)
    visited[S[0]][S[1]] = True
    while stack:
        # 가독성 향상 방안
        (r, c) = stack.pop()
        # 뽑은 값 체크
        if maze[r][c] == '3':
            return 1

        for i in range(4):
            # 여기 방향 바뀔때마다 다시 원래 값으로 돌아온 후, 방향 더하기
            nr = r + dr[i]
            nc = c + dc[i]

            # 움직인 곳이, 행렬 내부에 있고, 방문하지 않았으며, 데이터 값이 1이 아닐때만, 스택에 append
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and maze[nr][nc] != '1':
                visited[nr][nc] = True
                stack.append((nr, nc))

    return 0


TC = int(input())

for tc in range(1, TC + 1):
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
    visited = [[False] * N for _ in range(N)]
    ans = delta(stack)
    print('#{0} {1}'.format(tc, ans))

