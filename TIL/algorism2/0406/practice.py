data = [[],[2,3],[4,0],[5,6],[7,0],[8,9],[10,11],
[12,0],[0,0],[0,0],[0,0],[0,0],[13,0],[0,0],[0,0]]


visited = [[False] for _ in range(len(data))]

def tra(root:list,i:int):
    if not visited[i]:
        print(i)
        visited[i] = True
    
    tra(data[root[0]],root[0])
    tra(data[root[1]],root[1])



def preorder(node):
    if node == 0:
        return
    print(node, end=' ')
    preorder(data[node][0])
    preorder(data[node][1])


print(preorder(1))