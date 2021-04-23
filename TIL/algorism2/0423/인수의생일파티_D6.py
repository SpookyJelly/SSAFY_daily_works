# 인수의 생일파티

# 인수가 사는 마을에는 N개의 집이 있고, 각 집에는 한 명의 사람이 살고 있다.
# N개의 집을 정점으로 볼 때, 도로는 어떤 집에서 다른 어떤 집으로 이동이 가능한 단방향 간선으로 볼 수 있으며,
# 각각에 대해서 이동하는데 시간이 정해져 있다.
# 도로는 모든 집들 간에 이동이 가능하도록 구성되어 있다.
# 집에 1번에서 N번까지의 번호를 붙일 때, 인수의 집은 X번 집이다
# 오늘은 인수의 생일이기 때문에 모든 마을 사람들이 인수의 생일을 축하해주기 위해 X번 집으로 모인다.
# 각 사람들은 자신의 집에서 X번 집으로 오고 가기 위해 최단 시간으로 이동한다.
# 도로가 단 방향이기 때문에 이용하는 도로는 오고 갈 때 다를 것이다.


# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 세 정수 N,M,X(1 ≤ X ≤ N ≤ 1,000, 1 ≤ M ≤ 10,000)가 공백으로 구분되어 주어진다.
# 다음 M개의 각 줄에는 세 정수 x, y, c (1 ≤ x, y ＜ N, 1 ≤ c ≤ 100)가 공백으로 구분되어 주어진다.
# 이는 x번 집에서 y번 집으로 가는 데 시간이 c가 걸리는 단 방향 도로가 존재한다는 뜻이다.

import sys
sys.stdin = open("1795_input.txt","r")

# X = > i
def dik(s,D):# 다이스트라 적용
    D[s] = 0 # 초기값 설정. 시작 지점의 D 값은 비운다
    que = [s]
    U = []
    while que:
        v = que.pop(0)
        for i in range(len(G[v])):
            # 방문한적 없고, 연결되어있다면 이하를 확인한다
            if i not in U and G[v][i]:
                # D[v] == v번 노드까지 가는데 걸리는 거리
                # D[i] == 원래 i번 노드까지 가는데 걸리는 최소 거리 (라고 생각되었던것)
                # G[v][i] + D[v] --> v번 노드까지 이동한 다음, i 번 노드로 이동하는 경우, 그 때의 거리
                # 근데 만약에 v번 노드에서 i번 노드로 가는게, 여태까지 알고 있던 i번 노드로 가는 최소 거리 보다 짧다면 교체
                if G[v][i] + D[v] < D[i]:
                    D[i] = G[v][i] + D[v]
                    que.append(i)
        U.append(v)
    return D

# 그러면 i => X 으로 나가는 다이스트라
# dik1과의 차이는 나와 인접해있는 노드라고 간주할 적에, 내가 진출하는 노드인가? (가는 화살표) 내가 진출 받는?? 노드인가(오는 화살표)인가를 구분
# G가 비대칭이기에 가능하다.
def dik2(s,D):
    D[s] = 0 
    que = [s]
    U = []
    while que:
        v = que.pop(0) # 1회차 : v = 2
        for i in range(len(G[v])): 
            # G[v]의 길이만큼 i가 변하면서 살핀다. i = 0 ~5
            # 만약에 i가 이미 패밀리가 아니고, G[i][v] 가 0이 아니라면 --> G[1][2] --> 1번 노드에서 2번 노드로 향하는 간선 == 2번이 화살표를 맞는 입장
            if i not in U and G[i][v]:
                if G[i][v] + D[v] < D[i]:
                    D[i] = G[i][v] + D[v]
                    que.append(i)
        # 검사가 다 끝나면, 노드 v에 대한 검사는 모두 끝났다는 의미로 U에 추가한다.
        U.append(v)  
    return D

def dik3(s,D,is_R):
    D[s] = 0 
    que = [s]
    while que:
        v = que.pop(0) # 1회차 : v = 2
        for i in range(len(G[v])):
            if is_R:
                if i not in U and G[i][v]:
                    if G[i][v] + D[v] < D[i]:
                        D[i] = G[i][v] + D[v]
                        que.append(i)
                    # U.append(i)
            else:
                if i not in U and G[v][i]:
                    if G[v][i] + D[v] < D[i]:
                        D[i] = G[v][i] + D[v]
                        que.append(i)
        U.append(v)
    return D  

TC = int(input())
for tc in range(1,TC+1):
    N,M,X = map(int,input().split()) # N 개의 집 / M 간선의 수 / X : 목적지
    G = [[0] * (N+1) for _ in range(N+1)] # 그래프가 될 행렬
    for _ in range(M):
        x,y,c = map(int,input().split()) # x에서 y로 가는데 c라는 시간이 걸린다
        G[x][y] = c
    D1 = [1e10] * (N+1) # 짱짱큰 초기값
    D2 = [1e10] * (N+1)

    # A = dik3(X,D1,True)
    # B = dik3(X,D2,False)
    A = dik(X,D1)
    B = dik(X,D2)
    for idx in range(1,len(A)):
        A[idx] += B[idx]

    print('#{} {}'.format(tc,max(A[1:])))
