#7465번 창용마을 무리의 개수

# 창용 마을에는 N명의 사람이 살고 있다.
# 사람은 편의상 1번부터 N번 사람까지 번호가 붙어져 있다고 가정한다.
# 두 사람은 서로를 알고 있는 관계일 수 있고, 아닐 수 있다.
# 두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면,
# 이러한 사람들을 모두 다 묶어서 하나의 무리라고 한다.
# 창용 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하라.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 각각 창용 마을에 사는 사람의 수와 서로를 알고 있는 사람의 관계 수를 나타내는
# 두 정수 N, M(1 ≤ N ≤ 100, 0 ≤ M ≤ N(N-1)/2) 이 공백 하나로 구분되어 주어진다.
# 이후 M개의 줄에 걸쳐서 서로를 알고 있는 두 사람의 번호가 주어진다. 같은 관계는 반복해서 주어지지 않는다.

"""

# 상호배타적 집합으로 무리를 구하면 된다
# union 연산과 find 연산을 이용하자.

"""
import sys
sys.stdin = open('7465_input.txt','r')

def union(i:int)->int:
    # 자기자신의 값이 자신의 인덱스와 다르면, 그 요소 값을 가져온다. --> while문 때문에 계속 반복한다
    # i == Persona[i]가 될 때까지.. 즉, 인덱스 == 요소값인 대표자를 반환하는 것이다
    while i != Persona[i]:
        i = Persona[i]
    return i

TC = int(input())

for tc in range(1,TC+1):
    N,M = map(int,input().split())
    # 대표자가 같으면 같은 집합이다 --> 같은 요소값을 가지는 것으로 같은 집합임을 표시
    Persona = [i for i in range(N+1)]

    for _ in range(M):
        p1,p2 = map(int,input().split())
        Persona[union(p2)] = union(p1)

    for i in range(len(Persona)):
        Persona[i] = union(i) # union(i)는  자기가 속해있는 집합의 번호가 나온다.
        # 이 for문은 그 집합 번호가 달라졌다면, 다시 갱신해주는 역할을 한다
    set_P = set(Persona[1:])
    print('#{} {}'.format(tc,len(set_P)))