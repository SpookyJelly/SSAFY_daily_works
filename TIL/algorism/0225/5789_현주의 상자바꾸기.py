# 5789번 현주의 상자 바꾸기 (D3)

"""

현주는 1번부터 N번까지 N개의 상자를 가지고 있다.
각 상자에는 숫자를 새길 수 있는데 처음에는 모두 0으로 적혀있다.
숫자가 너무 단조로웠던 현주는 다음 Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경하려고 한다.
변경하는 방법은 다음과 같다.

   ·  i (1 ≤ i ≤ Q)번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경

현주가 Q회 동안 위의 작업을 순서대로 한 다음 N개의 상자에 적혀있는 값들을 순서대로 출력하는 프로그램을 작성하라.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 두 정수 N, Q (1 ≤ N, Q ≤ 103)가 공백으로 구분되어 주어진다.

다음 Q개의 줄의 i번째 줄에는 Li, Ri (1 ≤ Li ≤ Ri ≤ N)이 주어진다.

"""


import sys
sys.stdin = open('5789_input.txt','r')

TC = int(input())

for tc in range(1,TC+1):
    N,Q = map(int,input().split())
    N_lst = [0] * N
    #print(N_lst)
    for i in range(1,Q+1):
        L,R = map(int,input().split())
        for idx in range(L-1,R):
            N_lst[idx] = i
        #print(N_lst)
    print('#{}'.format(tc),end=' ')
    print(*N_lst)