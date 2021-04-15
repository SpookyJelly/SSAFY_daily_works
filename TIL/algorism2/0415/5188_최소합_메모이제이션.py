# 메모이제이션의 핵심 : 재귀 / 저장.
# 필요한 것 : 여태까지 이동했던 경로의 숫자합을 받아줄 비어있는 행렬
# 재귀의 베이스 케이스 : 여기서는 현재 위치가 0,0 일 때이다.


from pprint import pprint 
import sys
sys.stdin = open('5188_input.txt','r')

# 최후미 요소에서 시작해서 한칸씩 이동
def memento(row,col):
    # base case
    if [row,col] == [0,0]:
        return arr[row][col]
    # memory 배열의 값이 -1 이 아니면 --> 이미 메모이제이션이 완료 되었다면 --> 그 값을 가져온다
    if memory[row][col] != -1:
        return memory[row][col]
    # 최소값 대신으로 쓸 임의의 큰 수
    up = left = 0xffffff
    # row, col이 범위 이내라면 이전 단계로 이동
    # 범위에 0을 포함하지 않는 이유 : 0을 포함하게 되면 다음 재귀에는 -1이 들어가게 되는데, 
    # 파이썬에서는 이게 에러가 나는게 아니라 마지막 값을 참조하게 되서, 엉망진창이 된다.
    if 0<row<N:
        up = memento(row-1,col)
    if 0<col<N:
        left = memento(row,col-1)
    # 현재 메모이제이션 값은, 위쪽이나 왼쪽의 메모이제이션 된 값의 최소값 + 현재 위치의 arr 값이다.
    memory[row][col] = min(up,left) + arr[row][col]
    return memory[row][col]


TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    memory = [[-1]*N for _ in range(N)]
    arr = [list(map(int,input().split())) for _ in range(N)]



    s = N-1
    print('#{0} {1}'.format(tc,memento(s,s)))