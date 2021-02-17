def BruteForce2(p,t):
    N = len(t)
    M = len(p)

    # 시작 위치 컨트롤
    # 범위가 요상하게 설정되어 있는 이유가, P의 끝위치가 T의 끝위치와 동일해야하기 때문이다.
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if t[i+j] == p[j]:
                cnt += 1
            else:
                break
        if cnt == M :
            return i
    return -1

print(BruteForce2('aa','eereaeaabr'))