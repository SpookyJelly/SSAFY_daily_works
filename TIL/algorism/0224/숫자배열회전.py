# 1961 숫자배열 회전 (D2)

# 이건 90도 돌리는거 만든다음 2번 3번 연짱으로 돌리면 된다.

"""

N*N 행렬이 주어질 때, 시계방향으로 90도, 180도,270도 회전한 모양을 출력하라

"""
import sys
sys.stdin = open('1961_input.txt','r')


# 90도 돌리는 친구
def EyeofTerror(arr):
    blank_arr = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):

            # N이 len 이므로, 인덱스로 사용할때는 꼭 -1 을 해주자
            blank_arr[c][N-1-r] = arr[r][c]

    return blank_arr

# 출력 형식 맞춰주기 위해서 한 행을 하나의 문자열로 찌부 시켜준거
def LunaticEyes(arr):
    for row in range(N):
        st = ''
        for col in range(N):
            st += arr[row][col]
        arr[row] = st
    return arr


TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    arr_90 = EyeofTerror(arr)
    arr_180 = EyeofTerror(arr_90)
    arr_270 = EyeofTerror(arr_180)

    ans_arr = [['' for _ in range(N)] for __ in range(N)]

    for element in [arr_90,arr_180,arr_270]:
        element = LunaticEyes(element)


    # 이하는 출력 형식을 맞춰주기 위한 발악
    d_lst = [arr_90,arr_180,arr_270]

    # range(3)인 이유 --> 열이 되어버릴 d_lst가 3개니까.// 각 열은 d_lst에 있는 것들을 실전압축해서 만들어진 것들
    for row in range(3):
        for col in range(N):
            ans_arr[col][row] = d_lst[row][col]
	# 이렇게 ans_arr를 순서에 맞게 만들어도, 이차원 배열이라서 언패킹 한번으로 안된다. 결국 다시 순회하면서 출력해야함
    print('#{0}'.format(tc))
    print(ans_arr)
    print('N:',N)
    for R in range(len(ans_arr)): # len(ans_arr)인 이유...행이 ans_arr개 만큼 필요하니까.
        for C in range(N): # 그럼 여기도 N 일 이유가 없는데? 지금 출력 잘된건, 뒤에 공백이 숨어 있는거였다.. --> 이거 줄일수 있는 방법은?
            print(ans_arr[R][C],end = ' ')
        print()