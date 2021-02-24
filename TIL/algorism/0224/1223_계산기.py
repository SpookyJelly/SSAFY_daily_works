# 1223번 계산기2 (D4)

"""

문자열로 이러우진 계산식이 주어질 때, 이 계산식을
후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며
피연산자인 숫자는 0 ~ 9의 정수만 주어진다. (다행;)

입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다
"""

import sys
sys.stdin = open("1223_input.txt",'r')

TC = 10

for tc in range(1,TC+1):
    N = int(input()) # 들어오는 문자열의 길이
    #N = 7
    case = list(input()) # 입력되는 문자열들을 리스트로 저장. 문자열 말고 리스트로 하는 이유? 음 글쎄
    #case = ['3', '+', '2', '*', '3', '+', '1']
    stack = [] # 스택으로 활용될 빈 리스트 , 다행이다...여기 비우니까 오류나길래 뭐지 싶었는데. 잘되었다.
    new= [] # 새로 이동 될 리스트
    idx = 0
    while idx<N: # 3가지 케이스로 나누자
        # 전체 리스트만 순회하면 되니까... 이 조건이면 멈추겠지? 일단 확인부터 해보자
        if case[idx] == '+':  # case의 입력값이 + 인 경우
            for _ in range(len(stack)):
                if stack[-1] == '+' or stack[-1] == '*': # 근데 스택의 최상단 값이 자기랑 동일한 우선순위야.
                    new.append(stack.pop()) # 그럼 스택 맨 위에 있는게 pop 되서 new로 들어간다
            stack.append(case[idx]) # 그리고 자기 자신이 들어간다. 근데 이 과정이 여러번 될 수도? 그래서 for문 사용



        elif case[idx] == '*': # case의 입력값이 * 인 경우
            for _ in range(len(stack)):
                if stack[-1] == '*': # 최상단값이 자신과 동일한 우선 순위인 경우
                    new.append(stack.pop())
            stack.append(case[idx])


        else: # case의 입력값이 숫자인 경우
            new.append(int(case[idx])) # 정수는 stack을 거칠 필요 없이 바로 new로

        idx += 1
    #print('new:',new)
    #print('stack:',stack)
    # 위 과정을 끝나면 스택에 단 하나의 요소만 남는다. 그걸 pop시켜줘서 new를 완전히 후열 뭐시기로 만든다.
    for __ in range(len(stack)): # 스택에 달랑 하나만 남는줄 알았는데, 만약에 끝에 연산자가 무더기로 오는 경우, 하나가 아닐 수 있다.
        new.append(stack.pop()) # 그렇기 때문에 쭉 다 비워주자
    #print('new:',new)
    #print('stack:',stack) # 스택은 다시 비어져있는 상태

    idx = 0
    while idx<N: # 여기서부터는 계산하는 부분
        if type(new[idx]) == type(1): # 만약에 new[idx]가 정수라면...
            stack.append(new[idx])
        else: # 만약에 new[idx]가 정수가 아니라면 --> 연산자라면
            a = stack.pop()
            b = stack.pop()
            if new[idx] == '+':
                c = a+b
                stack.append(c)
            else: # 연산자 중에서 * 겠지
                c = a*b
                stack.append(c)
        #print('stack : ',stack)
        #print('idx :',idx)
        idx+=1

    print('#{0} {1}'.format(tc,stack.pop()))
