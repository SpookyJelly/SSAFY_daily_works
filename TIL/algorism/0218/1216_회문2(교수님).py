import sys
sys.stdin = open("1216_input.txt","r")

#문자열인지 회문인지를 확인하여 boolean으로 return
def chkP(chkstr):
    l = len(chkstr)
    for i in range(l//2-1):
        if chkstr[i] != chkstr[l-1-i]:
            return False
    return True


# 길이가 M인 회문을 문자열을 return
def allChk_old(M):
    for n in range(N):
        for i in range(N - M + 1):
            # 가로시작점
            if chkP(BRD[n][i:i + M]):
                return BRD[n][i:i + M]

            # 세로시작점
            tempS = ''
            for k in range(i, i + M):
                tempS = tempS + BRD[k][n]
            if chkP(tempS):
                return tempS

    return ''


# 함수의 목적 : M 길이의 회문이 전체 BRD에 존재하는가를 찾고, 있다면 길이 M을 반환.
def allChk(M): # M은 회문의 길이.
    for i in range(N): # 가로 기준으로 행. 행에 있는 문자열을 체크하겠다라는 말...
        for j in range(N-M+1): # j : j+M를 체크해야한다. / 회문이기에, 처음과 끝을
    # 여기서 주목해야할 것은 사실 i는 요소 하나하나를 고정해주는 것이고,
    # 실제 값이 변경되는 것은 변수 j 이다.
    # j와 pos 두 변수의 이동으로 회문 검사는 가생이에서 가운데로 집결하게 되는 것이다.
    # pos는 점점 커지는 변수.... 가장 앞에 있는 비교자를 앞으로 밀어주는 한편, 뒤에 있는 문자를 가운데로 강겨준다.
    # 이거 좀 진득하게 해봐야겠다.
            #가로
            pos = 0
            while pos < M//2 and BRD[i][j+pos] == BRD[i][j+M-1-pos]: #갯수가 차서 나오는 경우, 내용이 서로 달라서 나옴
                pos += 1
            if pos == M//2:
                return M

            #세로
            pos = 0
            while pos < M//2 and BRD[j+pos][i] == BRD[j+M-1-pos][i]: #갯수가 차서 나오는 경우, 내용이 서로 달라서 나옴
                pos += 1
            if pos == M//2:
                return M
    return 0





TC = 10
for tc in range(1, TC+1):
    t = input()
    N = 100
    BRD = [input() for _ in range(100)]

    retV = 0
    for l in range(100,1,-1):
        #if len(allChk(l)) > 0 :
        if allChk(l) > 0 :
            retV = l
            break


    print('#{} {}'.format(tc, retV))
