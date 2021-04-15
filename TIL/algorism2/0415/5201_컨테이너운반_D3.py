# 5201 컨테이너 운반

# 화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.
# 트럭당 한 개의 컨테이너를 운반 할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.
# 컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고, A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다고 한다.
# 이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램을 만드시오.
# 화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다. 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 컨테이너 수 N과 트럭 수 M이 주어지고,
# 다음 줄에 N개의 화물이 무게wi, 그 다음 줄에 M개 트럭의 적재용량 ti가 주어진다.
# 1<=N, M<=100, 1<=wi, ti<=50

import sys
sys.stdin = open('5201_input.txt','r')

def two_pointer(cargo_lst,truck_capacity):
    cargo_pointer = 0
    truck_pointer = 0
    total_weight = 0
    while cargo_pointer< len(cargo_lst) and truck_pointer < len(truck_capacity):
        # 화물 무게가 트럭 적재 용량보다 작거나 같을 경우 ( 실을 수 있는 경우)
        if cargo_lst[cargo_pointer] <= truck_capacity[truck_pointer]:
            total_weight += cargo_lst[cargo_pointer]
            truck_pointer += 1
        
        # else: 화물무게가 트럭 적재 용량보다 큰 경우 ( 실을 수 없는 경우)
        cargo_pointer += 1
    return total_weight

TC = int(input())

for tc in range(1,TC+1):
    N,M = map(int,input().split()) # N = 컨테이너 수 // M = 트럭 수
    cargo_lst = list(map(int,input().split()))
    truck_capacity = list(map(int,input().split()))
    cargo_lst.sort(reverse=True)
    truck_capacity.sort(reverse=True)

    ans = two_pointer(cargo_lst,truck_capacity)
    print('#{0} {1}'.format(tc,ans))