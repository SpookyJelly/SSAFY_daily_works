# 1861번 정사각형 방

# N2개의 방이 N×N형태로 늘어서 있다.
# 위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.
# 당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
# 물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
# 처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.

# 입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N (1 ≤ N ≤ 103)이 주어진다.
# 다음 N개의 줄에는 i번째 줄에는 N개의 정수 Ai, 1, … , Ai, N (1 ≤ Ai, j ≤ N2) 이 공백 하나로 구분되어 주어진다.
# Ai, j는 모두 서로 다른 수이다.


# [출력]

# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 한 칸을 띄운 후, 처음에 출발해야 하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지를 공백으로 구분하여 출력한다.
# 이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력한다.

# 기본 아이디어 : 
# 1. 숫자 N 이 있는 위치에서 이동이 가능한지를 표시하는 리스트 A를 만든다
# 2. 이동이 가능하다면 해당 숫자를 인덱스로 하여 A에 1로 표시한다.
# 3. 리스트 A에 연속된 1의 갯수 + 1이 연속해서 이동 가능한 최대 횟수이다.
def close_room_searcher(arr):
    V_lst = [0]*((N**2)+1)
    # 델타 무브 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(len(arr)):
        for j in range(len(arr)):
            for idx in range(4):
                n_x = i + dx[idx]
                n_y = j + dy[idx]
                if 0<=n_x<N and 0<=n_y<N and arr[n_x][n_y] == arr[i][j]+1:
                    # 여기가 핵심이다. maze 행렬이 N*N 크기로 구성되어있고,
                    # 1~N까지의 숫자가 하나만 있다는 점을 이용하여, "N번 숫자가 있는 곳은 이동할 여지가 있다" 라는 것을 표시함
                    # 그렇기에 표시가 한 리스트에 연속된다면, 연속해서 이동할 수 있다는 뜻이 되는것
                    V_lst[arr[i][j]] = 1
    return V_lst

# 시작 위치 및 최대 이동 횟수 찾는 함수
def counting_stars(lst):
    maxi = 0
    cnt = 0 # 최대 이동 가능한 방의 갯수
    start = 0 # 시작 위치
    for idx in range(len(lst)):
        if lst[idx]:
            cnt+=1
        else:
            # lst가 1이 아니면, 여태까지 나온 최대값이랑 비교
            # 문제의 조건에 따라 동일한 최대값이면, 가장 숫자가 적은 것을 출력해야하니 LT를 사용했다.
            if maxi<cnt:
                maxi = cnt
                start = idx - cnt
            cnt = 0
    return [str(start),str(maxi+1)]




import sys
sys.stdin = open('1861_input.txt','r')

TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    maze = [list(map(int,input().split())) for _ in range(N)]
    result = close_room_searcher(maze)
    ans = ' '.join(counting_stars(result))
    print('#{0} {1}'.format(tc,ans))
