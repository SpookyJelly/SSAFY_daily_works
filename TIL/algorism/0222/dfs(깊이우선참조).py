G = [[],[2,3],[1,4,5],[1,7],[2,6],[2,6],[4,5,7],[3,6]]
#
# def push(item):
#     s.append(item)
# def pop():
#     if len(s) != 0:
#         return s.pop(-1)


def dfs(v):
    visited = [False] * 10 # 데이터 갯수만큼 만들어줘라
    s =[] # 스택 한번 선언
    s.extend(G[v])
    #visited[v] = True
    # Goal = 3
    N = len(G)
    #print(s)
    while s : # 스택에 뭔가 넣었다 뺐다하면서 작업을 할 것이다.
        # 그래서 얘는 스택에 뭔가 차 있을 동안만 반복
        # pop 하면서 데이터 처리
        v = s.pop(-1) # v = 현재 위치의 버택스 (현재의 위치) / w = 인접한 버택스
        #print(v) # 실제로 팝한 데이터가 나한테 필요한거임
        if v == Goal:
            return 1
        ###???### 풀로 도는게 아니라 어느 지점에서 멈추고 싶다면 이 지점
        for w in range(len(G[v])): # G를 보면 나하고 인접한 친구들로 구성되어있는 리스트다.
            if not visited[v]:
                s.append(G[v][w])
        visited[v] = True
    return 0



def dfsr(v): # v를 기준으로 인접한 지점을 다 쫓아간다는 말
    visited[v] = True
    print(v)
    ########목표지점 넣고 싶을때는 이 라인에############
    #if v == 목표:
        #pass
    for w in G[v]:
        if not visited[w]:
            dfsr(w)
Goal = 3
print(dfs(2))