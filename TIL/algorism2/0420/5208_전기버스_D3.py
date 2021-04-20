#5208번 전기 버스

# 충전지를 교환하는 방식의 전기버스를 운행하려고 한다. 정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.
# 충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야 한다.
# 정류장과 충전지에 대한 정보가 주어질 때, 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오. 단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.


# [입력]
#
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 한 줄에 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi가 주어진다. 3<=N<=100, 0 ＜ Mi ＜ N
import sys
sys.stdin = open('5208_input.txt','r')

# 핵심 아이디어 : 거꾸로 생각하기
# 도착 지점에서부터 스캔, 도착지점 이전의 각 정류장에서 도착지로 도달할 수 있는지를 확인 (출발지 인덱스 + 배터리 용량) >= 도착지 인덱스 --> 도달 가능
# 도달 가능한 놈들만 스택에 집어넣는다. -> 스택에서 pop 하면서 반복 -> pop으로 나온 출발지 = 새로운 도착지로 하여 반복 (추가로 cnt += 1)
# 다만 스택에 집어넣을 때 신경 써야할 것이, 현재 도착지에서 가장 멀리 있는 지점이 먼저 OUT 될 수 있게 설계해야한다.
# 불필요한 가지를 자르는 것이 핵심인데, 상식적으로 생각해보았을때, 출발지와 도착지 간의 스탭이 큰 경우가 더 정답에 근접하지 않겠는가?
def reverse(goal):
    global mini
    stack = [[goal,0]]

    while stack:
        sub_goal,cnt = stack.pop()
        # 뽑았는데, cnt가 최소값보다 크다면, 더 볼 필요 없다. continue로 이번 루프를 넘긴다.
        if cnt > mini:
            continue
        if sub_goal == 1:
            mini = cnt
        else:
            # 도착지점에 도달 할 수 있는 경우들 중, 출발지와 더 가까운 곳이 더 먼저 스택에서 빠질 수 있도록
            # 거꾸로 조사하면서 append 하였다.
            for idx in range(sub_goal-1,0,-1):
                sub_test = idx + bus_lst[idx]
                if sub_test >= sub_goal and cnt<mini:
                    stack.append([idx,cnt+1])


TC = int(input())
for tc in range(1,TC+1):
    bus_lst = list(map(int,input().split()))
    goal = bus_lst.pop(0)
    # 인덱스를 문제에서 주어지는 버스정류장 번호로 쓰기 위해서 수도 값을 0번 인덱스에 위치 시켜주었다.
    bus_lst = ['null']+bus_lst
    mini = 0xffffff
    reverse(goal)
    # 출발지에서 배터리 갈아끼우는 것은 count 하지 않으므로, -1을 해준다.
    print('#{0} {1}'.format(tc,mini-1))
