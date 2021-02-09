"""
# 4828 최소 최대값
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.


[입력]

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

"""
import sys
sys.stdin = open("sample_input.txt", "r")


T = int(input())

for i in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    # 각 케이스마다 값 초기화. mini는 0으로 설정하면 아무것도 저장 안될 수 도 있으니,
    # 처음값을 지정하여 오류를 막았다.
    maxi, mini = [0, N_list[0]]

    # N_list 전체에 대해 검사.
    # N_list의 요소가 지정된 최대값/ 최소값과 비교하여 수정 소요가 있는지 판단
    for num in N_list:
        if num < mini:
            mini = num
        elif num > maxi:
            maxi = num
    print('#{0} {1}'.format(i, maxi-mini))

    # N을 사용하지 않았는데, 이걸 사용해서 설계했더라면 자원 낭비가 덜 하지 않았을까?
