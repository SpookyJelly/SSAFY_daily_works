def perm2(n,k):
    global chk
    if chk:
        return
        if k == n :
            t = r = 0
        if ta[0] == ta[1] and ta[1] == ta[2]:
            t+=1
        if ta[3] == ta[4] and ta[4] == ta[5]:
            t += 1
        if ta[0]+1 == ta[1] and ta[1]+1 == ta[2]:
            r += 1
        if ta[3]+1 == ta[4] and ta[4]+1 == ta[5]:
            r+=1
        if t+r == 2:
            chk == True
    else:
        for i in range(n):
            if not visited[i]:
                ta[i] = arr[i]
                visited[i] = True
                perm2(n,k+1)
                visited[i] = False

ta = list(input())
N = len(ta)
chk = False
visited = [False]*N
arr = [1]*N