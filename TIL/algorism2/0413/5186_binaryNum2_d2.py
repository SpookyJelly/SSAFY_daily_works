# 5186번
# 0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다. 예를 들어 0.625를 이진 수로 바꾸면 0.101이 된다.
# N = 0.625
# 0.101 (이진수)
# = 1*2-1 + 0*2-2 + 1*2-3
# = 0.5 + 0 + 0.125
# = 0.625
# N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고, 13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.

# [입력]

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

# 다음 줄부터 테스트 케이스의 별로 소수점 아래가 12자리 이내인 N이 주어진다.


# [출력]

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys
sys.stdin = open('5186_input.txt','r')

# 기본 아이디어 : N에 곱하기 2해서 정수부분만 따로 빼낸다. 12번 반복한다.


TC = int(input())

for tc in range(1,TC+1):
    N = float(input())
    result = ''
    # 13번 부터는 overflow를 출력해야하니까, 일부러 13번 돌려서, len(result)가 13이면 overflow를 출력하게 하려고 함
    for _ in range(13):
        # N == 0 이면 중도탈출
        if N == 0:
            break
        N *=2
        result += str(int(N))
        N -= int(N)
    if len(result)>12:
        result = 'overflow'
    
    print('#{0} {1}'.format(tc,result))


"""
다른 풀이 방법 
(2를 곱하는 방식이 아니라, 필터를 1/2 배 하는 식으로 계산)

a = 0.5 // 0.5 == 2^-1 이기 때문에
value = int(input())
cnt = 0
result = ''
while val > 0 and cnt < 13:
    if val >= a:
        result += '1'
        val -= a
    else:
        result += '0'
    a *= 0.5
    cnt += 1
if cnt == 13:
    print('overflow')
else:
    print(result)


"""
