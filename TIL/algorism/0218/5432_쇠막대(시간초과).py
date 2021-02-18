# 5432. 쇠막대기 자르기 (D4)

"""

쇠막대기와 레이저의 배치는 다음 조건을 만족한다.

 - 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.

 - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.

 - 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.

 - 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

1. 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 “()” 으로 표현된다.
 또한, 모든 “()”는 반드시 레이저를 표현한다.

2. 쇠막대기의 왼쪽 끝은 여는 괄호 ‘(’ 로, 오른쪽 끝은 닫힌 괄호 ‘)’ 로 표현된다.

"""
import sys
sys.stdin = open("5432_input.txt",'r')


TC = int(input())
#TC = 1
for tc in range(1,TC+1):

    #T = '()(((()())(())()))(())'
    T = input()
    icon_bar = T.replace('()','T')


    #icon_bar = '((T))'
    print(icon_bar)


    a = 0
    b = 0
    i=0
    cnt = 0
    cut = 0
    N = len(icon_bar)
    for idx in range(N):

        if icon_bar[idx] == '(':
           i = 0
           a = 0
           b = 0
           #i로 움직이는 while문이다.
           while i+idx <N: # 탈출 조건이 있어야한다. True로 해도 관계 없나
                if icon_bar[idx+i] == '(':
                    a += 1
                elif icon_bar[idx+i] == ')':
                    b += 1
                else:
                    cnt += 1

                i+=1

                if a == b:

                    if cnt !=0 :
                        cut += cnt+1
                        print(cut)
                    cnt = 0
                    break
    print(f'#{tc} {cut}')

# 아니 시발 왜 제한 시간 초과
# 함수로 돌려야하나?