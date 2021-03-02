# Forth

"""

Forth라는 컴퓨터 언어는
스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.


3 4 + .


Forth에서는 동작은 다음과 같다.


숫자는 스택에 넣는다.
연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
‘.’은 스택에서 숫자를 꺼내 출력한다.



Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오.
만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다.
피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.
나눗셈의 경우 항상 나누어 떨어진다.

"""
# 사용되는 연산자 + - / * .

import sys
sys.stdin = open('4874_input.txt','r')

TC = int(input())

for tc in range(1,TC+1):
    stack = []
    string = input().split() # 굳이 리스트 안붙여줘도, 공백단위로 나누면서 list로 형변환한다.
    for elem in string:
        if elem.isdigit():
            stack.append(int(elem))
        else:
            if elem =='.':
                ans = stack.pop()
                # 정상적이라면, .를 조우했을때, 스택에는 정답 인수 하나 밖에 없을 것이다.
                # 그 case를 len 함수를 이용해서 파악했다.
                if len(stack) == 0:
                    print('#{0} {1}'.format(tc,ans))
                    break
                else:
                    print('#{0} error'.format(tc))
                    break
            else:
                if len(stack)>=2:
                    # 순서에 주의하라. 처음에는 a를 먼저 pop한 변수로 넣었는데, 더하기 곱하기는 문제가 없지만
                    # 빼기, 나눗셈 할 때는 의도한 바와 다른 값이 나온다. 먼저 뽑은 친구가 b라는 사실에 주의해라
                    b = stack.pop()
                    a = stack.pop()
                    if elem == '+':
                        stack.append(a+b)
                        continue
                    if elem == '-':
                        stack.append(a-b)
                        continue
                    if elem == '*':
                        stack.append(a*b)
                        continue
                    if elem == '/':
                        stack.append(a//b)
                        continue
                else:
                    print('#{0} error'.format(tc))
                    break
# 코드가 쓸데없이 복잡해보인다.. 이거 더 줄일 수 있는 방법은 없을까?


