#4866번 괄호검사 (D2)

"""
주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다.
입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
"""
# 접근법 : 스택의 LIFO를 이용하면 될 것 같다.
# ( { [ 가 입력될 때마다, 스택에 집어 넣고, ) } ] 이 입력될때마다 스택에서 pop 시킨다.
# pop할 때의 주의점은, 현재 값 (a)가 pop된 값(b)와 쌍일치하는지 확인해야한다. --> 딕셔너리 어때?
# 맞으면 그대로 진행, 아니면 바로 틀렸다고 한다.

TC = int(input())
#TC = 1
prhs_dic ={
    '(' : ')',
    '{' : '}',
    '[' : ']',
}

for tc in range(1,TC+1):
    string = input()
    stack = [] # 여기에는 여는 값만 모인다
    result = 1 # 기본 정답은 1이다.
    for idx in range(len(string)):
        if string[idx] == '(' or string[idx] == '{' or string[idx] == '[':
            stack.append(string[idx])
        elif string[idx] == ')' or string[idx] == '}' or string[idx] == ']': # else쓰면 안되는게, 괄호 빼고 다른 문자열도 들어올 수도 있기 때문에,
            if len(stack) >= 1: # 뽑으라는 지시가 나오면, stack이 남아있는지를 확인한다.
                b = stack[-1]
                if prhs_dic[b] != string[idx]: # 쌍일치 하지 않으면 바로 0으로
                    result = 0
                    break
                else:
                    stack.pop(-1) # 쌍일치하면 pop 시켜준다.
            else: # 뽑으라는 지시가 나왔는데, 스택의 길이가 없어서 뽑지 못하면 오답이다.
                result = 0
                break
    if len(stack) > 0: # 다 돌았는데, 아직 끝맺음 짓지못한 괄호가 있을수도 있다. 그럼 오답이다
        result = 0
    print(f'#{tc} {result}')
    print(f'제 스택은 : {stack}')