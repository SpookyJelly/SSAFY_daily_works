# 순서는 오른쪽,오른쪽 아래, 아래, 왼쪽 아래를 살펴보겠다
#  오른    행 0 / 열 1
# 오른 아래  행 1 / 1
# 아래 행 1 / 열 0
# 왼쪽 아래 행 1 / 열 -1
dr =[0,1,1,1]
dc =[1,1,0,-1]




def check():
    # 이차원을 순회하면서 해당 정점을 시작으로 4군데 검사를 실시한다.
    for i in range(N):
        for j in range(N):
            # 4방향을 살펴볼 것.
            for k in range(4):
                o_cnt = 0
                nr,nc = i,j # 왜 nr \nc를 새로 만드냐? i,j를 직접 컨트롤하게 되면 이상한 값으로 갈 수도 있어서.
                # while문 조건 순서 바뀌면 매우 곤란하다
                while 0<=nr<N and 0<=nc<N and arr[nr][nc] == 'o':
                    o_cnt += 1
                    if o_cnt ==5:
                        return 'YES'
                    nr +=dr[k]
                    nc +=dr[k]





    return "NO"






T = int(input())

for tc in range(1,T+1):
    N = int(input())

    # 오목판 만들기. 리스트 아닌 이유는, 내용물을 바꿀 필요가 없기 때문이다.

    arr =[input() for _in range(N)]

    print("#{} {}".format(tc,check()))