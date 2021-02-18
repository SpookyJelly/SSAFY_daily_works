# 4861번 회문

"""
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다.
NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.



[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

"""

#접근법 : 일단 회문을 어떻게 찾을지를 생각해야지.. 원본과의 비교?? -> 제일 클래식하지
# 다만 문제점은 이게 빙고꼴이니까..세로로 작성되어 있는걸 가로행으로 변환한 다음 원본 리스트에 어펜드 하자
# 그리고 전체 리스트에 대해서 검사.. 테스트 케이스 몇개 안되니까 괜찮을 거 같은데?
# 몇개 있는것을 찾는것도 아니고, 어디에 있는것들 찾는것도 아니라, 어떤게 있는지를 찾는거니까
# 회문도 1개 존재니까 바로 retun하면 되겠네.




import sys
sys.stdin = open('4861_input.txt','r')

# Pen 함수의 역할

# 문자열를 한개씩 받아 회문여부를 판단해서, 회문이면 그 리스트로 반환
# 근데 문제가 있다 시발....리스트 자체가 아니라, 리스트 내부에 회문이 있을 수도 있다!
# for문 돌려서 점점 orgin/sample의 길이가 M이 될때까지 바꿔야지 시발


def Pen(lst,M)->list:
    i = 0
    # 해당 while문은 회문을 판단할 부분, 그러니까 M 크기로 썰어놓은 list를 계속 수정하는 것이다.
    # 회문 판단할 문자열의 길이는 M이 되도록 유지하고, 매 루프마다 그 시작점이 1씩 이동하게 한다.
    # 또한 리스트의 끝 문자열인 i+M의 크기는 파라미터인 lst의 길이를 넘지 않도록 한다.
    while i+M <= len(lst):
        orgin = list(lst)[i:i+M]
        sample = list(lst)[i:i+M]
        N = len(orgin)
        for idx in range(N//2):
            sample[idx], sample[N - 1 - idx] = sample[N - 1 - idx], sample[idx]
        if orgin == sample:
            return sample
        i+=1


TC = int(input())

for tc in range(1,TC+1):
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
    #print(arr)
    for row in range(N):
        # 열 기준으로 뽑은 문자열을 받아줄 swap
        swap = ''
        for col in range(N):
            swap += arr[col][row]

         # N과 arr은 별개이기에, arr에 잘 어펜드 되는 모습이다
        arr.append(swap)
    #print(arr)
    #print(len(arr))


    for idx in range(len(arr)):
        ans = Pen(arr[idx],M)
        if ans:
            print('#{0} {1}'.format(tc,''.join(ans)))
