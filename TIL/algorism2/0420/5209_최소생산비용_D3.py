# 5209 최소 생산비용 D3
# A사는 여러 곳에 공장을 갖고 있다. 봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.
# 각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.
# 이때 1-C, 2-A, 3-B로 제품별 생산 공장을 정하면 생산 비용이 21+11+31=63으로 최소가 된다.

# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 제품 수 N이 주어지고, 이후 제품당 한 줄 씩 N개의 줄에 걸쳐 공장별 생산비용 Vij가 주어진다. 3<=N<=15,   1<=Vij<=99

import sys
sys.stdin = open('5209_input.txt','r')

def perm(l,k,mini): # l: 리스트의 길이, k : 선택한 원소의 갯수
    global minimi

    if mini > minimi:
        return
    if k==N:
        result.append(selector[:])
        minimi = mini

    else:
        for i in range(k,l):
            selector[i],selector[k] = selector[k],selector[i]
            # 재귀의 특징인 세이브포인트 역할을 살려서 해결.
            # parameter로 현재까지의 최소값을 넘겨줘야하는 것은 짐작했는데, 어떤 값을 넘겨줘야할지가 어려웠다.
            # swap 순열은 k~l 범위의 값이 교환되면서 생성되는데, 루프마다 k의 값이 커지면서 교환범위를 점점 줄여나간다.
            # 결국 k번째 자리에 k 이후의 값들을 쭉쭉 넣으면서 생성하는 것이다.
            # 앞서 말했듯, 재귀는 세이브 포인트 역할을 한다고 했다. 이번에는 k 번째 위치부터 바꿔볼꺼니까, k 값을 저장해야하는 것이다.
            # 실제로, 재귀가 끝나고 나오는 32번째 라인에서도 i번째 위치와 k번째 위치를 교환하면서 원상복구를 하는데, 이는 곧 k번째 위치에 변동사항이 있었다는 것이다.
            perm(l,k+1,mini + line[selector[k]][k])
            selector[i], selector[k] = selector[k], selector[i]




TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    selector = [i for i in range(N)]
    result=[]
    line = [list(map(int,input().split())) for _ in range(N)]
    minimi = 0xfffff
    perm(N,0,0)
    print('#{0} {1}'.format(tc, minimi))

    # 제한 시간 초과... 가지치기를 어떻게 할까요? --> 부분집합 만들때 잘라버리자자