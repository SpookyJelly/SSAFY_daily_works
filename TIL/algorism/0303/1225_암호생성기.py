# 1225_암호생성기(D3)

"""

다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.

- 8개의 숫자를 입력 받는다.

- 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.

다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로,
그 다음 수는 4, 그 다음 수는 5를 감소한다.

이와 같은 작업을 한 사이클이라 한다.

- 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다.
이 때의 8자리의 숫자 값이 암호가 된다.

[제약 사항]

주어지는 각 수는 integer 범위를 넘지 않는다.
마지막 암호 배열은 모두 한 자리 수로 구성되어 있다.

[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고, 그 다음 줄에는 8개의 데이터가 주어진다.

[출력]

#부호와 함께 테스트케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.

"""

import sys

sys.stdin = open('1225_input.txt', 'r')

# 1,2,3,4,5 감소 시키는 것이 한 사이클이므로, 인덱스를 이용해서 그 감소값들을 꺼내줄 것이다
counter = [1, 2, 3, 4, 5]

# ***문제 조건 보충 필요*** Test Case는 10개이다. 나는 이 사실을 몰라서
# while input():으로 입력값이 들어오면 계속 반복하게 하려고 했는데, 그마저도 input.txt의 마지막 행이 enter가 아니라서 자동으로 끝나지 않아 난감했었다.
# 문제에 명확한 조건이 명시되어야할 필요가 있다.
i = 0
while i < 10:
    i += 1
    TC = int(input())
    int_lst = list(map(int, input().split()))
    cnt = 0  # 이 변수는 while문 내부에서 변화하면서 counter의 값을 가져올 것이다.

    while True:  # 루프 횟수가 명확하지 않으므로, while문 사용
        first = int_lst.pop(0)

        # pop 시킨 요소가 0 이하이면 0으로 바꾸고 리스트를 반환
        if first - counter[cnt] <= 0:
            first = 0
            int_lst.append(first)
            break

        # 사실상 else 구문과 동일하다. pop 시킨 친구를 counter[cnt]만큼 빼준 다음 append 해준다
        int_lst.append(first - counter[cnt])

        # cnt는 counter의 인덱스로 사용하여, while문의 루프 횟수와 관계없이 항상 first에서 1,2,3,4,5 만을 뺄셈하도록 한다.
        # 그를 위해서 나머지 연산자를 이용해 0,1,2,3,4를 반복하게 했다.
        cnt = (cnt + 1) % 5

    int_lst = list(map(str, int_lst))
    print('#{0} {1}'.format(TC, ' '.join(int_lst)))


# counter 대신에 for문을 활용할 수도 있구나!
"""
def password():
    while True:
        for i in range(1,6):
            q = queue.pop(0)
            q -= i
            if q<= 0 :
                q=0
            queue.append(q)
            if queue[-1] == 0:
                return


"""