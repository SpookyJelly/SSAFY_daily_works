import sys
sys.stdin= open("input_1216.txt","r")

def my_reverse(line):
    r_line = []
    # 뒤에서부터 읽어오면서 뒤집은 리스트를 만들자!
    for i in range(len(line)-1,-1,-1):
        r_line.append(line[i])
    return r_line


def my_find():
    # 전체 크기가 N // 가로를 검사하든, 세로를 검사하든 전체는 N이다.
    for i in range(N):
        # 가로 검사
        # 텍스트 - 패턴 만큼 검사
        for j in range(N-M+1):
            # 이제 여기서부터 패턴과 텍스트를 비교하면서 검사
            # 부분 문자열을 위한 빈 리스트
            tmp =[]
            # 부분 문자열을 완성하는 부분
            for k in range(M):
                tmp.append(words[i][j+k])
            # 회문 검사
            if tmp == my_reverse(tmp):
                return tmp
        
        ##################################
        # 세로 검사
        for j in range(N-M+1):
            tno = []
            for k in range(M):
                tem.append(word[j+k][i])
            if tem == my_reverse(tmp):
                return tmp
        # 문제에서 회문이 1개 존재한다고 하였기에, 필요하지는 않다
        return []


T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())

    words = [list(input()) for _ in range(N)]

    ans = my_find()

    print("{} {}".format(tc, ''.join(ans)))