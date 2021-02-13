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