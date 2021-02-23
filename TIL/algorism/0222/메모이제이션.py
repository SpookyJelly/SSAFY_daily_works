# 메모이제이션 : 재귀 함수 등에서 이미 구해진 값을 여러번 구하는 경우에는 메모리 문제등이있음
# 이를 막기 위해서, 사전에 미리 어떠한 값을 할당하는 것이다.
# 동적 프로그래밍의 기반이 된다.

def fibo1(n):
    if n >= 2 and len(memo) <= n : #len(memo) <=n의 의미 : 이미 구해진 상태이다.
        memo.append(fibo1(n-1)+fibo1(n-2)) # 자꾸자꾸 새로운 값을 더해준다.
    return memo[n]

memo = [0,1]

print(fibo1(40))


"""
n에 따른 fibo1의 결과
n = 0
-> if문 만족 안함. 바로 memo[0] 리턴 -> memo[0] == 0
n = 1
-> if 문 만족 안함. 바로 memo[1] 리턴 -> memo[1] == 1

n = 2
-> if문 만족 이제 memo에 fibo1(0)+ fibo1(1)을 더해준다.
-> memo = [0,1,1]이 된다.

"""

###########리스트의 길이를 이용해서 풀이하는 방법##############
memo2 = [-1]*21
memo2[0] = 0
memo2[1] = 1

def fibo2(n):
    if memo2[n] == -1:
        memo2[n] = fibo2(n-1) + fibo2(n-2)
    return memo2[n]

print(fibo2(10))
print(memo2)




#####실제 손으로 연습해보면서 접근해보자.