# BFS 연습 2 --> 경로 출력

import sys
sys.stdin = open('DFS1_input.txt','r')


def BFS(i:int,lst:list):
    que =lst[i]
    result=[i]
    visited = [False] * (N+1)
    visited[i] = True
    while que:
        root = que.pop(0)
        if not visited[root]:
            que.extend(lst[root])
            result.append(root)
            visited[root] = True
    
    return list(map(str,result))



node_lst = list(map(int,input().split()))
N = max(node_lst)
first_lst = [[] for _ in range(N+1)] # 높은 노드 번호 부터 방문함
for idx in range(0,len(node_lst),2):
    first_lst[node_lst[idx]].append(node_lst[idx+1])
    first_lst[node_lst[idx+1]].append(node_lst[idx])

print('-'.join(BFS(1,first_lst)))