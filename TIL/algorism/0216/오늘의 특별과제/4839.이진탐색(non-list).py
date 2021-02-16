# 4839번 이진탐색

"""
이 망할 이진탐색 문제는 사실 input으로 리스트가 없이도 풀 수 있다고 한다.

mid값을 그대로 page로 이동하는 방법등으로 진행하자

지금 인덱스와 데이터가 일치하는 상황 ..!!! index == data

#후기 : 진짜 쉽지 않았다.....유연한 사고를 가져야겠다는 생각을 한다...
"""

def binary(P,page):
    first = 1
    last = P
    cnt = 0
    while first <= last:
        mid = int((first+last)/2)
        if mid == page:
            cnt += 1
            return cnt
        elif mid < page:
            first = mid
            cnt += 1
        elif mid > page:
            last = mid
            cnt += 1
    return -1


TC = int(input())
for tc in range(1, TC+1):
    P,Pa,Pb = list(map(int,input().split()))
    if binary(P,Pa) == binary(P,Pb):
        print('#{0} {1}'.format(tc,'0'))
    elif binary(P, Pa) < binary(P, Pb):
        print('#{0} {1}'.format(tc, 'A'))
    elif binary(P, Pa) > binary(P, Pb):
        print('#{0} {1}'.format(tc, 'B'))