#4880번 토너먼트 카드게임

"""
1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다.
전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.
그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데,
i번부터 j번까지 속한 그룹은 파이썬 연산으로 다음처럼 두개로 나눈다.

1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다.
전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.
그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데,
i번부터 j번까지 속한 그룹은 파이썬 연산으로 다음처럼 두개로 나눈다.

[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 별로 인원수 N과 다음 줄에 N명이 고른 카드가 번호순으로 주어진다. 4≤N≤100
카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다.

"""
import sys
sys.stdin = open('4880_input.txt','r')


def versus(arr):
    # mid = ((arr[0][0]+1)+(arr[-1][0]+1))// 2
    mid = (len(arr) + 1) // 2 # 1번부터 시작하는 것은 짝수인 경우와 홀수인 경우를 구분하라.. 9개일때는 어떻게 되는지? -> 대개 반토막 내는게 문제
    # mid = len(arr) // 2   9//2 -> 4 [0:4] 0 1 2 3
    # (1+ 9) // 2 --> 5 --> 1부터 5까지 [1:6]라는 범위가 나와야함 --> 1 2 3 4 5
    # mid = (len(arr) +1) //2  10//2 -> 5 [0:5] 0 1 2 3 4
    if len(arr) == 1:
        return arr
    else:
        a = versus(arr[:mid])
        b = versus(arr[mid:])
        # 여기 밑에서부터 가위바위보 전개...
        # 밑으로 내려갈 수 있는 경우는 a/ b 길이가 1이 되었을 때 뿐이다.
        # 같으면 인덱스 작은 애가 이긴다.
        if a[0][1] == b[0][1]: # a = [(0,1)]
            return a
        else:
            if a[0][1]==1:
                if b[0][1] == 3:
                    return a
                else:
                    return b
            if a[0][1] == 2:
                if b[0][1] == 1:
                    return a
                else:
                    return b
            if a[0][1] == 3:
                if b[0][1] == 1:
                    return b
                else:
                    return a

TC = int(input())

for tc in range(1,TC+1):
    N = int(input()) # 케이스별 인원 수
    arr = list(map(int,input().split()))
    arr_i = []
    for p in enumerate(arr):
        # print(p)
        arr_i.append(p)
    print(arr_i)
    ans = versus(arr_i)
    print('#{0} {1}'.format(tc,ans[0][0]+1))


