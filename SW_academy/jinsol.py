import sys
from pprint import pprint
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1,t+1):
    rst=1
    N = [list(map(int,input().split()))for i in range(9)]
    for i in range(9):
        c,ce = [],[]
        for j in range(9):
            c +=[N[j][i]]
            ce += [N[j//3+(i//3)*3][j%3 +(i//3)*3]]
        sn,sc,sce = set(N[i]),set(c),set(ce)
        if len(sn) !=9 or len(sc) !=9 or len(sce) !=9:
            rst = 0
    print(f'#{tc} {rst}')