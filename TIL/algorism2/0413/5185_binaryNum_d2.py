# 16진수 1자리는 2진수 4자리로 표시된다.

# N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.

# 단, 2진수의 앞자리 0도 반드시 출력한다.

# 예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.

# 0100 0111 1111 1110


# [입력]

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

# 다음 줄부터 테스트 케이스의 별로 자리 수 N과 N자리 16진수가 주어진다. 1<=N<=100

# 16진수 A부터 F는 대문자로 표시된다.

# [출력]

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
import sys
sys.stdin = open('5185_input.txt','r')

def chg(d):
    filt = 0b1000
    a=[]
    for i in range(4):
        t = d&filt
        if t== 0:
            a.append('0')
        else:
            a.append('1')
        filt >>=1
    return a



TC = int(input())
for tc in range(1,TC+1):
    N, num = list(input().split())
    ret = []
    for idx in range(len(num)):
        if num[idx].isdecimal():
            ret += chg(int(num[idx]))
        else:
            ret += chg(ord(num[idx])-ord('A')+10 )
    print('#{0}'.format(tc),end=' ')
    print(''.join(ret))
        