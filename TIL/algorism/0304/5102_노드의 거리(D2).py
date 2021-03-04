# 5102번 노드의 거리 (D2)
"""
V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.
노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.
E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
두 노드 S와 G가 서로 연결되어 있지 않다면, 0을 출력한다.

"""
# 난관 1. 경로 딕셔너리 만들기
# 난관 2. 카운터 변수 +1 지점 결정 및 갱신 지점 결정
# 난관 3. BFS와 DFS의 구분을 잘 못해서 bfs 함수 자체에 대한 의심을 가졌음


import sys
sys.stdin = open('5102_input.txt','r')

# bfs를 만드는데 필요한 것. 비어있는 큐, 방문여부를 체크하는 변수
# 방문여부를 체크할 때, 변수가 아니라 행렬을 이용해서도 해보자.
def bfs(graph,start,goal):
    discovered = [start]
    counter = 0
    queue = [[start,counter]]
    while queue:
        # pop할때마다 counter 최신화 안해주면, counter는 고정이 된다
        [v,counter] = queue.pop(0)
        for w in graph[v]:

            if w == goal:
                return counter +1


            if w not in discovered:
                discovered.append(w)
                queue.append([w,counter+1])

    return 0

# 이런...방향성이 없다 == 양쪽으로 통행이 가능하다!
# 카운터랑 붙여라

TC = int(input())
for tc in range(1,TC+1):
    V,E = map(int,input().split())
    graph_dic={}

    for _ in range(E):
        node,way = map(int,input().split())
        graph_dic[node] = graph_dic.get(node,[]) + [way]
        graph_dic[way] = graph_dic.get(way,[]) + [node]

    S,G = map(int,input().split())


    # 제대로 넓이 우선 탐색이 되고 있었는데, 그래프 형태때문에 DFS로 되고 있다고 착각한것.
    print('#{0}'.format(tc),end=' ')
    print(bfs(graph_dic,S,G))
