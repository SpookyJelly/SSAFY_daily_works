# 4834번 숫자카드

"""

0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )

"""

import sys
sys.stdin = open("sample_input (3).txt", "r")


# 최대값 구하는 나만의 함수
def my_max(lst):
    maxx = 0
    for num in range(len(lst)):
        if lst[num] > maxx:
            maxx = lst[num]
    return maxx


# 입력값 T만큼 반복한다.
for tc in range(1, int(input())+1):
    N = int(input())
    ai_list = list(map(int, input()))

    # 몇번 반복되었는지 체크받아줄 변수
    maxi = 0
    # 가장 많이 반복된것으로 판단되는 변수들이 모일 리스트
    result = []
    # ai_list 인덱싱 for문
    for idx in range(len(ai_list)):
        # 등장횟수를 카운팅해줄 임시변수
        cnt = 0
        # 이하의 for문은 1번 for문이 반복됨에 따라 시행이 짧아진다.
        # 왜냐? 어짜피 ai_list[idx] 이전의 문자열들은
        for k in range(idx, len(ai_list)):
            if ai_list[idx] == ai_list[k]:
                cnt += 1
            if maxi <= cnt:
                maxi = cnt
                result += [ai_list[idx]]

# 이제 카드 장수만 같은 경우만 추리면 되는데....
# 내장 함수 안쓰니까 쉽지 않고, PEP 준수도 쉽지 않다.
    print('#{0} {1} {2}'.format(tc, my_max(result), maxi))

# 교수님이 보여주신 방식으로 다시 접근해보자 (key,vaule의 분리)
