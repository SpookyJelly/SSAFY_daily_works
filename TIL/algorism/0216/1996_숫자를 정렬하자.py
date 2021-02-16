# 1996번 숫자를 정렬하자.

"""
주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.

[제약 사항]
N 은 5 이상 50 이하이다.


[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 이 주어지고, 다음 줄에 N 개의 숫자가 주어진다.


[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 그냥 정렬하는거니까, 이왕하는거 이번에 배운 selecting sort를 쓰자

"""
# 오름 차순으로 정렬된 1~k번 리스트만 출력할 수 있는데, 이번에는 그런 조건 없으니 통으로 반환하자
def selecting(lst):
    # 그래서 len(lst)-1까지를 i로 설정한다. 만약에 k번까지만 보고 싶으면 여기에 k를 넣으면 됨
    for i in range(len(lst)-1):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        tem = lst[i]
        lst[i] = lst[min_idx]
        lst[min_idx] = tem
    return lst

# print(selecting([4,4,32,325,2,3,1,5]))

TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    N_lst = list(map(int,input().split()))
    print('#{0}'.format(tc), end = ' ')
    N_lst = selecting(N_lst)
    for idx in range(len(N_lst)):
        print(N_lst[idx], end = ' ')
    print()
