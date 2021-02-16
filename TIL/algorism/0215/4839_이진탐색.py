# 4839번 이진탐색

"""

애증의 이진탐색...

주의점 1. 인덱스를 잡고 움직이자.
주의점 2. 이 문제에서 정렬대상은 책이므로, range(1,401)을 쓰자
주의점 3. 문제에서 주어진 변수들을 사용하자

잠깐만, range(0,401) 하더라도, 시작값을 1로 설정하면 괜찮지 않을까?
--> 이렇게하면 장점이....인덱스 == 요소


** 여기서 엄청난 주의 사항!! 이하의 풀이는 일반적인 바이너리 서치 알고리즘이 맞으나,
주어진 문제의 조건은, mid 값을 제외하지 않은채, 그대로 다시 써치 범위에 집어넣는다.
이 차이점 때문에 오류가 많이 발생했던 것이다.

*그렇기 때문에 이번 문제는 리스트를 만들 필요 없이 page값을 first와 last에 할당함으로서 풀수도 있었다.

"""


def binary(lst, page):

    first = 1  # 1
    last = len(lst)-1  # len(lst) = 401 --> last == 400
    cnt = 0
    while first <= last:
        l = lst[first]  # l = 1
        r = lst[last]  # r = 400
        mid = int((l+r)/2)
        # a = lst[mid]
        if lst[mid] == page:
            cnt += 1
            return cnt
        elif lst[mid] < page:
            first = mid  # +1 중간 값도 재탐색범위에 들어가기에,
            cnt += 1
        else:
            last = mid  # -1
            cnt += 1


TC = int(input())
for tc in range(1, TC+1):
    P, Pa, Pb = list(map(int, input().split()))
    P = list(range(0, P+1))  # 리스트 크기를 하나 더 늘려서 인덱스 값 == 밸류 값으로 만들어줬다.
    N = len(P)
    if binary(P, Pa) == binary(P, Pb):
        print('#{0} {1}'.format(tc, 0))
    elif binary(P, Pa) < binary(P, Pb):
        print('#{0} {1}'.format(tc, 'A'))
    else:
        print('#{0} {1}'.format(tc, 'B'))
