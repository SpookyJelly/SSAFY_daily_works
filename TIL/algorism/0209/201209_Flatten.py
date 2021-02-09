# Flatten
"""
평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.
평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때,
제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.

[제약 사항]

가로 길이는 항상 100으로 주어진다.

모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.

덤프 횟수는 1이상 1000이하로 주어진다.

주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로
그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).

덤프는 항상 1개씩만 옮긴다.
"""
# 접근방법
# 1. dump라는 함수 만듬 (최대밸류 요소에서 최소 밸류 요소로 1씩 시켜줌) -> return : 바뀐 리스트
# 2. dump를 dump_n번 반복
# 3. 변경된 리스트의 차이를 출력

import sys
sys.stdin = open("input (8).txt", "r")


def dump(lst):
    # 최소/ 최대값을 받아줄 변수들. 비교 대상자가 있어야하므로 lst[0]을 초기비교대상으로 선정했다.
    dump_max, dump_min = [lst[0], lst[0]]
    # 밸류로 최소/최대값 찾고, 인덱스로 그 밸류에 접근해야하니, 인덱스를 받아줄 임시 변수도 만들어준다.
    maxi_idx, mini_idx = [0, 0]
    # 전 범위를 순회하며 검사
    for i in range(len(lst)):
        if dump_max < lst[i]:
            dump_max = lst[i]
            # 만약에 이번 루프에서 lst[i]가 최대값이라 판단되면, 그 인덱스 값도 저장한다.
            maxi_idx = i
        elif dump_min >= lst[i]:
            dump_min = lst[i]
            mini_idx = i

    # 실질적인 dump 작업. 리스트의 원본을 바꿔준다.
    lst[maxi_idx] -= 1
    lst[mini_idx] += 1
    return lst


def maximini(lst):
    maxi = 0
    mini = lst[0]
    for element in lst:
        if element > maxi:
            maxi = element
        elif element <= mini:
            mini = element
    return maxi-mini


for tc in range(1, 11):
    dump_n = int(input())
    dumpboxes = list(map(int, input().split()))

    # dump_n이 시행 횟수이니까, 그만큼만 반복할 수 있게 해준다.
    while dump_n > 0:
        dumpboxes = dump(dumpboxes)
        dump_n -= 1

    print('#{0} {1}'.format(tc, maximini(dumpboxes)))
