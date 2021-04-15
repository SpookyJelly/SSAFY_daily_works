#5189번 전자카트

# 골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.
# 사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.
# 각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.
# 두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.
# N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.

import sys
sys.stdin = open('5189_input.txt','r')

# Base idea : Create all route of cart -> Calculate the engery consumption

# Create sector permutation with recursive method
def perm2(arr, n,k):
    if k==n:
        # append to list using shallow copy
        # add start point and end point to make perfect route
        track.append([0]+arr[:]+[0])
    else:
        for i in range(k,n):
            arr[k],arr[i] = arr[i],arr[k]
            perm2(arr,n,k+1)
            arr[k],arr[i] = arr[i],arr[k]

TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    office = [list(map(int,input().split())) for _ in range(N)]
    lst = list(range(1,N))


    track = []
    # make (n-1)P(n-1) permutation
    perm2(lst,N-1,0)

    min_e = 0xfffff
    for items in track:
        total = 0
        # Now, items is a full course. (ex. [0,1,2,0] )
        # So, make sum for each course while selecting items's elements as engery consumption 
        for idx in range(len(items)-1):
            # start = 0 , end = 1 --> office[0][1] --> the engery consumption to reach sector 1 from sector 0
            # start = 1 , end = 2 --> office[1][2] --> the engery consumption to reach sector 1 from sector 2
            # start = 2 , end = 0 --> office[2][0] --> the engery consumption to reach sector 2 from sector 0
            # do these sequence every items
            start = items[idx]
            end = items[idx+1]
            total += office[start][end]
            if total > min_e:
                break
        # pruning
        if total < min_e:
            min_e = total

    print('#{0} {1}'.format(tc,min_e))