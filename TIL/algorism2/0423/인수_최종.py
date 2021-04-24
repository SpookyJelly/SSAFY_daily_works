import sys
sys.stdin = open('1795_input2.txt','r')

def dik3(s,D,is_R,G):
    D[s] = 0
    que = [s]
    U = []
    while que:
        v = que.pop(0) # 1회차 : v = 2
        # 수정 1. D[i] 갱신을 max 함수를 사용해서, if문으로 쓸데없이 길었던 부분을 쳐냄,
        # 수정 2. i in U 인 경우만 체크하기로 한것을 제거해서 G[v] 전체를 조사하도록 함
        # 수정 2.5 그러면, 전부 다 체크하는 것은 시간 낭비이니, 최소값을 먼저 집어넣어야하겠다 <-- 최소값 찾기를 어떻게 할까? 다른 사람들은 heap을 쓰던데, 나는 그러고 싶지는 않은데...
        # 그냥 min 쓰면 0이 들어가니까...
        mini = 0xffff
        for i in range(len(G[v])):
            if is_R:
                if G[i][v] !=0 and G[i][v] < mini:
                    mini1 = G[i][v]
                    mini_way1 = i
            else:
                if G[v][i] !=0 and G[v][i] < mini:
                    mini2 = G[v][i]
                    mini_way2 = i


        for i in range(len(G[v])):
            if is_R:
                # if i in U : continue
                if G[i][mini_way1] and D[i] > D[v] +mini1:
                    D[i] = D[v] +mini1
                    que.append(mini_way1)
                    U.append(v)
            else:
                # if i in U: continue
                if G[mini_way2][i] and D[i] > D[v] +mini2:
                    D[i] = D[v] +mini2
                    que.append(mini_way2)
                    U.append(v)
    return D

# def dik3(s,D,is_R,G):
#     D[s] = 0
#     que = [s]
#     U = []
#     while que:
#         v = que.pop(0) # 1회차 : v = 2
#         # 수정 1. D[i] 갱신을 max 함수를 사용해서, if문으로 쓸데없이 길었던 부분을 쳐냄,
#         # 수정 2. i in U 인 경우만 체크하기로 한것을 제거해서 G[v] 전체를 조사하도록 함
#         # 수정 2.5 그러면, 전부 다 체크하는 것은 시간 낭비이니, 최소값을 먼저 집어넣어야하겠다
#         for i in range(len(G[v])):
#             mini = 0xffff
#             if is_R:
#                 mini = min(mini,G[i][v])
#                 if G[i][v]:
#                     D[i] = max(G[i][v] + D[v] , D[i])
#                     que.append(i)
#                         # U.append(v)
#             else:
#                 if G[v][i]:
#                     D[i] = max(G[v][i] + D[v], D[i])
#                     que.append(i)
#                         # U.append(v)
#     return D

TC = int(input())
for tc in range(1,TC+1):
    N,M,X = map(int,input().split()) # N 개의 집 / M 간선의 수 / X : 목적지
    G = [[0] * (N+1) for _ in range(N+1)] # 그래프가 될 행렬

    for _ in range(M):
        x,y,c = map(int,input().split()) # x에서 y로 가는데 c라는 시간이 걸린다
        G[x][y] = c

    D1 = [1e10] * (N+1) # 짱짱큰 초기값
    D2 = [1e10] * (N+1)

    A = dik3(X,D1,True,G)
    B = dik3(X,D2,False,G)

    for idx in range(1,len(A)):
        A[idx] += B[idx]

    print('#{} {}'.format(tc,max(A[1:])))