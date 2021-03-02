# 1224번 계산기 3

"""

문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+(4+5)*6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"345+6*+7+"

변환된 식을 계산하면 64를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 문자열 중간에 괄호가 들어갈 수 있다.

이 때 괄호의 유효성 여부는 항상 옳은 경우만 주어진다.

피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.


"""
import sys

sys.stdin = open('1224_input.txt', 'r')

# 필요한거 1. 후위표기식으로 만드는 함수 2. 후위 표기식 계산하는 함수

# 후위 표기식으로 만드는 함수에 필요한것.
"""
1.빈 스택
2. 딕셔너리 2개  --> 연산자 우선순위 표기용 --> 스택 내부에서 사용하는것, 스택 외부에서 사용하는것 2개 필요

"""


def Gorehowl(str: list) -> list:
    stack = []
    result = []
    # string에서의 우선도
    out_dic = {
        '+': 1,
        '*': 2,
        '(': 3,

    }
    in_dic = {
        '+': 1,
        '*': 2,
        '(': 0
    }

    for word in str:
        if word.isdigit():
            result.append(word)
        elif word == ')':
            # ')'가 등장하면, '('나올때까지 스택에서 팝시켜준다
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # 그리고 마무리로 '('도 스택에서 없애준다.
        else:  # 연산자 비교하고 append 해야하는데...최초에 넣어줄때 어떻게 넣는담 ')' 처리는 어떻게?
            while len(stack) > 0 and out_dic[word] <= in_dic[stack[-1]]:  # 스택 길이가 0보다 크면서,
                # 밖에 있는 연산자의 우선순위가 스택 제일 위의 우선도보다 낮다면 (찍어누를수 없다면)
                # 스택 맨위를 팝 시켜준 다음, result에 넣는다
                result.append(stack.pop())
            # 여기는 찍어누를수 있을때 눌러주는곳
            stack.append(word)
    # 스택에 남은 찌꺼기들 합해주기
    while stack:
        result.append(stack.pop())

    return result


# 후위 표기식 계산하는 함수
# 기본적으로 다 스택에 집어넣은 다음, 연산자가 나오면 2개 뽑아서 계산 --> 괄호 종범해서 그냥 만들면 된다
def Sulfuras(str: list) -> int:
    stack = []

    for elem in str:
        if elem.isdigit():
            stack.append(int(elem))
        else:  # 부호가 2개뿐이라 크게 고려할게 없다
            b = stack.pop()
            a = stack.pop()
            if elem == '+':
                stack.append(int(a + b))
            else:  # elem == '*'
                stack.append(int(a * b))
    return stack


TC = 10
for tc in range(1, TC + 1):
    N = int(input())
    string = list(input())
    ans = Gorehowl(string)
    print('#{0} {1}'.format(tc, Sulfuras(ans)[0]))
