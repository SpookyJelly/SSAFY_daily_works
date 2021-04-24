#5247번
# 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
# 사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때
# 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.
# 단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.
# 예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.


# [입력]
# 첫 줄에 테스트 케이스의 개수가 주어지고, 
# 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M

import sys
sys.stdin = open('5247_input.txt','r')

"""

처음에는 재귀로 풀어볼라고 했는데, 계속 삑이 났다(재귀 한도초과), 그래서 거꾸로도 생각해보려고 했는데, 마찬가지 결과였다.
결국 이 문제는 한단계 한단계씩 나아가는 BFS 문제라는 것을 알게 되었다. 등장하는 숫자에 대해서 모두 연산을 수행하고, 그 과정에서 조건에 맞지 않으면 탈락시키는 식으로
핵심은 이 문제가 BFS라는 걸 깨닫는것, 그리고 연산중 이미 등장한 조합( num,cnt)이 나왔을때 어떻게 쳐낼것인지.
를 생각하는것이라 생각한다.

# 재귀로 풀었던 흔적
def eternal(num,cnt):
    global min_cnt
    if cnt > min_cnt:
        return
    if num == M:
        min_cnt= cnt
        return
    elif num > M or num > 1000000:
        return

    if num > 0 :
        eternal(num*2,cnt+1)
        eternal(num -10, cnt + 1)
        eternal(num + 1, cnt + 1)
        eternal(num -1, cnt + 1)
    return
"""
from collections import deque
def BFS(n,c):
    que = deque([(n,c)])
    # 중복해서 나오는 값들이 있을수 있으므로, 그 경우를 걸러야한다.
    set_filter = set()

    while que:
        num,cnt = que.popleft()

        if num in set_filter: continue
        # 이런 조합이 다시 나오지 않도록 추가
        # 예전에 이러한 조합이 나왔었나요? --> 나왔으면 스킵하세요.
        # ###  옛날에 이런 질의문을 dict을 형성해서, 구현했던거 같다,
        # if dict.get(num,0):continue
        # dict[num] = 1 이런 식으로..

        # set_filter에 num만 넣어야한다. 나는 옛날에 푼 문제가 기억나서 현재 cnt 까지 넣어줬는데,
        # cnt 값에 따라 결과가 달라지는 그때 그 문제와 다르게, 이번에는 한번의 cnt에서 모든 경우를 다 살피기 때문에,
        # 나중에 동일한 값이 나오는 것은 의미가 없다. 즉, cnt = 1일때 num =8 이였다면, cnt = 2 일때 num = 8 인것은 소용이 없다는 것이다.
        set_filter.add(num)

        if num == M:
            return cnt


        if 1<= num*2 <= 1000000:
            que.append((num*2,cnt+1))
        if 1<= num-10 <= 1000000:
            que.append((num-10,cnt+1))
        if 1<= num+1 <= 1000000:
            que.append((num+1,cnt+1))
        if 1<= num-1 <= 1000000:
            que.append((num-1,cnt+1))


TC = int(input())

for tc in range(1,TC+1):
    N,M = map(int,input().split())
    print('#{} {}'.format(tc,BFS(N,0)))


# 제한시간 초과라... --> set_filter 수정해서 해결.