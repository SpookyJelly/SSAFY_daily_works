#4615번 재미있는 오셀로.
"""
규칙 생략

"""

import sys
sys.stdin = open("4615_input.txt","r")

# 같은 돌의 색깔 나올때까지 8방향 살핌 -> 같은 색상 나오면, 그 사이에 있는 돌들 모두 자신의 색깔로 바꾼다
# 돌의 row,col, color를 받아준다.
def finding(R,C,color):
    # 델타-> 북 북동 동 동남 남 남서 서 북서
    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]


    for d in range(8):
        nx = R
        ny = C
        # while문 진입전, 한번 델타 무브를 해준다.
        # -> while문에서 arr[nx][ny]== color 일때까지 반복할 꺼라.
        # nx = R / ny = C 이면 while문을 돌지 않기 때문이다.
        nx += dr[d]
        ny += dc[d]
        
        cnt = 0
        # while문의 목적은, 자기자신과 다르고, 0이 아닌 요소를 count 하기 위해서 설계.
        # arr[nx][ny]= 0 or 자신의 color 이면 while 멈춤 --> while문 내부는 arr[nx][ny] == 다른 color 일때만 적용됨 
        while 0<=nx<N and 0<=ny<N and arr[nx][ny] != color and arr[nx][ny] != 0:
            # 해당 조건을 만족하는 arr[nx][ny]가 나올때마다 cnt += 1
            cnt += 1
            nx += dr[d]
            ny += dc[d]

        # 위의 while문이 종료되었을때, 그 위치의 값이 color와 동일하다면 if문 수행
        # 만약 arr[nx][ny] == 0 or 다른 color이면, 오셀로 규칙을 만족하지 않는 경우이므로,
        # 색을 바꾸지 않고 다른 방향을 탐색한다.
        # **여기도 범위 체크해야한다.** while문을 마친 친구는 1) arr[nx][ny] == 0 or 다른 color 이거나, 2)nx, ny가 범위 밖인 친구들이다.
        # 1)을 거르기 위해서 arr[nx][ny] == color를 설정하고, 2)를 거르기 위해서는 nx / ny 범위 조건을 넣어줬다.
        if 0<=nx<N and 0<=ny<N and arr[nx][ny] == color: 
            R1 = R
            C1 = C

            # cnt 만큼 바꿔주자.
            # dr[d] / dc[d] 방향으로 cnt 번 움직이면서 값을 color로 바꿔줌
            for _ in range(cnt):
                R1 += dr[d]
                C1 += dc[d]
                arr[R1][C1] = color
    # 원본 arr을 바꿔줘서 이후 입력에도 활용한다.
    return arr

"""

Q1.

1 0 1 0      1 1 1 2         2 2 2 2             1 1 1 2
0 0 0 1 에서 0 0 0 1 가 되면? 0 0 0 2 인가? 아니면  0 0 0 2 인가?
0 0 0 2      0 0 0 2         0 0 0 2             0 0 0 2
                                                #이거다.

"""



TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    arr = [[0 for _ in range(N)] for __ in range(N)]
    
    # 최초 4개 배치
    arr[N//2][N//2] = 2
    arr[N//2-1][N//2-1] = 2
    arr[N//2][N//2-1] = 1
    arr[N//2-1][N//2] = 1

    for i in range(M):
        # 돌 놓는 방법
        row,col,color = list(map(int,input().split()))
        # 문제에서 제시한 착점 방법과 행렬 내의 착점을 일치 시켜준다.
        n_r,n_c = col-1, row-1
        arr[n_r][n_c] = color
        #finding 함수를 이용해, 착수 할때마다 배열을 바꿔준다.        
        finding(n_r,n_c,color)
        
    # 굳이 finding 함수로 거쳐 나온 애를 어디 할당할 필요가 없다.
    # finding 함수가 원본 arr를 변형시키기 때문
    black = 0
    white = 0
    for R in range(len(arr)):
        for C in range(len(arr)):
            if arr[R][C] == 1:
                black += 1
            elif arr[R][C] == 2:
                white += 1

    print('#{0} {1} {2}'.format(tc, black,white))
    # 종료조건은 어떻게 설정하지???? --> 문제가 알아서 종료하기 때문에 따로 생각할 필요가 없다