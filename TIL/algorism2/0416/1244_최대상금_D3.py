#1244번 최대 상금

# 기본 아이디어
# 재귀 DFS를 이용한 swap


TC = int(input())

for tc in range(1,TC+1):
    num, swap_n : input().split()
    swap_n = int(swap_n)