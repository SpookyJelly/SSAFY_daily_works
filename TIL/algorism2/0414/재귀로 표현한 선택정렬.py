def selectionsort(A,s):
    n = len(A)
    if s == n-1:return

    mini = s
    for i in range(s, n):
        if A[mini] > A[i]:
            mini = i
    A[mini],A[s] = A[s],A[mini]
    selectionsort(A,s+1)

arr = [3,54,1,23,5,24,5,4,6]
print('정렬 전:',arr)
selectionsort(arr,0)
print('정렬 후:',arr)


# # 반복으로 표현하는 경우
# n = len(A)
# for i in range(n-1):
#     mini = i
#     for j in range(i+1,n):
#         if A[j] < A[mini]:
#             mini = j
#     A[mini],A[i] = A[i],A[mini]