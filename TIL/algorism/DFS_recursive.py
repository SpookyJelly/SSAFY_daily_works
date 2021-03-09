def recursive_DFS(v, discoverd=[]):
    discoverd.append(v)
    for w in graph[v]:
        if not w in discoverd:
            discoverd = recursive_DFS(w, discoverd)

    return discoverd


graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [5],
    5: [6, 7],
    6: [],
    7: [3]
}

print(recursive_DFS(1))