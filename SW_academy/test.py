arr = [3,6]
n = len(arr)
for i in range(1<<n):
    for j in range(n):
        if i&(1<<j): #i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j],end=' ')
    print()
