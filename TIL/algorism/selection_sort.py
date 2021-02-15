# 선택 정렬

arr = [10,15,2,19,6,14]
arr = [9, 20, 2, 18, 11, 19, 1, 25, 3, 21, 8, 24, 10, 17, 7, 15, 4, 16, 5, 6, 12, 13, 22, 23, 14]
for i in range(len(arr)-1):
    min_idx = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i],arr[min_idx] = arr[min_idx], arr[i]

print(arr)