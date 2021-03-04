def BFS_class(graph, v):  # graph : 노드들 간 연결 되어 있는 데이터, v: 시작 지점
    queue = []
    queue.append(v)
    visited = [False] * (len(graph)+1)
    result =[]

    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            result.append(t)
        for i in graph[t]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                result.append(i)

    return result



def iterative_BFS(graph,start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered


# graph : 노드들 간 연결되어있는 상태 <-- 딕셔너리로 구현해보자
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1,7],
    4: [2,6],
    5: [2,6],
    6: [4,5,7],
    7: [3, 6]

}


print(BFS_class(graph,2))
print(iterative_BFS(graph,2))
