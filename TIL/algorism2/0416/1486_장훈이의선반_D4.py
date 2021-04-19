# 1486번 장훈이의 선반

# 서점에는 높이가 B인 선반이 하나 있는데 장훈이는 키가 매우 크기 때문에,
# 선반 위의 물건을 자유롭게 사용할 수 있다.
# 어느 날 장훈이는 자리를 비웠고, 
# 이 서점에 있는 N명의 점원들이 장훈이가 선반 위에 올려놓은 물건을 사용해야 하는 일이 생겼다.
# 각 점원의 키는 Hi로 나타나는데, 점원들은 탑을 쌓아서 선반 위의 물건을 사용하기로 하였다.
# 점원들이 쌓는 탑은 점원 1명 이상으로 이루어져 있다.
# 탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 
# 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같다.
# 탑의 높이가 B 이상인 경우 선반 위의 물건을 사용할 수 있는데
#  탑의 높이가 높을수록 더 위험하므로 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑을 알아내려고 한다.

# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 두 정수 N, B(1 ≤ N ≤ 20, 1 ≤ B ≤ S)가 공백으로 구분되어 주어진다.
# S는 두 번째 줄에서 주어지는 점원들 키의 합이다.
# 두 번째 줄에는 N개의 정수가 공백으로 구분되어 주어지며, 각 정수는 각 점원의 키 Hi (1 ≤ Hi ≤ 10,000)을 나타낸다.
# [출력]

# 각 테스트 케이스마다 첫 번째 줄에는 
# ‘#t’(t는 테스트 케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
#  만들 수 있는 높이가 B 이상인 탑 중에서 탑의 높이와 B의 차이가 가장 작은 것을 출력한다.

import sys
sys.stdin = open('1486_input.txt','r')

# 접근 방법 1. 브루트 포스 방법을 이용한 부분집합 구한 후, B랑 인접한 경우 구하기
# 생각해보니까 부분집합을 통한 브루트 포스는 N의 크기가 너무 커서 무리다.
# 부분 집합이여도 통과는 되는구나... 근데 부분집합 경우가 실행시간이 10배 이상 길다.
def sub_power(n: int, lst: list) -> list:
    result = []
    for i in range(1 << n):
        tem = []
        for j in range(n):
            if i & (1 << j):
                tem.append(lst[j])
        result.append(tem)
    return result


# 목표 : 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑을 알아내려고 한다. --> 무작정 키 큰 사람으로 조합해서는 안된다는 것
# 이상적인 것은 선반 높이와 탑 높이가 같은 것이지.
# 재귀호출한 후 되돌아가는 것은, 내가 한 선택을 취소하고 되돌리는것이라고 생각하자.

def binary_weaver(idx,value):
    global min_V
    if value >= B:
        if min_V > value:
            min_V = value

    else:
        for i in range(idx,N):
            binary_weaver(i+1,value+employee_tall[i])
            binary_weaver(i+1,value)
            return

TC = int(input())

for tc in range(1,TC+1):
    N,B = map(int,input().split()) # N : 직원의 수 / B: 탑의 높이
    employee_tall = list(map(int,input().split())) # 인간 탑의 높이 == 인간들의 키의 합
    min_V = 0xfffff
    binary_weaver(0,0)
    print('#{0} {1}'.format(tc,min_V-B))
