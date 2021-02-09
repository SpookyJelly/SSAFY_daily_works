# 4835번 구간합
"""
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.


첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )
"""

# 접근 방법
# 1. N을 M 크기의 배열로 쪼갠다.
# 2. 그 쪼갠 배열의 요소 합을 어떤 list에 저장해놓는다.
# 3. 어떤 리스트에서 가장 큰 값, 가장 작은 값 추림
# 4. 어떤 리스트 초기화, 반복

import sys
sys.stdin = open("sample_input (4).txt", "r")


def maximini(lst):
    maxi = 0
    mini = lst[0]
    for element in lst:
        if element > maxi:
            maxi = element
        elif element <= mini:
            mini = element
    return maxi-mini


for tc in range(1, int(input())+1):
    len_N, M = list(map(int, input().split()))  # 여기서 list가 없어도 되네?, 난 map 함수는 던더 str가 없어서 이상한 형태로 나오는줄 알았는데
    N = [int(x) for x in input().split()]
    # N을 M크기로 쪼갠 리스트의 요소합을 받아줄 리스트 생성
    sum_lst = []
    # 리스트를 쪼개는 시작, 끝 기준이 매 루프 마다 바뀐다.
    # 시작은 0부터 시작하고, 끝은 len_N에서 끝난다.
    # 그리고 쪼개지는 리스트의 크기는 M이다.
    # 그렇다면 시작은 [0:M] 끝은 [len_N-M:len_N]이 된다. --> 두 리스트 모두 크기를 계산해보면 둘다 M이다.
    # 해당 조건을 생각하면서 range를 설정하자.
    for idx in range(0, (len_N-M)+1):
        New_N = N[idx:idx+M]
        sm = 0
        for num in New_N:
            sm += num
        sum_lst += [sm]
    # 세부 배열의 합을 받은 sum_lst라는 항목의 최소 최대값을 추출하자
    # 사용자 지정 함수인 maximini로 깔끔하게 합차까지 계산하여 반환했다.
    print('#{0} {1}'.format(tc, maximini(sum_lst)))
