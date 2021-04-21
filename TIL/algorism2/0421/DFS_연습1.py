#모든 정점을 깊이 우선 탐색하여 깊이 우선 탐색 경로를 출력

import sys
sys.stdin = open('DFS1_input.txt','r')

def DFS1(i:int,lst:list):
    result = [i]
    stack = lst[i]
    visited = [False] * (N+1)
    visited[i] = True
    while stack:
        x = stack.pop()
        if not visited[x]:
            result.append(x)
            stack.extend(lst[x])
            visited[x] = True
    return list(map(str,result))
        



node_lst = list(map(int,input().split()))
N = max(node_lst)
first_lst = [[] for _ in range(N+1)] # 높은 노드 번호 부터 방문함
second_lst = []  # 높은 노드 번호부터 방문
for idx in range(0,len(node_lst),2):
    first_lst[node_lst[idx]].append(node_lst[idx+1])
    first_lst[node_lst[idx+1]].append(node_lst[idx])

for elem in first_lst:
    second_lst.append(elem[::-1])


print('-'.join(DFS1(1,first_lst)))
print('-'.join(DFS1(1,second_lst)))
