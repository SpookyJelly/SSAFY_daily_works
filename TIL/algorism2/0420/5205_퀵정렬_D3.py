# 퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.
# [입력]

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.
# 5<=N<=1,000,000, 0 <= ai <= 1,000,000

# [출력]

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, , N/2번 원소를 출력한다.
import sys

sys.stdin = open('5205_input.txt', 'r')


def quick(lst, l, r):
    # l,r은
    # 각각 검사의 시작과 끝 인덱스를 나타냄
    # l,r은 s값에 따라 변하므로(재귀를 반복하면서) l>=r 조건으로 올 수 있다. (quick(lst,l,s-1)을 계속 타고 재귀할 경우)
    # 그러나 l>=r은 우리가 정렬할 수 있는 조건이 아니므로, return 시켜준다.
    if l >= r:
        return
    # l<r 이라는 것은 아직 더 검사의 여지가 있다는 것이다
    if l < r:
        s = partition(lst, l, r)
        # s는 새로운 피벗의 위치이고, partition 함수에 의해서 s 위치에 올바른 값까지 들어가 있다.
        # 새로운 피벗 위치를 제외하고 재귀로 다시 돌린다.
        quick(lst, l, s - 1)
        quick(lst, s + 1, r)


def partition(lst, i, j):
    l = i
    r = j
    # i,j = 각각 초기값
    pivot = lst[i]
    # l은 지나오면서 전부 피벗 값보다 작거나 같은 녀석들을 만나는게 정상
    # r은 지나오면서 전부 피벗 값보다 크거나 같은 녀석들을 만나는게 정상
    while l <= r:  # 0 while
        # 현재 l이 정상이면 l+=1
        # 여기서도 범위 체크를 해줘야한다. 만약에 현재 피벗이 최대값이라면 while 조건을 탈출하지 못한다.
        # l의 탐색 종료 시점은, r과 만났을때이다. 따라서, l<=r 동안만 값이 커지게 하자
        while l <= r and lst[l] <= pivot:  # 1 while
            l += 1
        # 현재 r이 정상이면 r을 작아지게 한다.
        # 1 while 조건에 의해 l==r --> l +=1 --> l>r 으로 state가 변경되어 이 while문을 아예 거치지 않을 수도 있다.
        while l <= r and lst[r] >= pivot:  # 2 while
            r -= 1
        # l과 r 둘다 비정상 상황을 조우하여 while문을 둘다 탈출한 상황인데, 아직 서로가 교차하지 않은 상황 (l<=r)조건을 유지하고 있으면,
        # 두 값을 swap 시켜주어 다시 0 while로 돌아가게 한다
        if l <= r:
            lst[l], lst[r] = lst[r], lst[l]

    # 여기는 l>r일때 도달한다.
    # l>r 이라는 뜻은 두 포인터가 서로 교차했다는 것이고, 교차한 지점( 두 포인터가 같은 위치에 있다가, 변경된 지점. 여기서는 r이 더 늦게 움직이므로, r의 위치가 곧
    # 새로운 피벗의 위치가 된다.)
    lst[i], lst[r] = lst[r], lst[i]
    # 새로운 피벗의 위치를 반환한다.
    return r


TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    quick(lst, 0, N - 1)
    print('#{0} {1}'.format(tc, lst[N // 2]))
