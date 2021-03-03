# 다리를 지난 트럭 (D2)

"""
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 구하자

트럭은 1초에 1만큼 움직인다.

제한 조건
bridge_length는 1 이상 10,000 이하입니다.
weight는 1 이상 10,000 이하입니다.
truck_weights의 길이는 1 이상 10,000 이하입니다.
모든 트럭의 무게는 1 이상 weight 이하입니다.

"""

def solution(b_len, w_limit, truck_lst):
    N = len(truck_lst)

    destination = []
    onbridge = []

    # onbridge.append(truck_lst[0])
    # truck_lst.pop(0)

    t = 0
    while len(destination) < N:
        t+=1
        if (t % b_len) == 0:
            go = onbridge.pop(0)
            destination.append(go)
        if len(truck_lst)>=1:
            if sum(onbridge)+truck_lst[0] <= w_limit:
                onbridge.append(truck_lst[0])
                truck_lst.pop(0)


        # t+=1

    answer = t

    return answer


print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
# print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))