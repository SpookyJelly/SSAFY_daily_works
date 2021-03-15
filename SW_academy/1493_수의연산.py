# 1493 수의 연산

# 설명 생략
import sys
sys.stdin = open('1493_input.txt','r')

def find_coordinate(s: int) -> list:
    # n == y축 높이
    n = 0
    ignite = 0
    while s > ignite:
        ignite = int(1 + ((n - 1) * n) / 2)
        n += 1
    # while문 탈출했을때 -> s <= ignite
    if ignite == s:
        x_init = 1
        y_init = n
        return [x_init, y_init]
    else:  # s<ignite
        sn = (n - 1) - 1  # while 나오면서 한번 더 더해지니까 한번 더 빼주자
        ignite_sn = int(1 + ((sn - 1) * sn) / 2)
        x_init = 1
        y_init = sn
        while ignite_sn != s:
            ignite_sn += 1
            x_init += 1
            y_init -= 1
        return [x_init, y_init]  # TODO:[x_init, y_init]로 바꿔


# 좌표계를 받아서 정수로 반환
def find_Snumber(coor) -> int:
    x_pos = coor[0]
    y_pos = coor[1]
    d = x_pos
    cnt = 0
    starting_point = int(x_pos + (x_pos * (x_pos - 1)) / 2)
    # 설계의도 sp는 d만큼 증가, d는 매 루프마다 1씩 증가, 루프는 y_pos-1만큼만 반복
    while cnt < y_pos - 1:
        starting_point += d
        cnt += 1
        d += cnt
    return starting_point


TC = int(input())
for tc in range(1, TC + 1):
    p, q = map(int, input().split())
    p_lst = find_coordinate(p)
    q_lst = find_coordinate(q)
    # print(p_lst)
    # print(q_lst)
    pq_lst = [0, 0]
    for idx in range(2):
        pq_lst[idx] = p_lst[idx] + q_lst[idx]

    print('#{0} {1}'.format(tc, find_Snumber(pq_lst)))
