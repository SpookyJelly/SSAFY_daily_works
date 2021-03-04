#5097번 회전 (D2)

"""

N개의 숫자로 이루어진 수열이 주어진다.
맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때,
수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 N과 M이 주어지고,
다음 줄에 10억 이하의 자연수 N개가 주어진다. 3<=N<=20, N<=M<=1000,

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.

"""
# 핵심 : 무작정 M번 반복하는 것이 아니라, 일정 주기로 원래 모습으로 돌아온다.
# 그 사이클을 파악하여 적은 횟수만 작업을 수행하도록 한다.

import sys
sys.stdin = open('5097_input.txt','r')



TC = int(input())

for tc in range(1,TC+1):
    N,M = map(int,input().split())
    int_lst = list(map(int,input().split()))

    donum = M%N
    for i in range(donum):
        first = int_lst.pop(0)
        int_lst.append(first)


    print('#{0} {1}'.format(tc, int_lst[0]))