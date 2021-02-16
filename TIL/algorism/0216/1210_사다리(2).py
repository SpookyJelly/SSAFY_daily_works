# 1210번 사다리 문제

# 보아하니 포인터를 이용한 것 같다.
# 마지막 행에서 2가 등장한 xp yp를 가지고 chkline이라는 함수를 돌렸다
def chkLine(xp):
    # yp --> 행인듯, 이게 점차 감소되는 모습을 보일것 같다
    yp = 99
    # 방향 지시등
    d = 0
    # yp가 0보다 클때 순환 --> yp == 0 일때 멈춘다
    while yp > 0:
        # 포인터가 d == 1 or 0 이고 열 왼쪽 인덱스가 범위를(0~99) 벗어나지 않으며, 그 왼쪽 인덱스의 밸류가 1이면
        if (d == 0 or d == 1) and xp - 1 > 0 and data[yp][xp - 1]:
            # 왼쪽 열로 이동한다.
            xp -= 1
            # 포인터는 1이 된다. 이로서 계속해서 멈춤 조건 만나기 전까지는 왼쪽으로 이동
            d = 1
        # if문과 상동하다. 다만 여기는 오른쪽으로 이동할 뿐
        elif (d == 0 or d == 2) and xp + 1 < 100 and data[yp][xp + 1]:
            xp += 1
            d = 2

        # 포인터와 관계없이 열 왼쪽/ 오른쪽 인덱스가 범위(0~99)를 벗어나지 않는데, 왼쪽,오른쪽 인덱스의 밸류가 0이다.
        # 그럼 위로 한 칸 이동한다.
        else:
            yp -= 1
            d = 0
    # 열 위치 인덱스를 반환한다.
    return xp


T = 10

for t in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    for i in range(len(data)):
        if data[99][i] == 2:
            result = chkLine(i)
    print('#{} {}'.format(t, result))