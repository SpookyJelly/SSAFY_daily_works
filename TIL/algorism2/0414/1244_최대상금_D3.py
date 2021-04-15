# 1244번 최대상금
# 정해진 횟수만큼 교환이 끝나면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산된다.

# 숫자판의 오른쪽 끝에서부터 1원이고 왼쪽으로 한자리씩 갈수록 10의 배수만큼 커진다.

# 위의 예에서와 같이 최종적으로 숫자판들이 8,8,8,3,2의 순서가 되면 88832원의 보너스 상금을 획득한다.

# 여기서 주의할 것은 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.
# 94의 경우 2회 교환하게 되면 원래의 94가 된다.

# 정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액을 계산해보자.

# [입력]

# 가장 첫 줄은 전체 테스트 케이스의 수이다.

# 최대 20개의 테스트 케이스가 표준 입력을 통하여 주어진다.

# 각 테스트 케이스에는 숫자판의 정보와 교환 횟수가 주어진다.

# 숫자판의 정보는 정수형 숫자로 주어지고 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번이다.

# [출력]

# 각 테스트 케이스마다, 첫 줄에는 “#C”를 출력해야 하는데 C는 케이스 번호이다.

# 같은 줄에 빈 칸을 하나 사이에 두고 교환 후 받을 수 있는 가장 큰 금액을 출력한다.

import sys
sys.stdin = open('1244_input.txt','r')

# 그냥 브루트포스로 가야하나?
# 아니? 투포인터 써보자
def two_pointer(numbers,swap):
    start = 0
    cnt = 0
    end = len(numbers)-1
    while cnt < swap:
        while start < end:
            if numbers[start] < numbers[end]:
                numbers[start],numbers[end] = numbers[end] , numbers[start]
                cnt += 1
                start += 1
                if cnt == swap:
                    break
            else: # numbers[start] >= numbers[end]
                start += 1
        if end == len(numbers)//2:
            answer = timekilling(numbers,cnt,swap)
            return answer
        else:
            end -=1
            start = 0

    return numbers


def timekilling(numbers,cnt,swap):
    while cnt < swap:
        numbers[-1],numbers[-2] = numbers[-2],numbers[-1]
        cnt +=1
    return numbers


TC = int(input())

for tc in range(1,TC+1):
    numbers, swap = input().split()
    numbers = list(numbers)
    swap = int(swap)
    print(two_pointer(numbers,swap))
    