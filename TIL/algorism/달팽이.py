# 달팽이 만들어보기

def snail(arr):
    # 우 하 좌 상 델타무브
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    N = len(arr)
    #
    cnt = 1
    # 그렇기 때문에, 최초 값은 dr/dc가 더해졌을때, nx = 0 , ny =0으로 시작할 수 있게 셋팅 필요
    nx = 0
    ny = -1
    while cnt <= (N*N):
        for i in range(4):
            # 방향 전환전에 dr/dc 만큼 더해준다.
            nx += dr[i]
            ny += dc[i]
            # nx, ny 범위가 N을 벗어나지 않게 함과 동시에, 내가 숫자를 찍을 부분이 0이여야함
            while 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0:
                arr[nx][ny] = cnt
                cnt+=1
                nx += dr[i]
                ny += dc[i]
            # 마지막 while문 돌고 나온것이 nx += dr[i] ny+=dc[i]가 먹혀 있으므로, index 에러가 난다.
            # 다음 방향 먹여주기 전에 한번 빼주자.
            nx -= dr[i]
            ny -= dc[i]
    return arr






N = 5
arr = [[0 for _ in range(5)] for __ in range(5)]

print(snail(arr))

