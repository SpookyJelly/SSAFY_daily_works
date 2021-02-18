# 4861번 회문 문제. 교수님 솔루션 버젼

# 문제를 풀때는 가장 어려운 데이터로 연습하는게 낫다. (안그럼 그리디 알고리즘의 함정에 빠진다)
# 예를 들면 N 큐브가 20*20 이고, 찾으려는 데이터가 13일때,
# 0~12 / 1~12 / 2 ~13 ....7~19로 범위로 데이터를 수정하면서 회문 확인을 해준다.

"""
모든 가로에 대해서 (0~19)
for r in range(N):
    for i in range(0, N-M+1):
        print(BRD[r][i])

모든 세로에 대해서
for c in range(N):
    for i in range(0,N-M+1):
        print(BRD[i][c]
                # 안쪽 for문인 i가 C보다 먼저 계속 바뀌니까, 열이 된다는 사실을 곱씹어보자.

"""

def chkP(chkstr):
    print(chkstr)
    if chk~~


def allChk():
    for n in range(M):
        for i in range(N-M+1):
            # 가로시작점
            if chkP(BRD[n][i:i+M]):
                return BRD[n][i:i+M]

            # 세로시작점
            tempS =''
            for k in range(i,i+M):
                tempS = tempS + BRD[k][n]
            if chkP(tempS):


TC = int(input())
for tc in range(1,TC+1):
    N,M = map(int,input().split())
    BRD = [input() for _ in range(N)]

    #가로줄에 대한것을 체크해보자



    # 전체 세로줄에 대한 것을 체크해보자
