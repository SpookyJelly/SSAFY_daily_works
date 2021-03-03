def solution(b_len, w_limit, truck_lst):
# 굉장히 무식한 방법으로 해결했습니다.
# 메모리 낭비, 시간 낭비의 정점을 찍었다고 자부합니다.

# 알고리즘 설계가 안되어서, 홧김에 그냥 진짜 다리를 만들었습니다.
    N = len(truck_lst)


    bridge = [0] * b_len
    # a = truck_lst
    destination =[]
    t = 0
    while len(destination) < N:
        # 다리 앞에 도착했을때, 트럭을 뽑아냅니다
        if bridge[0] != 0:
            destination.append(bridge[0])
            bridge.pop(0)
            bridge.append(0)

        else: # 아무일 없어도 앞으로 간다.
            bridge.pop(0)
            bridge.append(0)
        # 근데, 트럭이 이미 한대 이상 올라가 있는데, 추가로 트럭이 올라가는 경우가 있습니다.
        # (조건에 따르면, 기존에 올라가 있던 트럭이 온전히 올라간 이후에 발생하는 사건)
        if len(truck_lst)>=1:
            # 그러한 경우, 다리 전체에 올라가 있는 트럭의 무게 + 대기열 가장 앞의 트럭 무게
            # 가 다리의 하중 이하 일 경우, 트럭 한대를 더 올려줍니다.
            # 한 대인 이유 : 1초에 한대 씩 올라 갈 수 있기에
            if sum(bridge) + truck_lst[0] <= w_limit:
                bridge.pop()
                bridge.append(truck_lst[0])
                truck_lst.pop(0)


                # 처음에는 여기서도 t+=1을 했다.
                # 근데, 다리에 올라가는것 자체가 동일 시간내에 이루어지므로, 무관하다고 생각합니다
                #t+=1




        t+=1


    return t


print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))