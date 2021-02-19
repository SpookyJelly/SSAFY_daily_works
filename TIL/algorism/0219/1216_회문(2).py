import sys
sys.stdin = open("1216_input.txt","r")

def my_find(M):
    # 전체크기가 N이다.
    for i in range(N):
        # 부분 문자열의 시작점
        for j in range(N-M+1):
            #스왑을 응용한 회문 검사
            # 바꾸는 횟수가 패턴의 길이와 관계가 있는거지
            
            # 가로 검사
            for k in range(M//2):
                if words[i][j+k] != words[i][j+M-1-k]:
                    break
                elif k ==M//2 - 1:
                    return M

            # 세로 검사
            for k in range(M//2):
                if words[j+k][i] != words[i][j+M-1-k]:
                    break
                elif k == M //2 -1:
                    return M




for tc in range(10):
    tc_num = int(input())

    N = 100

    words = [input() for i in range(N)]

    # 가장 길이가 긴 회문검사를 한다
    for i in range(N,0,-1):
        ans = my_find(i)
        if ans:
            break
    print("{} {}".format(tc_num,ans))