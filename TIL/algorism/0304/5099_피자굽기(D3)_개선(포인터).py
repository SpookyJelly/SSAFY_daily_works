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


# 함수의 기본 아이디어 -> pop(0)와 append()를 쓰는 것은 시간이 너무 오래 걸릴 거 같으므로,
# 피자 배출구가 움직이도록 한다.

### 제약 조건 :pop()과 append()를 일절 쓰지 않는다!

def emberfire_oven(pizza: list, oven_size: int, pizza_num):
    oven = [pizza[idx] for idx in range(oven_size)]
    pizza = pizza[oven_size:]  # 큐로 사용
    pointer = 0  # 피자 배출구의 현 위치
    counter = 0  # 치즈가 다 녹은 피자의 갯수

    # 종료조건 : counter가 전체 피자 갯수와 동일해지면 while문 내부의 return에 의해서 종료됨.
    while True:

        oven[pointer]['cheeze'] = oven[pointer]['cheeze'] // 2

        # 진짜 피자 (number가 0이 아닌 피자)의 치즈가 다 녹았을때,
        if oven[pointer]['cheeze'] == 0 and oven[pointer]['number'] != 0:
            counter += 1

            # 먼저 마지막 피자인지를 확인해준다.
            if counter == pizza_num:
                return oven[pointer]

            # 마지막 피자가 아닌 경우, oven[pointer]를 교체해준다. 근데 경우가 2가지다. 큐가 남은 경우, 안 남은 경우.
            else:

                # 피자 큐에 피자가 남은 경우
                if pizza:
                    oven[pointer] = pizza[0]
                    # 어떻게든 pop 안쓰려고 슬라이싱을 이용했다.
                    pizza = pizza[1:]

                else:  # 피자큐에 피자가 안남은 경우
                    oven[pointer] = {'cheeze': 0, 'number': 0}  # 가짜 피자를 넣어준다


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
