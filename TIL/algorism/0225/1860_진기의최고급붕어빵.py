#1860번 진기의 최고급 붕어빵 (D3)

"""
오늘은 N명의 사람이 자격을 얻었다.

진기는 0초부터 붕어빵을 만들기 시작하며,
M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.

서빙은 진기가 하는 것이 아니기 때문에,
붕어빵이 완성되면 어떤 시간 지연도 없이 다음 붕어빵 만들기를 시작할 수 있다.

0초 이후에 손님들이 언제 도착하는지 주어지면,
모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별하는 프로그램을 작성하라.


첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 세 자연수 N, M, K(1 ≤ N, M, K ≤ 100)가 공백으로 구분되어 주어진다.

두 번째 줄에는 N개의 정수가 공백으로 구분되어 주어지며,

각 정수는 각 사람이 언제 도착하는지를 초 단위로 나타낸다. 각 수는 0이상 11,111이하이다.

"""
import sys
sys.stdin = open('1860_input.txt','r')

def check():
    for idx in range(N):
        # se = idx번째로 온 손님의 도착 시간
        se = guest[idx]
        # makeC = 그 손님이 도착했을때까지 진기가 만들어놓은 붕어빵의 갯수
        makeC = se//M *K
        # 지금까지 제공했어야할 붕어빵의 갯수
        sell = idx+1
        # 만약 만들어 놓은 붕어빵이, 제공해야할 붕어빵보다 적다면 불가능
        if makeC < sell:
            return "Impossible"
    # 그렇지 않다면 가능.
    return "Possible"

TC = int(input())

for tc in range(1,TC+1):
    N,M,K = map(int,input().split())
    guest = list(map(int,input().split()))
    # 손님들이 도착하는 순서에 따라 정렬.
    guest.sort()
    ans = check()
    print('#{0} {1}'.format(tc, ans))