import sys
sys.stdin = open('1795_input2.txt','r')

# 최소값만 먼저 끄집어서 넣을 수는 없을까? 힙 사용하는거 말고??
# 더 강해져서 돌아오겠다.
def dik3(s,D,is_R,G):
    D[s] = 0 
    que = [s]
    U = []
    while que:
        v = que.pop(0) # 1회차 : v = 2
        for i in range(len(G[v])):
            if is_R:
                if i not in U and G[i][v]:
                    if G[i][v] + D[v] < D[i]:
                        D[i] = G[i][v] + D[v]
                        que.append(i)
                        # U.append(v)
            else:
                if i not in U and G[v][i]:
                    if G[v][i] + D[v] < D[i]:
                        D[i] = G[v][i] + D[v]
                        que.append(i)
                        # U.append(v)
    return D  

TC = int(input())
for tc in range(1,TC+1):
    N,M,X = map(int,input().split()) # N 개의 집 / M 간선의 수 / X : 목적지
    G = [[0] * (N+1) for _ in range(N+1)] # 그래프가 될 행렬
    G1 = [[0] * (N+1) for _ in range(N+1)] # 그래프가 될 행렬
    for _ in range(M):
        x,y,c = map(int,input().split()) # x에서 y로 가는데 c라는 시간이 걸린다
        G[x][y] = c
        G1[y][x] = c
    D1 = [1e10] * (N+1) # 짱짱큰 초기값
    D2 = [1e10] * (N+1)

    A = dik3(X,D1,True,G)
    # B = dik3(X,D2,True,G1)
    B = dik3(X,D2,False,G)
    for idx in range(1,len(A)):
        A[idx] += B[idx]

    print('#{} {}'.format(tc,max(A[1:])))