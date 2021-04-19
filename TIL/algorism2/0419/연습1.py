# 배열의 데이터를 퀵 정렬하시오
# 루모토 알고리즘 사용
import sys
sys.stdin = open('practice1_input.txt','r')

def quicksliver(lst):
    if len(lst) <=1:
        return lst

    N = len(lst)
    next = (N//2)
    pivot = lst[N//2]
    L = 0 # 왼쪽 인덱스 (시작 지점)
    R = N-1 # 오른쪽 인덱스 (가장 끝 지점)

    L_stop = R_stop = False
    # L과 R가 다른 동안 계속 쭉쭉 (혹시 몰라서 범위 체크도)
    while L <= R:
        while 0<=L<N and lst[L] <= pivot:
            L +=1
        while 0<=R<N and lst[R] >= pivot:
            R -=1

        if L<R:
            lst[L],lst[R] = lst[R],lst[L]

        elif L == R:
            lst[L],lst[N//2] = lst[N//2],lst[L]
            left = quicksliver(lst[:next])
            right = quicksliver(lst[next+1:])
            result = left+lst[next]+right
            return result


TC = int(input())
for tc in range(1,TC+1):
    lst = list(map(int,input().split(',')))
    print(lst)
    print(quicksliver(lst))
