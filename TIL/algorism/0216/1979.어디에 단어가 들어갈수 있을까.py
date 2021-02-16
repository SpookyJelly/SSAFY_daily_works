# 1979번 어디에 단어가 들어갈 수 있을까??

"""

N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는
프로그램을 작성하라.

[제약 사항]

1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.


[출력]

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

"""

# 접근 방법.
# 일단 들어가는 위치의 인덱스는 중요한게 아니기에, K크기를 가진 배열의 갯수에 주목하자.
# 흰색 부분이 1 / 검은색 부분이 0 // 흰색부분에 들어가야한다.
# 일단 퍼즐 모양을 받아준다. (arr)
# 모든 row 와 col 에 대해서 연속된 1의 갯수의 최대값을 세어주자.
# 연속된 1의 갯수를 세어줄 cnt 변수와 끊켰을때 반환받아줄 빈칸 리스트를 만들어준다.
# 반환 받은 빈칸 리스트에서 K가 몇개인지 count 해주면 된다.

TC = int(input())
for tc in range(1,TC+1):
    N, C = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]
    iamtoast = []
    cnt_row, cnt_col = 0,0

    for row in range(N):
        cnt_row = 0
        cnt_col = 0
        for col in range(N):
            # 행에 대해서 연속적인 1인 경우
            if arr[row][col] == 1:
                cnt_row += 1
            else:
                iamtoast += [cnt_row]
                cnt_row = 0

            # 열에 대해서 연속적인 경우
            if arr[col][row] == 1:
                cnt_col += 1
            else:
                iamtoast += [cnt_col]
                cnt_col = 0
        iamtoast += [cnt_row]
        iamtoast += [cnt_col]

    counter = 0
    for element in iamtoast:
        if element == C:
            counter += 1
    print('#{0} {1}'.format(tc, counter))