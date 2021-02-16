# 4837번

"""
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다.
집합 A의 부분 집합 중 N개의 원소를 갖고 있고,
원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

"""

def bitlst(lst:list) -> list:
    n = len(lst)
    result = []
    for i in range(1<<n):
        temlst = []
        for j in range(n):
            if i & (1<<j):
                temlst.append(lst[j])
        result.append(temlst)
    return result


for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    cnt = 0
    lst_N= list(range(1,13))
    test_case = bitlst(lst_N)
    print(test_case)
    for element in test_case:
        if sum(element) == K and len(element) == N:
            cnt += 1
            print(element)
    print(f'#{tc} {cnt}')