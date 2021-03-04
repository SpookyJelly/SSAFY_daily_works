# 5099번 피자굽기 (D3)

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


# 일단, 내가 원하는 자료형으로 만드는것부터 시작하자
# 나는 사전형 자료를 사용할 것인데, 치즈의 양과 피자의 번호를 동시에 가지고 있도록 할 것이다.


# 함수의 기본 아이디어 -> pop(0)와 append()를 쓰는 것은 시간이 너무 오래 걸릴 거 같으므로,
# 피자 배출구가 움직이도록 한다.
def emberfire_oven(pizza: list, oven_size: int, pizza_num):
    oven = [pizza[idx] for idx in range(oven_size)]
    pizza = pizza[oven_size:]  # 큐로 사용
    pointer = 0
    counter = 0 # 피자 배출구의 현 위치
    # a를 찾을 때까지 반복한다.
    while True:
        # 일단 치즈를 녹이고 시작한다.
        oven[pointer]['cheeze'] = oven[pointer]['cheeze'] // 2

        if oven[pointer]['cheeze'] == 0: # and oven[pointer]['number'] != 0
            # 피자가 오븐에서 나갈때마다 체크한다.
            a = oven.pop(pointer) # oven[pointer] = pizza[0] <-- pizza가 남았는지 안남았는지 구분... # 오븐 칸을 어떻게 비울지랑, 비운경우를 구분하는걸 추가로 고려..
            counter += 1
            # 오븐 밖으로 튀어나간 피자가 전체 피자 갯수와 같으면, a는 마지막에 튀어나간 피자가 된다.
            if counter == pizza_num:
                return a
            # 피자가 남아있으면, 해당 큐에서 튀어나간 피자의 위치에 다시 남은 피자를 넘어준다.


            if len(pizza) >= 1:
                oven.insert(pointer, pizza[0])
                pizza.pop(0)
            # 아니면, 가짜 피자를 넘어준다. 가짜 피자는 치즈가 20인데, 이는 제약 조건에 등장한 최대 치즈의 양이다.
            # 따라서, 오리지날 피자들보다 먼저 튀어나가는 일은 없다.
            # 왜 굳이 가짜 피자를 넣어주냐고?? 지금 이 함수는 고정된 오븐의 크기를 기준으로 하여 포인터가 움직이는데,
            # 오븐의 크기가 변경되면 전체 시퀀스가 오작동하기 때문
            else:
                oven.insert(pointer, {'cheeze': 20, 'number': 'null'})
        # pointer는 0~oven_size -1 을 반복한다
        pointer = (pointer + 1) % oven_size


TC = int(input())

for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    cheeze = list(map(int, input().split()))
    pizza = []

    for i in range(M):
        pizza_i = {
            'cheeze': cheeze[i],
            'number': i + 1,
        }
        pizza.append(pizza_i)

    ans = emberfire_oven(pizza, N, M)
    print('#{0}'.format(tc), end=' ')
    print(ans['number'])

# 포인터랑 큐를 반반씩 사용한 미묘한 코드.