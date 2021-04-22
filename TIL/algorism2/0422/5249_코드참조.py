import sys
sys.stdin = open('5249_input.txt','r')

TC = int(input())

for tc in range(1,TC+1):
    V,E = map(int,input().split())
    node_lst = [[] for _ in range(V+1)]
    print(node_lst)
    for _ in range(E):
        n1,n2,w = (map(int,input().split()))
        node_lst[n1].append([n2,w])
        # 쌍방향 리스트로 만들어준다.
        node_lst[n2].append([n1,w])
    print(node_lst)
    # 패밀리에 join 되었는지 확인하는 것. 인덱스 번호 == 노드 번호, 요소들 == 방문여부
    MST = [False] * (V+1)
    # 여기 key의 요소들이 최소 가중치가 된다
    key = [0xffffff] *(V+1)
    # 최소 셋팅
    key[0] = 0
    ans = []

    for _ in range(V+1):
        # key 값이 최소인 정점 찾기
        u, min_key = 0,0xffffffff
        # 패밀리에 조인되지 않고, min_key 값보다 key[i] (i번째 노드에 닿은 간선 (최소 가중치)) 값이 작으면 바꿔준다.
        for i in range(V+1):
            if not MST[i] and min_key > key[i]:
                # 현재 노드에서 뻗어있는 간선들 중에서 가장 숫자가 작은 놈을 u,min_key로 삼는다
                # min_key는 이 조건문에서 최소 값을 거르는데 쓰는 filter로 쓰고, u는 현재 i번째 노드에서 가장 간선 가중치가 낮은 노드의 번호이다.
                u, min_key = i, key[i]
        # 방문처리 처음에는 0번 위치 빼고 전부 이상한 값이 들어가있으니, 당연히 초회차에는 MST[0] = True가 된다.
        MST[u] = True
        # 처음에는 key들이 다 0xffff이니까 필연적으로 0이 먼저 들어간다
        ans.append(key[u])

        # nodle_lst[u]에 있는 모든 v,w (목적지 / 가중치) 를 대상으로 조사
        for v,w in node_lst[u]:
            # 만약에 목적지 v가 패밀리에 들어와있지도 않고, 이미 key[v]에 들어와있는 녀석이 w 보다 크다면 --> 더 작은 가중치를 찾은것
            if not MST[v] and key[v] > w:
                # 바꿔준다.
                key[v] = w

        print('tc',tc,ans)
    print(key)
    print('='*50)

# 대충 사이클은 알겠는데, 실제로 짜라고 하면.... 어려울거 같다.