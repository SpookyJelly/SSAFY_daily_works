# 1번 정원에 나무심기

"""

정원은 사각형 모양, 나무는 세로줄로 심음
가장 왼쪽 세로줄 부터 나무 심고, 한줄 씩 띄워심기
나무의 가격을 알고 있을때, 정원에 나무를 심기 위한 총 비용과 심은 나무의 수를 구하자
가장 비싼 나무의 가격과 해당 나무의 열 번호 계산
만약 가장 비싼 나무가 여러개 심어져 있는 경우 가장 큰 열의 "번호" 계산

정원 크기인 N X M 리스트가 주어질 때 나무를 심는 총 비용과 심은 나무의 수, 심은 나무
중 가장 비싼 나무의 가격, 가장 비싼 나무가 심어진 열을 출력하는 프로그램을 만드시오.

[입력 ]
첫 줄에는 테스트케이스 개수 T가 주어진다 . ( 1 < = T < = 1 0 )
다음 줄부터 테스트 케이스의 첫 줄엔 정원의 크기인 행의 개수 N과 열의 개수
M이 주어진다 . (3 <= N <= 20, 3 <= M <= 20)
그 다음 줄부터는 정원 영역이 N 줄에 걸쳐 각 행 별로 M개의 자연수가 공백으
로 구분되어 주어진다 . 주어지는 자연수는 1 0 0이하이다 .
[출력 ]
각 줄에 #과 1부터인 테스트케이스번호를 출력하고 나무를 심는 총 비용 , 심은
나무의 수 , 가장 비싼 나무의 가격 , 가장 비싼 나무가 심어진 열을 빈칸으로 구분
하여 출력하시오 .
"""
import sys
sys.stdin = open('1번_input.txt','r')

# 주어진 리스트의 총 합을 구하는 함수


def mysum(lst: list)->int:
    total = 0
    for idx in range(len(lst)):
        total += lst[idx]
    return total

# 주어진 리스트의 최대값을 구하는 함수


def mymax(lst: list)->int:
    maxi = 0
    for idx in range(len(lst)):
        if lst[idx] > maxi:
            maxi = lst[idx]
    return maxi


# 테스트 케이스가 몇개인지 입력받음

T = int(input())

# 이하 for문을 T번 반복한다.
for tc in range(1, T+1):
    # 변수 N,M을 정수형으로 변환하여 한 라인에서 입력 받는다.
    # N는 행이고, M는 열이다.
    N, M = map(int, input().split())

    # 2차원 배열을 받는 변수 tree. 행의 갯수번 입력 받아야한다.
    tree = [list(map(int, input().split())) for x in range(N)]

    cost = []  # 나무가 심어진 위치와 그 가격을 저장할 변수
    for col in range(M):
        # 만약에 열 번호가 짝수라면 이하를 실행
        # if문의 조건은 짝수일 경우 실행하라고 되어있지만, 이는 인덱스가 0부터 시작하기 때문에 그렇다.
            for row in range(N):
                if col % 2 == 0:
                    # 설계 의도는, 명세에 제시된 대로, 1열부터 왼쪽 위에서부터 아래로 나무를 count 하는 것이다.
                    # 그렇기에, col을 바깥 for문에 위치시켜 안쪽 루프인 row가 다 순환하기 전까지 값이 바뀌지 않게 한다.

                    cost.append(tree[row][col])

    total_cost = mysum(cost)  # 나무 심는데 드는 총 비용을 나타내는 변수
    tree_N = len(cost)  # 심은 나무의 갯수
    expensive_T = mymax(cost)  # 가장 비싼 나무의 값

    # 마지막으로, 가장 비싼 나무가 심어진 열을 찾아야하는데,
    # 만일 여러개 심어져 있는 경우, 가장 큰 열의 번호를 계산해야한다.
    # 따라서, tree 배열 내에서 expensive_T와 동일한 요소를 찾은 후, 그 위치들 중 최대값을 출력한다.
    result = []
    for j in range(M-1, -1, -1):
        for i in range(N-1, -1, -1):
            # tree는 전 범위를 검색하는 것이므로, and j%2 ==0을 통해,
            # 홀수 열만 조사할수 있도록 한다.
            if tree[i][j] == expensive_T and j % 2 == 0:
                where = j+1
                result.append(where)
    # 출력 형식 조정.
    print('#{0}'.format(tc), end='')
    print('', total_cost, tree_N, expensive_T, mymax(result))
    print()
