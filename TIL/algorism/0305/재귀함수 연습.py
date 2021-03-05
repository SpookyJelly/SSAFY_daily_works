# 재귀함수 연습 문제 1

"""
어떤 수(number)의 각 자리 숫자(digit)의 합을 계산하는 sumOfDigits()라는 재귀 함수를 작성하자.
입력한 수를 읽어 sumOfDigits() 함수를 호출하며,
이 함수는 합산할 숫자가 남지 않을 때까지 자신을 호출해, 최종적인 합을 사용자에게 표시한다.

입력 : 47253

출력 : 21

입력 : 543

출력 : 13


"""


def sumOfDigits(num):

    a = num % 10
    num = num //10
    if 0<=num<10:
        return num + a


    return sumOfDigits(num) + a


print(sumOfDigits(6452))
print(sumOfDigits(47253))
print(sumOfDigits(643))



# 재귀함수 연습문제 2
# 복리 이자의 재귀적 계산
"""
복리 횟수가 1이라고 가정하면 공식을 다음과 같이 간단히 나타낼 수 있습니다.

P′=P(1+r)t
P : 원금
P′ : 원리금
r : 이율
t : 기간

그런데 이번 문제는 위 공식을 그대로 사용하지 말고 재귀적으로 풀어야 합니다. 결괏값의 소수점 이하는 그대로 두시면 됩니다.

연이율 5.8%인 연복리 상품에 360만원을 2년간 예치했을 때 만기 수령액:

>>> compound_interest_amount_withoutN(3600000, 0.058, 2)
4029710.4000000004

천만원을 연이율 5% 월복리 예금에 1년 넣었을 때 만기 수령액:

>>> compound_interest_amount_withoutN(10000000, 0.05 / 12, 12)
10511618.978817329
"""

def bokri(P,r,t):
    if t == 1:
        return P*(1+r)

    return bokri(P,r,t-1) *(1+r)


print(bokri(3600000,0.058,2))
print(bokri(10000000,0.05/12,12))


# 재귀함수 연습문제 3
# 위 문제를 풀었다면 아래 공식으로도 풀어보세요.
#
# P′=P(1+r/n)n^t
# P : 원금
# P′ : 원리금
# r : 이율
# n : 복리 횟수
# t : 기간
#
# 이 문제를 풀 수 있다면 엄청 잘 하시는 것으로 인정! 아, 재귀적으로 풀었을 때만요.

"""
>>> compound_interest_amount(1500000, 0.043, 6, 4)
1938836.8221341053

>>> compound_interest_amount(1500000, 0.043, 6, 1/2)
1921236.0840000005

함수를 만들었다면 마지막 인자로 1을 전달해서 1번 문제도 풀 수 있어요.

>>> compound_interest_amount(3600000, 0.058, 2, 1)
4029710.4000000004

"""

def bokri2(P,r,t,n):
    if t * n == 1:
        return P *(1+r/n)
    elif t*n >1:
        return bokri2(P,r,t-1/n,n) * (1+r/n)


print(bokri2(1500000,0.043,6,4))