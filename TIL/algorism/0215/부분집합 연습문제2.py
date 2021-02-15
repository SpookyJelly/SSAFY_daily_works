# 연습 문제 2
# 부분집합 합 문제 구현
# 실제로 10개의 정수를 입력받아 부분집합의 합이 0이 되는 것이 존재하는 지를 계산하는 함수를 작성해보자

test = list(map(int,input().split()))
N = len(test)
result = []
for i in range(1<<N):
    arr = []
    for j in range(N):
        if i & (1<<j):
            arr.append(test[j])
    result.append(arr)

for lst in result:
    if sum(lst) == 0:
        print('합이 0이 되는 것이 존재합니다.')
    else:
        pass