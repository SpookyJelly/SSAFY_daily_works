#1865번 동철이의 일분배

# 동철이가 차린 전자회사에는 N명의 직원이 있다.
# 그런데 어느 날 해야할 일이 N개가 생겼다.
# 동철이는 직원들에게 공평하게 일을 하나씩 배분하려고 한다.
# 직원들의 번호가 1부터 N까지 매겨져 있고, 해야 할 일에도 번호가 1부터 N까지 매겨져 있을 때, i번 직원이 j번 일을 하면 성공할 확률이 Pi, j이다.
#
# 여기서 우리는 동철이가 모든 일이 잘 풀리도록 도와주어야 한다.
# 직원들에게 해야 할 일을 하나씩 배분하는 방법은 여러 가지다.
# 우리는 여러 방법 중에서 생길 수 있는 “주어진 일이 모두 성공할 확률”의 최댓값을 구하는 프로그램을 작성해야 한다.


# [입력]
#
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤ N ≤ 16)이 주어진다.
# 다음 N개의 줄의 i번째 줄에는 N개의 정수 Pi, 1, … , i, N(0 ≤ Pi, j ≤ 100)이 주어진다.
# Pi, j는 i번 사람이 j번 일을 성공할 확률을 퍼센트 단위로 나타낸다.
import sys
sys.stdin = open('1865_input2.txt','r')

def perm(L,percent):
    global maxi
    if L == N:
        if percent > maxi:
            maxi = percent
        return
    else:
        # 가지치기를 재귀 들어가기전에 시행한다.
        # 아직 도착점에 도달하지도 않았는데도 maxi보다 값이 큰 우량아들만 검사를 한다.
        # 막판 포텐셜도 모르는데 벌써 가지치는건 이른거 아닌가? 라고 생각할 수 도 있는데,
        # 앞으로 계속 소수만 곱할기에, 계속 진도가 나가도 현재 percent argument보다 더 커지는것은 불가능하다.
        if maxi < percent:
            for i in range(N):
                if not visited[i]:
                    # a = table
                    visited[i] = True
                    per = (table[L][i])*0.01
                    perm(L+1,percent*per)
                    visited[i] = False
    return
TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]
    visited = [False]*N
    sel = [i for i in range(N)]
    maxi = 0
    perm(0,1)
    # 소숫점 0도 표시하고 싶으면 ( 엄격한 표기법 )  round보다 format을 써라. round는 0은 그냥 생략한다
    print('#{}'.format(tc),end= ' ')
    print(format(maxi*100,".6f"))