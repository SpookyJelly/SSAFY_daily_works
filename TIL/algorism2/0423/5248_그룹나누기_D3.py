# 5248번 그룹 나누기

"""상호배타 집합을 구하라"""

# 수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출하였다.
# 한 조의 인원에 제한을 두지 않았기 때문에, 한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모두 같은 조가 된다.
# 예를 들어 1번-2번, 1번-3번이 같은 조가 되고 싶다고 하면, 1-2-3번이 같은 조가 된다. 번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성하게 된다.
# 1번부터 N번까지의 출석번호가 있고, M 장의 신청서가 제출되었을 때 전체 몇 개의 조가 만들어지는지 출력하는 프로그램을 만드시오.

import sys
sys.stdin = open('5248_input.txt','r')



# 기본적으로 P는 모든 인원이 아무런 짝지가 안 맺어져있는 상황
# 그렇기에 n == P[n] 가 성립하여 최초의 반환값은 자기 자신이 된다 --> find_set(1) = 1
# 그런데, P[find_set(n2)] = find_set(n1)에서부터 뭔가 달라진다.
# ex) P[2] = 1 이 되어, 2회차 순환때는 find_set에서 n!=P[n]이 성립할수도 있다는 말.
# P[2] =1 이라는 것은 곧, 1과 2가 짝지가 되었다는 뜻.
# 이후 만약에 n1 = 3 n2 = 2가 나온다면, P[3] = 1이 되어 1-2-3이 모조리 짝지가 된다.

def find_set(n):
    while n != P[n]:
        n = P[n]
    return n

TC = int(input())
for tc in range(1,TC+1):
    N,M = map(int,input().split())
    # P는 최초에 모든 인원이 아무런 짝지가 맺어져있지 않은 상태이다.
    # 최초 P = [0,1,2,3,4]
    P = [ i for i in range(N+1)]
    student_lst = list(map(int,input().split()))
    for idx in range(0,len(student_lst),2):
        n1,n2 = student_lst[idx],student_lst[idx+1]
        P[find_set(n2)] = find_set(n1)
    cnt = 0
    for i in range(1,N+1):
        if i==P[i]:
            cnt +=1
    print('#{} {}'.format(tc, cnt))