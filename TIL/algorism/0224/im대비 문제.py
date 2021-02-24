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


# 델타를 이용해서 만들자
# 상 우 하 좌

dr = [-1,0,1,0]
dc = [0,1,0,-1]
                # 사실 arr도 외부에서 참조가 되기에, 굳이 parameter로 받지 않아도 되는데
                # 나는 혹시나 하는 마음에, 베이스는 받는 편을 선호한다.
                # 그런거 치고는 dr,dc는 잘만 외부에서 받았다.. ㅋㅋ
def DreadHorror(arr,telelst):
    row = telelst[0]
    col = telelst[1]
    #print(telelst)
    #print(arr[2][3])
    # 들어온 친구에 대해서만 4방향 보면 되잖아.
    if arr[row][col] == 'A':
        loop = 1
    if arr[row][col] == 'B':
        loop = 2
    if arr[row][col] == 'C':
        loop =3
    #print('loop : ',loop)
    #print('N',N)
    # cnt = 0 # cnt는 총 각 케이스 별로 누적되어야할 값이니까, 밖으로 빼줘서 초기화 안되게 한다.
    for k in range(4):
        # 각 방향별로 n번씩 살피자.
        i = 0
        row = telelst[0] # 여기서 찾을 기준점 초기화 해줘야지, 안 그러면
        col = telelst[1] # 방향 탐색 끝난 다음의 위치에서부터 다른 방향으로 간다. (북쪽 방향 탐색 끝난 다음, 그 위치에서 오른쪽 탐색함)
        while 0<=row<N and 0<=col<N and i<=loop: # i<= loop인 이유 -> 이 while문은 탐색 시작 기준은 언제나 자기 자신에서부터 시작한다. 자신을 검색하는것도 count에 들어가기 때문에, 이걸 빼먹는다면 , 스스로 검색하고 끝나는 경우도 있음
            if arr[row][col] == 'H':
                arr[row][col] = 'X'
            #print('i', i )
            #print('row , col',row,col)
            #print('arr[row][col] : ', arr[row][col])
            row += dr[k]
            col += dc[k]
            i+=1

    return arr
# 아니 그냥 범위 내에 있는 친구들을 count 해줄라고 했는데, 그러면 2개 기지국에 중복된 애들까지 다시 세어버려서....에러..
# 그래서 교수님 방법 대로, 기지국 범위 내에 있는 H들을 X로 덮어씌워줬다.
# 이거 하면서 실수가 많았던게, row에 들어갈 변수와 col에 들어갈 변수를 제대로 구분 못했던 것이다. 그래서 이상한 값 나왔는데, 그거 보고 곤란한 적이 많았다.
# 두번째로는, == 와 = 실수....ㅋㅋㅋ 당황해서 만든 오타라고 믿겠다.


import sys
sys.stdin = open('im_input.txt','r')


TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    # 리스트 내포로 가져가지 말고 미리 A,B,C의 정보를 가져갈까?
    arr =[]
    count = 0 # 카운팅 받는 변수
    telecom =[]    #그 뭐냐...기지국 있는 장소의 행/열 정보
    for x in range(N):
        a = list(input())
        for idx in range(len(a)):
            if a[idx]=='A'or a[idx] == 'B' or a[idx]== 'C':
                R = x
                C = idx
                telecom.append([R,C])
            elif a[idx]=='H':
                count += 1
        arr.append(a)  # 위의 과정을 분석하고, 한줄 씩 어펜드 한다.
    #print('arr',arr)
    #print('telecom',telecom)
    #print('cnt',cnt)
    #print(DreadHorror(arr,[2,3]))
    ans = 0
    for k in range(len(telecom)):
        arr = DreadHorror(arr,telecom[k])
        #print(arr)
    num_H = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'H':
                num_H += 1


    #print('H 의 수',num_H) # 15개에서 4개로 줄어들었다.

    print('#{0} {1}'.format(tc,num_H))



    #print('바뀌기 전 H',count) # 기지국 전파 발사 이전



    # 이런! 중복도 카운트 하는 바람에 output이 다르게 나왔다!


# 정답 : 4래용! --> 잘 나왔다.