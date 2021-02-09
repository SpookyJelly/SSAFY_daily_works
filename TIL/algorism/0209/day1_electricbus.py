"""
#4831번 전기버스

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )


각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )

3 # 노선 갯수
3 10 5 # K = 전기차 이동반경 / N = 목적지 / M =충전기 설치 된 정류장의 갯수
1 3 5 7 9 # 충전기 설치되어있는 스테이션
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17
"""
# 접근 방법
# 1. 버스가 실제로 움직인다고 가정한다. 버스는 기본적으로 풀파워(K)로 이동한다.
# 2. 만약에 풀파워로 이동하는 도착지에 충전기가 있다면, 버스는 그 곳으로 이동하고 파워를 다시 풀로 채운다. 충전횟수를 1 올린다.
# 3. 없다면, 풀파워에서 -1 하여 살핀다. 있다면 그곳으로 이동한다. 이동 후 다시 파워를 풀로 채운다. 충전횟수를 1 올린다.
# 4. 2~3의 과정을 반복한다. bus의 위치가 N이랑 같다면, 루프를 종료하고 충전 횟수를 반환한다.
# 4.1 3의 과정을 풀파워가 0이 되었는데도 이동이 불가하다면, 설계가 잘못된 것이다. 실패를 반환한다.

import sys
sys.stdin = open("sample_input (2).txt", "r")


for tc in range(1, int(input())+1):
    K, N, M = list(map(int, input().split()))
    # 구현할 알고리즘 상, 도착위치에 충전기가 없으면, 이동하지를 못한다. 그래서 몰래 마지막 위치에 N을 충전기로 지정한다.
    # 만약에 이미 들어온 값이 마지막에 충전기가 있어도 상관 없다. 어짜피 종료 조건이 "bus가 N과 같은가?" 이니까, N 하나 더 추가 되는거야 상관 없음
    charge = list(map(int, input().split()))+[N]
    # 버스의 위치를 표시하고, 충전횟수 표시할 변수 / bus , cnt
    bus, cnt = [0, 0]
    # range(N+1)이 전체 뻐스 노선도임. 근데 보니까 전체 뻐스 노선도 필요없다.
    # for i in range(N+1):
    #     # K 대신에 쓸 다른 임시변수 사용 (why? K는 계속 값 바꾸면서 재사용할꺼니까, 이미테이션이 필요)
    power = K
    while power > 0:
        if bus+power in charge:
            bus = bus+power
            cnt += 1
            # 성공적으로 이동하면 풀파워 충전
            power = K
        else:
            power -= 1
    if bus == N:
        print('#{0} {1}'.format(tc, cnt-1))
        # print(bus, cnt-1)
    else:
        print('#{0} {1}'.format(tc, 0))
        # print('실패')

"""이하는 구현하다가 놓은 코드인데, 충전소를 기준으로 설치하려고 했다.
# 셀프 과제) 버스의 움직임을 배제하고, 충전소 위치로만 문제를 한번 풀어보자."""
# def blueprint(K,charge):
#     maxi = 0
#     for i in range(len(charge)-1):
#         distance=charge[i+1]-charge[i]
#         if distance>maxi:
#             maxi=distance
#     if maxi>int(K):
#         return False
#     return True
#
#
# T = int(input())
#
# for tc in range(1,T+1):
#     K,N,M = list(map(int,input().split()))
#     charge = list(map(int,input().split()))
#     bus,cnt,smt=[0,0,0]
#     if blueprint(K,charge):
#         while(bus<N):
#             for i in range(len(charge)-1):
#                 smt += charge[i+1]-charge[i]
#                 if K <= smt: # 출발 직전
#                     bus=charge[i]
#                     smt=0
#                     cnt+=1
#                 if bus+K==N:
#                     bus=N
#                     cnt+=1
#                     break
#     print('#{0} {1}'.format(tc, cnt))

'''
    if blueprint(K,charge):
        while(bus<N):
            for idx in range(K,0,-1):
                if bus+idx in charge:
                    bus= bus+idx
                    cnt +=1
                    continue
                elif bus+idx == N:
                    bus=N
                    break # 이 라인은 없어도 됨
'''