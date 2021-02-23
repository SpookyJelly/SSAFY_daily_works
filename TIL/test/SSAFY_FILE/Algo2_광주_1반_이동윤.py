# 문제 2 보드게임

"""
각 10번 굴림, (배열) 20번 도착 승리,

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트
케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 첫번째로 주사위를 굴리는 사람이 누구인지
주어진다.

두번째 줄에는 A의 주사위 숫자가 순서대로 주어진다.
세번째 줄에는 B의 주사위 숫자가 순서대로 주어진다.

[출력]
출력의 각 줄은 ‘#t’로 시작하고, 공백을 한 칸 둔 다음 승자를 출력한다.
단, 무승부인 경우 AB를 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


"""

# 접근 방법:
# 전진 -> 상대방 있는지 확인 -> 목적지 도달 확인 -> 반복
# 위의 행동 양식을 그대로 A와 B에 대해서 옮길 예정

T = int(input())
for tc in range(1, T+1):
    first = input()  # A or B 가 들어간다
    dice_A = list(map(int, input().split()))  # A가 던진 주사위의 눈
    dice_B = list(map(int, input().split()))  # B가 던진 주사위의 눈
    process_A = 0  # A의 진전도
    process_B = 0  # B의 진전도
    # 이번 문제 풀이는 2차원 배열로 접근 할 것이므로, 두 주사위 눈금을 합친 새로운 배열을 만들었다.
    dice = [dice_A, dice_B]

    # 이하의 for문에서 승부가 나지 않을 경우 무승부이므로, 디폴트 값으로 설정한다.
    winner = 'AB'
    # 주사위 굴림의 횟수인 10번 동안 반복한다.
    for i in range(10):
        # 만일 첫번째로 굴리는 사람이 A라면 이하를 시행한다. 기본적인 흐름은 아래와 같다.
        # A가 굴린만큼 전진 -> 그 자리에 B가 있으면 B 초기화 -> B 굴린만큼 전진 -> 그 자리에 A있으면 A초기화
        if first == 'A':
            # process_A는 dice[0](A가 굴린 주사위의 눈의 모음) 의 i번째 요소에 맞게 전진한다.
            process_A += dice[0][i]
            # 전진 했는데, A와 B의 값이 같다면, A가 B를 잡은 것이 되므로 B를 초기화 해주자.
            if process_A == process_B:
                process_B = 0
            # process_B는 dice[1](B가 굴린 주사위의 눈의 모음) 의 i번째 요소에 맞게 전진한다
            process_B += dice[1][i]
            # 전진 했는데, A와 B의 값이 같다면, B가 A를 잡은 것이 되므로 A를 초기화 해주자.
            if process_B == process_A:
                process_A = 0

            # 만약에 A가 20 칸 이상으로 진전했다면, winner를 A로 설정해준다.
            if process_A >= 20:
                winner = 'A'
                # 더 이상 loop 돌릴 이유가 없으니 break
                break
            if process_B >= 20:
                winner = 'B'
                break
        # 첫번째로 굴리는 사람이 B이면 이하를 시행한다. 골자는 동일하나, 시행 순서만 바뀌었다.
        # B가 굴린만큼 전진 -> 그 자리에 A가 있으면 A 초기화 -> A 굴린만큼 전진 -> 그 자리에 B있으면 B초기화
        else:
            process_B += dice[1][i]
            if process_A == process_B:
                process_A = 0
            process_A += dice[0][i]
            if process_B == process_A:
                process_B = 0
            if process_A >= 20:
                winner = 'A'
                break
            if process_B >= 20:
                winner = 'B'
                break
    # 형식에 맞게 출력해준다.
    print('#{0} {1}'.format(tc, winner))
