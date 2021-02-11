# 2일차 - 색칠하기

"""
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.

예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.

2

2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )

3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )



[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )

다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )

color = 1 (빨강), color = 2 (파랑)

"""
# 접근 방법
# 0. 교집합으로 하는게 어떨까 생각해봤다.
# 1. 아니면 리스트가 중복되는 부분에 대해서 cnt 하는 방법을 생각
# 2. 각 사각형을 range와 for문으로 표시하는데, 시작 지점을 입력값인 Color1 / Color2로 조절하는 것이다.
# 3. 전체 사각형을 먼저 그린다.
# 4. 반복문 돌면서 각 Color에 맞는 부분에 1씩 추가... 그럼 결국 겹치는 부분은 2가 되겠네?
# 5. Big_squ의 값이 2인 부분 개수 count 반환
# 조건이 하나 더 있네, 색깔 구분이 있다. 그러면 입력되는 값들을 색상별로 분리해서 큰 색칠영역으로 만드는 것부터 시작하자.
# 기본 아이디어 : 입력받은 사각형을 하나의 셀로 다 쪼갠 다음, 그만큼 다 더하기


# 함수 목적 : 색상 리스트를 조사해, 더 큰 값을 가진 요소로만 반환 --> 쉽지 않다. 오답 가능성 농후
def makeasqu(lst):
    total = []
    # 입력된 인덱스 값으로 색칠되는 모든 경우의 수를 리스트화 해서 반환
    for row in range(lst[0], lst[2]+1):
        for col in range(lst[1], lst[3]+1):
            total.append([row, col])
    return total


for tc in range(1, int(input())+1):
    Color1 = []  # 1번 색상 칠해진 영역들 수용소
    Color2 = []
    for N in range(int(input())):  # 색상 분리해야한다.
        ColorN = list(map(int, input().split()))  # 입력 받는 리스트를 요소에 따라 color1 혹은 2로 넣는다
        if ColorN[4] == 1:  # 마지막 값. 색상에 따라 자료형 분리
            ColorN.pop()
            Color1.append(ColorN)
        else:
            ColorN.pop()
            Color2.append(ColorN)
    Big_squ = [[0]*10 for x in range(10)]  # Big_squ[0] --> 행 // Big_squ[1] --> 열
    # 으으믐...makeaqu로 나오는 반환값으로 어떻게 1씩 더하지
    # 구분은 1과 30으로 하자. 최대 N이 30이니까
    # Color1과 Color2의 모든 요소에 makeasqu를 씌우자
    # 반환은 Color별로 임시 저장해두자.. While로 할까?
    # i는 color1의 길이 j는 color2의 길이
    i, j = len(Color1), len(Color2)
    # 분리된 값을 저장할 리스트
    Color1_sq = []
    Color2_sq = []
    while i > 0 and j > 0:
        for a in range(len(Color1)):
            Color1_sq.extend(makeasqu(Color1[a]))
            i -= 1
        for b in range(len(Color2)):
            Color2_sq.extend(makeasqu(Color2[b]))
            j -= 1

    # 1번 색깔인 경우는 배열에 +1 / 2번 색깔인 경우는 배열에 +30
    for element1 in Color1_sq:
        Big_squ[element1[0]][element1[1]] += 1
    for element2 in Color2_sq:
        Big_squ[element2[0]][element2[1]] += 30

    cnt = 0
    for r in range(10):
        for c in range(10):
            # N의 개수가 최대 30개이므로, 1번 색깔로 30개가 박혀도 cnt는 올라가지 않는다.
            if Big_squ[r][c] > 30:
                cnt += 1
    print(f'#{tc} {cnt}')
