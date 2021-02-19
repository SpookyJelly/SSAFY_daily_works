# 1979번 어디에 단어가 들어갈 수 있을까?

"""
N X N 크기의 단어 퍼즐을 만들려고 한다. 
입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가
들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

[제약 사항]

1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 
가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
테스트 케이스의 두 번째 줄부터 
퍼즐의 모양이 2차원 정보로 주어진다.
퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.

"""
# 다시 푸는 친구.
# 기본 아이디어는 전이랑 비슷하다. 1 일때 cnt 올리고, 0이면 cnt 초기화 하는거
# 그런데, 0이 나와서 cnt를 버리기 전에, 다른 어딘가에 빽업을 한 후,
# 그 백업한 친구 안에 K 가 있는지를 확인하는 방식으로 진행 


import sys
sys.stdin = open("1979_input.txt",'r')


# 5 ,7,9 번이 문제군
# 리스트를 받아 그 리스트에 1이 K개 있는 경우를 int 꼴로 반환 
def amI(lst:list,K)->int:
    N = len(lst)
    i,cnt,counter =[0,0,0]
    # 연속된 1의 갯수를 리터럴로 받아주는 친구
    result = []
    # 리스트 전체를 순회 하는 while문. 지금보니까 for문으로 처리하는게 더 깔끔했을듯
    while i<N:
        if lst[i]:
            cnt += 1
        else:
            result += [cnt]
            cnt = 0
        i+=1
    # 마지막 요소가 1인 경우 result에 cnt를 어펜드 하지 못하니까, 탈출하면서 한 번 시켜준다.
    result += [cnt]

    # 만약 result의 요소가 K이면 , counter += 1
    for idx in range(len(result)):
        if result[idx] == K:
            counter += 1
    # 카운터 == 1이 K번 연속으로 등장한 횟수
    return counter



TC = int(input())
#TC = 1 
for tc in range(1,TC+1):
    N,K = map(int,input().split())
    # N,K = 5 ,3 
    BRD = [list(map(int,input().split())) for _ in range(N)]



    # 이번 문제해서 사용할 함수가 리스트를 받으므로, 행렬 자체를 하나의 리스트의 집합으로 만들어야한다.
    # 열과 행이 바뀌어진 리스트를 원래 행렬에 append 하여 모든 행/렬에 대해 검사를 하는것과 동일하게 한다.
    for row in range(N):
        tem = []
        for col in range(N):
            tem.append(BRD[col][row])
        BRD.append(tem)

    # BRD의 모든 요소를 amI 함수에 집어 넣어서, 리스트가 조건을 만족할때마다 += 1 하여 그 모음집을 출력
    ans = 0
    for iz in BRD:
        if amI(iz,K):
            # ans += 1로 하면, 중복이 나왔던 경우도 1개만 가산 하므로 곤란함
            ans += amI(iz,K)
    print('#{0} {1}'.format(tc,ans))




