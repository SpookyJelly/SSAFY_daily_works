# IM 대비 문제

"""

SS 텔레콤에서 현재 기지죽의 위치와 집들이 표시된 지도를 2차원 N*N 배열로 변환하여 기지국에 커버되지 않는 집의 수를 찾고자 한다.
기지국 1은 그림과 같이 세가지 종류가 있다. 각각 기지국은 기지국이 위치한 셀에서 동서남북으로 각 1개 2개 3개의 셀을 커버하며, 하나의
집은 1개 셀에 있다.

주어진 2차원 배열 지도에 위치한 기지국으로 커버되지 않는 집의 수를 찾는 프로그램을 작성하시오.

2차원 배열의 크기의 n은 50 이하이다. 기지국의 수는 50 이하이다.

[입력]

첫줄에 테스트 케이스의 수, 그 다음줄 부터 각 테스트 케이스가 n+1개의 줄로 구성
테스트 케이스의 첫줄은 n 이 주어지고, 다음 n개 줄에는 2차원 배열의 각 행이 한줄에 차례로 주어진다.
단, 집이 위치한 원소는 H .기지국이 위치한 원소는 A B C 로 표시하며 각각 동서남북으로 1,2,3개를 커버하는 기지국이다.
X인 원소는 아무것도 없다는 뜻이다.


"""

# 접근 방법
# 입력되는 값(arr)에서 H의 갯수 추리기. -1.
# A B C 가 arr에서 커버하는 공간 살피기. // 뻗어 나가는 조건은, N 안쪽으로만, 다른 A,B,C와 닿지 않을때까지만 뻗기.
# 그 뻗은 공간 내에서 H의 갯수 세기 -2.
# 1.-2. 하기?

import sys
sys.stdin = open('im_input.txt','r')


TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    # 리스트 내포로 가져가지 말고 미리 A,B,C의 정보를 가져갈까?
    arr =[]
    cnt = 0 # 카운팅 받는 변수
    telecom =[]    #그 뭐냐...기지국 있는 장소의 행/열 정보
    for x in range(N):
        a = list(input())
        for idx in range(len(a)):
            if a[idx]=='A'or a[idx] == 'B' or a[idx]== 'C':
                R = x
                C = idx
                telecom.append([R,C])
            elif a[idx]=='H':
                cnt += 1
        arr.append(a)  # 위의 과정을 분석하고, 한줄 씩 어펜드 한다.
    print('arr',arr)
    print('telecom',telecom)
    print('cnt',cnt)
    # 그럼 결과는 기지국과 집의 데이터로 꽉 들어찬 arr 행렬과
    # 기지국의 위치 정보로 차있는 telecom 리스트, 집의 갯수인 cnt 가 있을 것이다.

    # 이제 위치 정보를 기반으로 H 가 몇개인지 세야할텐데, 이건 함수로 만들자

def DreadHorror(arr,telelst):
    telelst[0] = row
    telelst[1] = col

    pass

# 정답 : 4래용!