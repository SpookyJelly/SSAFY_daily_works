# 연습문제 1번
"""
수식 문자열을 읽어서 피연산자는 바로 출력하고
연산자는 스택에 push 하여 수식이 끝나면 스택의
남아있는 연산자를 모두 pop 하여 출력하시오.
연산자는 4칙 연산만 사용하시오.

예를 들어 2+3*4/5 인 수식인 경우
- 2 3 4 5 / * + 가 출력


"""

susick = '2+3*4/5'
stack=list()

inside_stack =

for idx in range(len(susick)):
