# 두개의 탑


"""

1. N개의 블록 주어짐
2. M1층 탑 / M2층 탑 제작 --> M1+M2 = N
3. 쌓는 비용 층수 * 블록 무게
4. 각 탑을 짓는 최소 비용을 계산하여 출력
5. 각 탑의 층도 정해져 있음.

[제한 조건]
1. 1 ≤ N ≤ 50 , 1 ≤ M1 ≤ 50 , 1 ≤ M2 ≤ 50

2. M1 + M2 = N

3. 각 블록의 무게는 1kg 이상 1,000kg 이하이다.


[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫째 줄에는 N, M1, M2가 주어지고, 둘째 줄에는 각 블록의 무게가 주어진다.


[출력]
테스트 케이스 T에 대한 결과는 "#T"를 찍고, 한 칸 띄고, 정답을 출력한다.
(T는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


"""


import sys
sys.stdin =open("problem_input.txt",'r')

TC = int(input())

for tc in range(1,TC+1):
    N,M1,M2 = map(int,input().split())
    blocks = sorted(list(map(int,input().split())))

    if M1>M2:
        low = M2
        high = M1
    else:
        low = M1
        high =M2

    low_tower = [0]
    high_tower = [0]


    F = 1
    while blocks:
        B = blocks.pop()
        if F<low+1:
            low_tower.append(B)
            B = blocks.pop()
        if F<high+1:
            high_tower.append(B)
        F+=1


    result = 0
    for idx in range(len(low_tower)):
        result += idx * low_tower[idx]

    result2= 0
    for idx in range(len(high_tower)):
        result2 += idx * high_tower[idx]

    f_result = result+result2
    print('#{0} {1}'.format(tc,f_result))