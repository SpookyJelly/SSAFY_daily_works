#1974 스도쿠 검증 (D2)

"""
입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때,
위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.

[제약 사항]

1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.

2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

다음 줄부터 각 테스트 케이스가 주어진다.

테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.
"""
# 행검사, 열 검사 , 사각형 검사 해서 27번 검사를 하면 될듯
# 각 합이 45인지 확인하면 된다.

import sys
sys.stdin = open('1974_input.txt', 'r')

TC = int(input())
#TC = 1
for tc in range(1,TC+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    #print(arr)
    ans = 1
    total = 0
    total2 = 0
    # 행/열 검사
    for row in range(9):
        total = 0
        total2 = 0
        for col in range(9):
            total += arr[row][col]
            total2 += arr[col][row]
        #print(total,total2)
        if total != 45 or total2 != 45:
            ans = 0

    eel = 3 # 사각형 검사
    while eel>0:
        for k in [0,3,6]:
            for R in range(0,7,3):
                t = []
                for i in range(0,3):
                    s = arr[i+k][R:R+3]
                    t.extend(s)
                #print(t)
                #print(sum(t))
                if sum(t) != 45:
                    ans = 0
        eel -= 1

    print('#{0} {1}'.format(tc, ans))