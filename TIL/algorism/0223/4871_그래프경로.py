# 4871번 그래프 경로(D2)

"""
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때,
특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.

예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

"""
# DFS 기법을 이용해 분석

import sys
sys.stdin = open("4871_input.txt",'r')

TC = int(input())

for tc in range(1,TC+1):
     V,E = map(int,input().split())
     arr = [[0 for x in range(V)] for y in range(V)]
     for _ in range(E): # 일단 여기서 행렬 꼴로 경로를 표시하자.
         row , col = map(int,input().split())
         arr[row-1][col-1] = 1
     S,G = map(int,input().split()) # 시작점과 끝점을 입력 받는다.

     stack = list()  # 지나온 경로 저장 지나왔던 pass를 통과하지 않도록, 뭔가 조치가 필요할 거 같은데
     # 교수님 코드의 visited의 의미???
     # visited는 이 노드를 방문했는가?를 체크해서 ***스택에 노드가 중복해서 쌓이지 않도록 하는 것***.
     # 이걸 체크 안하면, 만약 노드가 순환하는 경우, 무한 루프가 생길 수도 있다.
     visited = [False] * V # 노드 수만큼의 false가 존재하므로 다음과 같이 만들어준다.
     # 이렇게 하면 [False, False, False, False, False, False] 가 된다.
     # 나는 [[False],[False],[False],[False],[False],[False]] 인줄 알았는데, 이런 꼴은 아래와 같이 해서 만든다.
     # [[False]]* V <-- 근데 가급적이면 이런거 하지마라.. shallow copy가 되어버리니까
     # 문법 실수할 수도 있지.ㅎㅎ
     stack.append(S-1)
     result = 0
     while stack:
        way = stack.pop(-1)
        for j in range(V):
            # 여기 스위트에서 visited 체크
            if not visited[j]:
                if arr[way][j] == 1 and j == G-1:
                    result = 1
                    break
                elif arr[way][j] == 1:
                    stack.append(j)
                    visited[j] = True

     print(f'#{tc} {result}')

    #arr =[[0, 0, 1, 1, 0, 0], [0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0],
     #[0, 0, 0, 0, 0, 0]]
