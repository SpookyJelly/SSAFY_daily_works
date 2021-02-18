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
