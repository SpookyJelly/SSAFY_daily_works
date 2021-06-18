import sys
sys.stdin = open('11942_input.txt','r')
from heapq import heappush,heappop

def dik(start):
    heap = []

    heappush(heap,['a',distance['a'],])

    while heap:
        cur_Vertex,way = heappop(heap)

        for nex_Vertex,wei in graph[str(cur_Vertex)]:

            if distance[str(nex_Vertex)] < wei:
                continue

            new_way = wei + distance[str(cur_Vertex)]
            if new_way < distance[str(nex_Vertex)]:
                distance[str(nex_Vertex)] = new_way
                heappush(heap,[str(nex_Vertex),new_way])


TC = int(input())

for tc in range(TC):
    N, M = map(int,input().split())
    graph = {}
    inf = 0xfffffff
    distance = {}

    for i in range(97,97+N):
        distance[chr(i)] = inf
        graph[chr(i)] = []

    for _ in range(M):
        start,goal,weight = input().split()
        graph[start] = graph.get(start,[]) + [(goal,int(weight))]

    distance['a'] = 0
    dik('a')
    
    print('#{0}'.format(tc+1), end=" ")
    for value in distance.values():
        print(value , end=" ")
    print()