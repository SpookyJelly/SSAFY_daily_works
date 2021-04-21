#2814번 최장경로

# N개의 정점과 M개의 간선으로 구성된 가중치가 없는 무방향 그래프에서의 최장 경로의 길이를 계산하자.
# 정점의 번호는 1번부터 N번까지 순서대로 부여되어 있다.
# 경로에는 같은 정점의 번호가 2번 이상 등장할 수 없으며, 경로 상의 인접한 점들 사이에는 반드시 두 정점을 연결하는 간선이 존재해야 한다.
# 경로의 길이는 경로 상에 등장하는 정점의 개수를 나타낸다.


# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 두 개의 자연수 N M(1 ≤ N ≤ 10, 0 ≤ M ≤ 20)이 주어진다.
# 두 번째 줄부터 M개의 줄에 걸쳐서 그래프의 간선 정보를 나타내는 두 정수 x y(1 ≤ x, y ≤ N)이 주어진다.
# x와 y는 서로 다른 정수이며, 두 정점 사이에 여러 간선이 존재할 수 있다.

import sys
sys.stdin = open('2814_input.txt','r')


def DFS(cur:int, count:int)->int:
    global result

    if result < count:
        result = count
    # 최장 경로를 추출하는거니까, 한번의 시도에 각각 자식 노드를 한가지만 방문해야한다.
    # 원래는 스택을 이용해서 구현했는데, 실수로 스택 초기값으로 N번째 연결되어있는 자식 노드를 다 때려박아서 실패했다
    for inner in node_lst[cur]:
        if not visited[inner]:
            visited[inner] = True
            DFS(inner, count+1)
            visited[inner] = False



TC = int(input())

for tc in range(1,TC+1):
    N,M = map(int,input().split())
    node_lst = [[] for _ in range(N+1)]
    result = 0
    for _ in range(M):
        parent, child = map(int,input().split())
        node_lst[parent].append(child)
        node_lst[child].append(parent)

    visited = [False] * (N + 1)

    for idx in range(1,len(node_lst)):
        visited[idx] = True
        DFS(idx,1)
        visited[idx] = False
    print('#{0} {1}'.format(tc, result))
        
