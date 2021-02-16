# 2001번 파리퇴치
"""

리벤지 문제이다. 파리를 잡는 최대값을 구하자...


"""
# 접근 방법
# 일단 인풋 잘 받아주고, 파리채 만들어야지 for 문 두번이면 될거 같은데, 바깥 for문은  열 고정, 안쪽 for문은 행고정

# 파리채가 x축 y축 동시에 움직인다는걸 생각하고, 밖 for문 안쪽 for문 우선순위 잘 생각해봐라

import sys
sys.stdin = open("input2.txt","r")

def mymax(lst):
    max = 0
    for element in lst:
        if element > max:
            max = element
    return max


TC = int(input())
for tc in range(1,TC+1):
    N,M = map(int,input().split())
    N_squ = [list(map(int,input().split())) for __ in range(N)]
    V_sum = 0
    result = []
    for i in range(0,N-M+1):
        for k in range(0,N-M+1):
            V_sum = 0

            # 파리채 무브먼트
            # 파리채 퍼포먼스 거의 다 왔는데 아쉽네
            for col in range(i,i+M): #얘도 0~2 고정
                for row in range(k,k+M): # 2번 반복 / N 이 2이번 # 앞으로 안간다
                    V_sum += N_squ[col][row]
                    result.append(V_sum)

    print('#{0} {1}'.format(tc, mymax(result)))



        # 위에 껄 그냥 함수로 뺀 다음 // 열 단위로 파리 잡아주는 친구