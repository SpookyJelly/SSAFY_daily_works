# def per(arr,start):
#     # 재귀로 만들라면 필요한게,,, 일단 방문 처리한 것.
#     # 그리고 베이스 케이스 <-- start ==3 이면 방출?
#     if start == 3:
#         return
#
#
#
#     for i in range(len(arr)):
#         if not v[i]:
#             v[i] = i
#             per(arr,start+1)
#
#
#     pass


### 반복문을 이용한 순열 생성
v = [0] *3

arr = []

result = [0] * 3

for i in range(len(result)):
    if v[i]: continue
    v[i] = 1
    result[0] = i
    for j in range(len(result)):
        if v[j]: continue
        v[j] = 1
        result[1] = j
        for k in range(len(result)):
            if v[k] :continue
            v[k] = 1
            result[2]= k
            print(result)
            arr.append(result[:])
            v[k] = 0
        v[j]=0
    v[i]=0


print(arr)