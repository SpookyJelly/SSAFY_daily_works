# 5251번 최소 이동거리

# A도시에는 E개의 일방통행 도로 구간이 있으며, 각 구간이 만나는 연결지점에는 0부터 N번까지의 번호가 붙어있다.
# 구간의 시작과 끝의 연결 지점 번호, 구간의 길이가 주어질 때,
# 0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리가 얼마인지 출력하는 프로그램을 만드시오.
# 모든 연결 지점을 거쳐가야 하는 것은 아니다.

# [입력]
# 첫 줄에 테스트 케이스의 개수 T가 주어지고,
# 테스트 케이스 별로 첫 줄에 마지막 연결지점 번호N과 도로의 개수 E가 주어진다.
# 다음 줄부터 E개의 줄에 걸쳐 구간 시작 s, 구간의 끝 지점 e, 구간 거리 w가 차례로 주어진다.
# ( 1<=T<=50, 1<=N, s, e<=1000, 1<=w<=10, 1<=E<=1000000 )

# 다이스트라로 풀면 된다
import sys
sys.stdin = open('5251_input.txt','r')

# def dijk(s):
#     D[s][0] = 0
#     D[s][1] = 0
#     curV = s
#
#     '''
#     U = [s]
#     for i in range(N):
#         v, dis = adj[curV][i]
#         D[w][0] = dis
#     '''
#     for k in range(N+1):
#         minV = 1000000
#         for i in range(N+1):
#             if i in U: continue
#             if D[i][0] < minV:
#                 curV = i
#                 minV = D[i][0]
#         U.append(curV)
#
#         for v, dis in adj[curV]:
#             if v in U: continue
#             if D[v][0] > D[curV][0] + dis:
#                 D[v][0] = D[curV][0] + dis
#                 D[v][1] = curV
#
#         print(D)

TC = int(input())

for tc in range(1,TC+1):
    N,E = map(int,input().split())
    node_lst = [[] for _ in range(N+1)]

    for _ in range(E):
        s,e,w = map(int,input().split())
        node_lst[s].append([e,w])
    # print(node_lst)
    MST = [False] * (N+1)
    key = [0xffff] * (N+1)

    key[0] = 0
    ans = []

    for _ in range(N+1):
        u,mini = 0,0xffff
        for idx in range(N+1):
            if not MST[idx] and key[idx] < mini:
                mini = key[idx]
                u = idx

        MST[u] = True
        ans.append(key[u])

        for v,w in node_lst[u]:
            # 방문하지 않았고, 거기의 key값이 크다
            # 프림이랑 다른 부분이 key[v] > key[u] + w 부분이다
            # key값의 변경이 앞선 노드의 가중치와 현재 노드의 가중치와의 합을 비교한 후 이루어진다.
            if not MST[v] and key[v] > key[u]+w:
                key[v] = key[u]+w
    # ans와 key의 차이가 도저히 이해가 안가는걸??
    # print('ans',ans)
    # 일단 여기서 key는 해당 노드에 도착하기 위한 최소 이동거리임
    # key[2] --> 2번 노드에 도착하기 위한 최소 이동거리
    # print('key',key)
    print('#{} {}'.format(tc,key[N]))