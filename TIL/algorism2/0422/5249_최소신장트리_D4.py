# 5249번 최소 신장 트리

# 그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때,
# 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.
# 0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때,
# 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.


# [입력]

# 첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.
# 다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다. 
# 1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000

# 이건 내가 직접 짜기에는 많은 시간이 걸릴듯...계속 연구하자
import sys
sys.stdin = open('5249_input.txt','r')

TC = int(input())

for tc in range(1,TC+1):
    V,E = map(int,input().split())
    node_lst = [[] for _ in range(V+1)]
    print(node_lst)
    for _ in range(E):
        n1,n2,w = (map(int,input().split()))
        node_lst[n1].append([n2,w])
        node_lst[n2].append([n1, w])
    print(node_lst)

    key = [ 0xffff for _ in range(V+1)] # 가중치 리스트
    pi = [0 for _ in range(V+1)] # 부모 노드 리스트
    U = set()
    result =[]
    pi[0] = 0
    key[0] =0
    print('pi_before',pi)
    print('key_before',key)

    for idx in range(V):
        mini = 100000
        for elem in node_lst[idx]:
            to, key_v = elem[0],elem[1] # idx번 노드 -> to 노드 간선 정보 , 가중치
            if not pi[to] and key_v <= mini:
                mini = key_v
                way = to
            # if way in U: continue # 이미 해당 노드가 포함되어있는지 아닌지 확인<-- 이게 문제인거 같은데
        pi[way] = True
        # 임시 최소값 등록
        key[way] = mini
        result.append(mini)
        for v,w in node_lst[way]:
            if not pi[v] and key[v] > w:
                key[v] = w
    print('U',U)
    print('pi_after',pi)
    print('key_after',key)
    print(sum(key))
    print(result)
    print('-'*50)