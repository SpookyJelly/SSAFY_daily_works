# arr[] : 데이터 저장하는 배열
# n : 원소의 개수, k : 현재까지 교환된 원소의 개수
def perm2(arr, n,k):
    if k==n:
        print(arr)
    else:
        for i in range(k,n):
            arr[k],arr[i] = arr[i],arr[k]
            perm2(arr,n,k+1)
            arr[k],arr[i] = arr[i],arr[k]

# 재귀적으로 만들기
def perm(arr, depth, n, k):
    # depth가 0부터 시작하여 k라면 k개를 모두 뽑은 것이므로 print하고 return
    if (depth == k):
        print(arr)
        return
    for idx in range(depth, n):
        # 각 depth에 대해 남아 있는 것들 중에 모두 뽑아보고,
        # 해당 경우에 대해 재귀적으로 perm 함수를 돌리고,
        # 원상복구 하여 다시 경우의 수를 찾는다
        arr[idx], arr[depth] = arr[depth], arr[idx]
        perm(arr, depth+1, n, k)
        arr[idx], arr[depth] = arr[depth], arr[idx]

# arr=list(input())
arr = [1,2,3]
n = len(arr)
# perm(arr,0,n,3)
perm2(arr,n,0)


