#5204 병합정렬

# N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2],L[N//2:N]으로 분할 한다.
# 병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.
# 정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.

# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.
# 5<=N<=1,000,000, 0 <= ai <= 1,000,000

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,  N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력한다.
from collections import deque
import sys
sys.stdin = open('5204_input.txt','r')

def Bonaparte(lst:list):
    if len(lst) <= 1:
        return lst
    # 재귀 함수를 통해 계속해서 left와 right로 divide 한다.
    lst_len = len(lst)//2
    left = Bonaparte(lst[:lst_len])
    right = Bonaparte(lst[lst_len:])

    return merge(left,right)

def merge(l_lst,r_lst):
    global cnt
    result =list()
    l_que = deque(l_lst)
    r_que = deque(r_lst)
    # 문제 조건 : 합병 되기 전 왼쪽 리스트의 끝자리가 오른쪽 리스트의 끝자리보다 클 경우 
    if l_que[-1] > r_que[-1]:
        cnt += 1
    while len(l_que)>0 or len(r_que)>0:
        if len(l_que)>0 and len(r_que)>0:
            if l_que[0] < r_que[0]:
                result.append(l_que.popleft())
            else:
                result.append(r_que.popleft())
        elif len(l_que)>0:
            result.append(l_que.popleft())
        elif len(r_que)>0:
            result.append(r_que.popleft())
    return result



TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    presort_lst = list(map(int,input().split()))
    cnt = 0
    L = Bonaparte(presort_lst)
    print('#{0} {1} {2}'.format(tc,L[len(L)//2],cnt))
