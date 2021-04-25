def find_set(x,p):
    while p[x] != x:
        x = p[x]
    return x

def Kruskal(N,edge):
    p =[i for i in range(N)] # 대표원소 초기화
    #N-1개의 대표원소 선택될때까지 반복
    L2 = 0
    cnt = 0
    for w,u,v in edge:
        if find_set(u,edge) != find_set(v,edge):
            # weight의 합을 구하는 것이다.
            p[find_set(v,edge)] = find_set(u,edge)
            cnt += 1
            L2 += w
            if cnt == N-1: # N-1개의 간선선택 완료
                return L2
import sys
sys.stdin = open('1251_input.txt','r')


T = int(input())
T = 1
for tc in range(1,T+1):
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())

    # 완전 그래프 정리
    adj = [[0]*N for _ in range(N)] # 인접행렬
    for i in range(N):
        for j in range(N):
            adj[i][j] = (X[i]- X[j]) **2 + (Y[i]-Y[j])**2
            adj[j][i] = adj[i][j] # 무향 그래프 이므로, 두 정점간의 간선 크기는 같다

    edge = [] # 간선 정보 기준 저장
    for i in range(N):
        for j in range(i+1,N):# 무향 그래프니까 굳이 i~j까지 추가할 필요없이 반만 추가해줘도 된다
            # 이게 왜 반이 되는지는 생각해보자
            edge.append([((X[i]- X[j]) **2 + (Y[i]-Y[j])**2),i,j])
    edge.sort()
    print(Kruskal(N,edge))

