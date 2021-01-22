'''
리스트의 총곱

사용자가 입력한 정수 num을 기준으로, 1~num으로 이루어진 리스트의 총 곱을 반환하는 함수를

1. `for`문을 사용하여 작성하시오.
2. `while`문을 사용하여 작성하시오. 

---
[입력 예시]
4

[출력 예시]
24
'''

# for문만 사용하여 풀기
def mul_with_for(numbers):
    result = 1
    for num in range(1,numbers+1):
        result *= num
    return result



# while문만 사용하여 풀기
def mul_with_while(numbers):
    result = 1
    while (numbers>0):
        result *= numbers
        numbers -=1
    return result
    


# 아래 코드는 바꾸지 않습니다.
if __name__ == '__main__':
    print(mul_with_for(4))   # 24
    print(mul_with_while(5)) # 120