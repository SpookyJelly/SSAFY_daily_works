# 5207 이진탐색
# 서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다.
# 그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.
# 전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면, 중심 원소의 인덱스 m=(l+r)//2 이고,
# 이진 탐색의 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1부터 r이 된다.
#
# 이때 B에 속한 어떤 수가 A에 들어있으면서,
# 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.
#
# 이때 m에 찾는 원소가 있는 경우 방향을 따지지 않는다. M개의 정수 중 조건을 만족하는 정수의 개수를 알아내는 프로그램을 만드시오.
"""

패착원인
1. 문제의 조건을 잘못 이해했다. 오-오 / 왼-왼 같이 연짱으로 같은 방향 나오는 놈들을 나가리 시키는건데, 왼-오 / 오-왼 이 나오지 않는놈들을 나가리 시켰다.
2. 재귀 전에 이전 단계 상태를 표시할때, parameter를 괜히 2개 씩이나 설정하였고, 그것의 컨트롤을 잘 하지 못했다.
3. flag를 직관적인 문자열로 바꾸는 것 또한 생각했으면 좋았을껄, 굳이 진위형/숫자형 flag를 받겠다고 끙끙 앓았다. ==> 풀이가 잘 안되면 잠깐 다른 생각을 해보던가 해야지

"""
import sys
sys.stdin = open('5207_input.txt','r')

# init --> lst : lst , l= 0 , r= len(lst)-1
# flag 진입 조건 변경 숫자로 바꾸는것
# def bin_search(l,r,l_flag,r_flag):
#     global cnt
#     m = (l+r)//2
#     if l<=r and 0<=m<N :
#         if A[m] == goal:
#             cnt+=1
#         else:
#             if A[m] < goal: # 오른쪽 탐색
#                 if not r_flag:
#                     bin_search(m+1,r,l_flag,True)
#             else: # 왼쪽 탐색
#                 if not l_flag:
#                     bin_search(l,m-1,True,r_flag)
#     return

#
def bin_search(l,r,flag):
    global cnt
    m = (l+r)//2
    # 범위 체크 (혹시 모르니까)
    if l<=r and 0<=m<N :
        if A[m] == goal:
            cnt+=1
        else:
            if A[m] < goal: # 오른쪽 탐색
                if flag == 'right': return

                bin_search(m+1,r,'right')
            else: # 왼쪽 탐색
                if flag== 'left':return

                bin_search(l,m-1,'left')
    return


TC = int(input())

for tc in range(1,TC+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    cnt = 0
    A.sort()
    for goal in B:
        bin_search(0,N-1,'null')
    print('#{0} {1}'.format(tc, cnt))