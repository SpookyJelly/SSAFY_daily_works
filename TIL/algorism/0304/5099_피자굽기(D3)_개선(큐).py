# 5099번 피자굽기 (D3) (큐)

"""

N개의 피자를 동시에 구울 수 있는 화덕이 있다. 피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다.

1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때, 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.

주어진 조건에 따라 피자를 구울 때, 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.

- 피자는 1번위치에서 넣거나 뺄 수 있다.
- 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
- M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
- 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 첫 줄에 화덕의 크기 N과 피자 개수 M이 주어지고, 다음 줄에 M개의 피자에 뿌려진 치즈의 양을 나타내는 Ci가 주어진다.

3<=N<=20, N<=M<=100, 1<=Ci<=20

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.

"""
import sys

sys.stdin = open('5099_input.txt', 'r')


# 문제에서 시키는대로, pop과 append를 활용한 큐를 이용하여 해결하자.
# 이번에는 자료형을 딕셔너리가 아닌, 리스트로 형성하자.

def emberfire_oven(pizza: list, oven_size: int, pizza_num):
    # pizza[0] <- 피자 번호
    # pizza[1] <- 치즈량
    oven = []
    for _ in range(oven_size):
        oven.append(pizza[0])
        pizza.pop(0)

    # 오븐에 마지막 피자가 남을때까지 반복한다.
    while len(oven) > 1:
        # 일단 치즈 한 번 녹이고 (제일 앞에서)
        oven[0][1] = oven[0][1] // 2
        # 치즈가 완전 녹았으면,
        # oven에서 제거한다.
        if oven[0][1] == 0:
            oven.pop(0)
            # 피자 큐에 피자가 남아있으면,
            # 완전 녹은 치즈피자 자리에 더해준다.
            # 이후, 피자 큐에서 맨 앞에서 제거
            if pizza:
                oven = [pizza[0]] + oven
                pizza.pop(0)

            # pizza 큐에 피자가 없는 경우는 고려할 필요가 없는것이,
            # 어짜피 문제의 목적은 마지막까지 살아있는 피자를 구하는 것이기에, 오븐내에 피자가 몇개가 있는건 관계가 없다.


        # 치즈가 덜 녹았으면,
        # oven 맨 뒤로 넣어버린 다음, 맨 앞에서 빼버린다.
        else:
            oven.append(oven[0])
            oven.pop(0)

    return oven


TC = int(input())

for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    cheeze = list(map(int, input().split()))

    pizza = []
    for num, chee in enumerate(cheeze):
        pizza.append([num + 1, chee])

    ans = emberfire_oven(pizza, N, M)
    print('#{0}'.format(tc),end=' ')
    print(ans[0][0])
