# 두개의 숫자열
"""
N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된
숫자열 Bj (j=1~M) 가 있다.
아래는 N =3 인 Ai 와 M = 5 인 Bj 의 예이다.
Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.
서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.

[제약 사항]

N 과 M은 3 이상 20 이하이다.

"""
# 접근 방법
# 1. 모든 경우의 곱하고 더하는 경우를 구한다.
# 1.1.1 for문 1개 --> A와 B에 동일한 인덱스 적용
# 1.1.1.1 이 루프 끝나고 가장 앞에 insert로 A에 0 집어넣으면 다음칸으로 미는거랑 동일하지 않을까? / B가 짧을 경우도 있으니까 그것도 고려해야겠다.
# 그냥 abs 쓰지말고 나누자 케이스를 (A가 긴 경우 / B 가 긴 경우)
# 2. 그것을 하나의 리스트에 떄려 박는다.
# 3. 최대값 반환
# abs 사용했으면 더 줄일 수도 있었을 듯 하다.
import sys
sys.stdin = open("input (1).txt", "r")


def my_max(lst):
    maxi = 0
    for num in lst:
        if maxi < num:
            maxi = num
    return maxi


for tc in range(1, int(input())+1):
    len_A, len_B = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = []
    if len(A) >= len(B):
        for idx in range(len(A)-len(B)+1):
            # 곱 받아줄 변수 필요
            ans = 0
            for i in range(len(B)):  # i = index of A
                ans += A[i]*B[i]
            result.append(ans)
            B.insert(idx, 0)  # 한 칸 삽입?
    else:
        for idx in range(len(B)-len(A)+1):
            ans = 0
            for i in range(len(A)):
                ans += A[i]*B[i]
            result.append(ans)
            A.insert(idx, 0)

    print('#{0} {1}'.format(tc, my_max(result)))
