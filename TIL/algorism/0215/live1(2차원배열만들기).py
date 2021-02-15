arr = [[1,2,3,4][1,2,3,5]]

for i in arr:
    print(i)


# 3 4 
# 1 2 3 4
# 5 6 7 8
# 9 1 2 3

# 크게 3가지 방법으로 2차원 배열을 만들어도 된다.

# arr = []

# N, M = map(int,input().split())

# arr = []

# for i in range(N):
#     arr.append(list(map(int,input().split())))

# for i in arr:
#     print(i)


# for i in range(N):
#     arr[i] = (list(map(int,input().split())))

# arr = [list(map(int,input().split())) for _ in range N]

# for i in arr:
#     print(i)