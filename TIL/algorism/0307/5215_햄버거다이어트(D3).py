# 5215번 햄버거 다이어트

"""
민기가 좋아하는 햄버거를 먹으면서도
다이어트에 성공할 수 있도록 정해진 칼로리 이하의 조합 중에서 민기가 가장 선호하는 햄버거를 조합해주는 프로그램을 만들어보자.

(단 여러 재료를 조합하였을 햄버거의 선호도는 조합된 재료들의 맛에 대한 점수의 합으로 결정되고,
같은 재료를 여러 번 사용할 수 없으며, 햄버거의 조합의 제한은 칼로리를 제외하고는 없다.)



[입력]


첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 재료의 수,
제한 칼로리를 나타내는 N, L(1 ≤ N ≤ 20, 1 ≤ L ≤ 104)가 공백으로 구분되어 주어진다.
다음 N개의 줄에는 재료에 대한 민기의 맛에 대한 점수와 칼로리를 나타내는
Ti, Ki(1 ≤ Ti ≤ 103, 1 ≤ Ki ≤ 103)가 공백으로 구분되어 주어진다.


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,
주어진 제한 칼로리 이하의 조합중에서 가장 맛에 대한 점수가 높은 햄버거의 점수를 출력한다.

"""
import sys
from pprint import pprint

sys.stdin = open('5215_input.txt', 'r')


def bit(arr, N,L):
    # N : 재료의 갯수
    all2 = []
    for i in range(1 << N):
        result = []
        limit = 0
        for j in range(N):
            if i & (1 << j):

                limit += arr[j][1]
                if limit > L:
                    break

                result.append(arr[j])

        all2.append(result)
    return all2


TC = int(input())
for tc in range(1, TC + 1):
    N, L = list(map(int, input().split()))  # N 재료의 수 , L = 제한 칼로리
    s = []
    for i in range(N):
        score, cal = list(map(int, input().split()))
        s.append([score, cal])

    sub_set = bit(s, N,L)
    max_score = -1
    for elem in sub_set:
        # 매 요소를 체크할때마다 값 초기화
        ham_cal = 0
        ham_score = 0

        for idx in range(len(elem)):
            ham_cal += elem[idx][1]
            ham_score += elem[idx][0]

        if ham_cal <= L and ham_score > max_score:
            max_score = ham_score

    print('#{0} {1}'.format(tc, max_score))

# 엥? 런타임 에러? 메모리 너무 써서 터진거 아닌가? def가 2의 20승까지 보니까?
# def 단계에서 칼로리 넘는 애들을 치워버릴까? -> 그래도 터졌다
# 내가 볼때는 def에서 길이가 긴 리스트를 반환하려다 보니까, 터지는거 같다. 그래서 아예 반환값을 정수 하나만 해버리는게 나을거 같다
