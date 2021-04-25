# 1251번 하나로

# - 환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(E * L2)만큼 지불
# 총 환경 부담금을 최소로 지불하며, N개의 모든 섬을 연결할 수 있는 교통 시스템을 설계하시오.
# 64비트 integer 및 double로 처리하지 않을 경우, overflow가 발생할 수 있습니다 (C/C++ 에서 64비트 integer는 long long 으로 선언).
# 위의 그림 2은 환경 부담금을 최소로 하며 모든 섬을 연결하고 있지만, 그림 3는 그렇지 않음을 알 수 있습니다.

# [입력]

# 가장 첫 줄은 전체 테스트 케이스의 수이다.
# 각 테스트 케이스의 첫 줄에는 섬의 개수 N이 주어지고 (1≤N≤1,000),
# 두 번째 줄에는 각 섬들의 정수인 X좌표, 세 번째 줄에는 각 섬들의 정수인 Y좌표가 주어진다 (0≤X≤1,000,000, 0≤Y≤1,000,000).
# 마지막으로, 해저터널 건설의 환경 부담 세율 실수 E가 주어진다 (0≤E≤1).
# 13초 정도 걸린다.

import sys
sys.stdin = open('1251_input.txt','r')
from time import time

st = time()

def prim(n):
    D[n] = 0
    # G[n][n] = 0 <-- 없어도 된다. 이미 밖에서 자기 자신에게 도달하는 거리는 0 인것으로 초기화 되어있다. ex) G[0][0] = G[1][1] = G[2][2] ... = 0

    U = []
    for _ in range(N):
        mini = float("inf")
        for idx in range(N):
            if  idx in U: continue
            if D[idx] < mini:
                mini = D[idx]
                key = idx
        U.append(key)

        for j in range(N):
            if j in U: continue
            # 이전에 풀었던 문제의 여파인가. 나도 모르게 조건을 G[key][j] + D[key] < D[j]으로 걸었다.
            # 이 문제에서 D[i]는 i번 섬에 부과되는 부담금이다. 그런데, 부과금이 부여되는 기준은 섬과 섬사이의 거리만으로 결정 되는것이고,
            # 이전 섬에 부여되었던 부과금은 하등 상관이 없기에  G[key][j]와 D[j] 만 비교하면 되는것이다
            if G[key][j] and G[key][j] < D[j]: #+ D[key] < D[j]:
                D[j] = G[key][j] #+ D[key]





TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())
    # 그래프 생성 / 2차원으로 만들기
    G = [[0] * N for _ in range(N)]
    # 큰 output에 대해서 자꾸 삑이 나길래 뭐지 싶었는데, D에 넣은 적당히 큰 값보다 더 쎈 친구들이 와버렸다
    # 그래서 python에서 선언할수 있는 양의 무한대를 적었다
    D = [float("inf")] * N
    for i in range(N):
        for j in range(N):
            G[i][j] = (X[i] - X[j])**2 + (Y[i] - Y[j])**2
            G[j][i] = G[i][j]

    prim(0)

    ans = 0
    for elem in D:
        ans += elem
    print('#{} {}'.format(tc, round(ans*E)))
    
end = time()
print(end-st)