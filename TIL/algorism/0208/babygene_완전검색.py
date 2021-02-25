# 완전검색 기법을 이용한 babygene 써치

def babygene(lst):
    N = len(lst)
    result= []
    for i in range(1<<N):
        tem = []
        for j in range(N):
            if i&(1<<j):
                tem.append(lst[j])
        result.append(tem)

    return result
# 모든 부분집합이 나온다. --> 생각해보니 부분집합이 아니였다. 순열을 구해야한다.

# 순열 구하는 함수 -> 주말에 해석해보자. 어짜피 이번 시험에는 아니 나온다...
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result




#N_list = list(input())
N_list = ['6','6','7','7','6','7']
target = babygene(N_list)
print(permute(N_list))


triple,run,cnt = [0,0,0]