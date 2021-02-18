import sys

import time

start = time.time()

sys.stdin = open("5432_input.txt",'r')
tt = int(input())
for t in range(1, tt + 1):
    n=list(input())
    tmp=0
    check=0
    ans=0
    for i in n:
        if i=='(':
            tmp+=1
            check=1
        else:
            if check==1:
                check=0
                tmp-=1
                ans+=tmp
            else:
                tmp-=1
                ans+=1
    print('#%d %d'%(t,ans))
    print(f"time :", time.time() - start)
