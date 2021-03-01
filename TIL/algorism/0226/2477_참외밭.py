#2477번 참외밭

"""
참외밭은 ㄱ-자 모양이거나 ㄱ-자를 90도, 180도, 270도 회전한 모양(┏, ┗, ┛ 모양)의 육각형이다.
다행히도 밭의 경계(육각형의 변)는 모두 동서 방향이거나 남북 방향이었다.
밭의 한 모퉁이에서 출발하여 밭의 둘레를 돌면서 밭경계 길이를 모두 측정하였다.

첫 번째 줄에 1m^2의 넓이에 자라는 참외의 개수를 나타내는 양의 정수 K (1≤K≤20)가 주어진다.
참외밭을 나타내는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로
둘레를 돌면서 지나는 변의 방향과 길이 (1 이상 500 이하의 정수) 가
둘째 줄부터 일곱 번째 줄까지 한 줄에 하나씩 순서대로 주어진다.
변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4로 나타낸다.
"""
import sys
sys.stdin=open('2477_input.txt','r')

T = int(input())

melon_dic={
    'garo':[],
    'sero':[],
}
H_lst =[]
for _ in range(6):
    D,H = map(int,input().split())
    if D == 1 or D == 2:
        melon_dic['garo'] = melon_dic.get('garo',[]) + [H]
    else:
        melon_dic['sero'] = melon_dic.get('sero',[])+[H]
    H_lst.append(H)
# print(melon_dic)
print(H_lst)

a = max(melon_dic['garo'])
b = max(melon_dic['sero'])

a_idx = H_lst.index(a)
b_idx = H_lst.index(b)

print(a_idx)
print(b_idx)


# 사람들이 %6 해주는 이유 --> index 에러 방지할라고!! %6 해주면 리스트 인덱스 넘어가는 애들도
# 다시 처음으로 올 수 있게 해준다. %n 테크닉...이거 유용하게 쓰자.
# 예를 들면 idx == 6이 왔다 %6 해서 0 --> 가장 처음 값 볼 수 있음
# 만약에 idx == -1 이 왔다 %6 하면 5 --> 가장 끝에 값 볼 수 있음 (이건 ㄹㅇ 처음 알았네)
garo_side = abs(H_lst[(a_idx-1)%6]-H_lst[(a_idx+1)%6])
# print(garo_side)
sero_side = abs(H_lst[(b_idx-1)%6]-H_lst[(b_idx+1)%6])
# print(sero_side)

big = a*b
small = garo_side*sero_side
# print(big, small)

squ = big-small

print(T*squ)


