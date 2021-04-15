# # 5188 최소합
# 그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고,
# 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 
# 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.
# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고,
# 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
import sys
sys.stdin = open('5188_input.txt','r')

def minisum(x,y,value):

    dx = [1,0]
    dy = [0,1]

    que = [[x,y,value]]
    ans = 0xffff
    while que:
        # 별일이 다 있습니다... 최초 코드는 시간초과로 에러가 떴습니다.
        # 별로 비효율적인 코드도 없었는데 왜 이럴까? 고민하다가, 혹시나 하는 마음에 29번 라인을
        # que.pop(0) 에서 que.pop() 으로 바꾸니까 바로 통과가 되었습니다.
        # 딱 한 글자 바꿨는데도, 더 빠른 속도가 나오는걸 몸소 체험하니
        # O(N)과 O(1)의 차이가 이런거구나..라는걸 알게 되었습니다
        x,y,value = que.pop()
        if value < ans:
            for i in range(2):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if [nx,ny] == [N-1,N-1]:
                        ans= min(value+ maps[nx][ny],ans)
                    else:
                        que.append([nx,ny,value + maps[nx][ny]])
    return ans

TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    # 주의 : 변수 이름은 bif 이랑 똑같이 짓지말자.
    # 기본원칙인데, 나도 모르게 행렬 받는 변수 이름을 map으로 하는 바람에 에러가 났다.
    maps = [list(map(int,input().split())) for _ in range(N)]
    print('#{0} {1}'.format(tc, minisum(0,0,maps[0][0])))

# 이후 메모이제이션으로도 풀어보자.
# 재귀구조로도 풀수 있겠다.
