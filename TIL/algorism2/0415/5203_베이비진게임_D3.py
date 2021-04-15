#5203 베이비진 게임

# 0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 
# 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.
# 게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며,
# 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.

# 두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 
# 승자를 알아내는 프로그램을 작성하시오. 만약 무승부인 경우 0을 출력한다.

# 예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 
# 플레이어 1은 9, 5, 5, 1, 4, 2카드를, 플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.

# 이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.


# 표본이 작아서 그런지 시간, 공간 제약 신경 안쓰고 만드니까 이렇게 편할 수 가 없습니다

import sys
sys.stdin = open('5203_input.txt','r')

# 플레이어의 현재 패가 babygin 인지 확인하는 함수
def babygin(lst:list)->bool:
    run = triplet = False
    arr = [0]*(12)
    for elem in lst:
        arr[elem] += 1
        if arr[elem] >= 3:
            triplet = True
            arr[elem] -= 3
    for idx in range(10):
        if arr[idx] >= 1 and arr[idx+1] >=1 and arr[idx+2] >= 1:
            run = True
    
    if run or triplet:
        return True
    else:
        return False

TC = int(input())

for tc in range(1,TC+1):
    card_lst = list(map(int,input().split()))
    # 플레이어 1 이 받을 모든 카드들
    card_1 = card_lst[::2]
    # 플레이어 2가 받을 모든 카드들
    card_2 = card_lst[1::2]

    ans = 0
    # 매 루프마다 한장씩 추가로 드로우 합니다.
    # 3장 이하에서는 죽었다 깨어도 run/triplet 을 만족할 수 없으니,
    # 기본 3장씩 드로우 한 상태에서 시작합니다.
    # idx는 6까지 가는데, idx는 리스트 슬라이싱에 사용되므로, 카드 리스트의 인덱스 최대 크기보다 1만큼 더 커야지
    # 플레이어 카드 풀 전체를 조사할 수 있습니다.
    for idx in range(3,7):
        player_1 = babygin(card_1[:idx])
        if player_1:
            ans = 1
            break
        player_2 = babygin(card_2[:idx])
        if player_2:
            ans = 2
            break
    print('#{0} {1}'.format(tc,ans))
    