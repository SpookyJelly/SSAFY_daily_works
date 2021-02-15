# 4839번 이진탐색

"""

책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때,
이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.

"""
# 이번에는 리스트 변경 없이, 인덱스만 건들여보자
# 인덱스 기준으로 생각하자.
def binary (lst,page):
    low = 0
    high = len(lst) -1
    cnt = 0
    while low<=high:
        halfidx = int((lst[low] + lst[high]) / 2)
        if lst[halfidx] == page:
            cnt +=1
            return cnt,halfidx
        if lst[halfidx]>page:
            high = halfidx -1
            cnt+=1
        if lst[halfidx]<page:
            low = halfidx + 1
            cnt+=1
    return -1

for tc in range(1,int(input())+1):
    P,Pa,Pb = list(map(int,input().split()))
    P = list(range(1,P+1))
    print(binary(P,Pa))
    print(binary(P,Pb))

    # 아 진짜 개야마돌게 하네 진짜. 왜 뭐가 문제야 진짜짜