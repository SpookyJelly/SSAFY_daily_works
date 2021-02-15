arr = [[1,2,3],[2,3,4],[3,4,5],[4,5,6]]

# 첫번째 행의 데이터를 출력

for _ in range(len(arr[0])):
    print(arr[0][_], end=' ')

for i in range(len(arr)):
    print(*arr[i]) # * 붙이면 리스트 괄호가 사라진다 !


# 첫번째 열의 데이터를 출력

for c in range(len(arr[0])):
    for r in range(len(arr)):
        print(arr[r][c], end = ' ')
    print()

# 첫번째 행의 합을 구하라.
value = 0
for i in range(len(arr[0])):
    value += arr[0][i]
print(value)

# 전체 행의 합을 구하라

value = 0
for r in range(len(arr)):
    for c in range(len(arr[0])):
        value += arr[r][c]
print(value)

# 각 행의 합을 구해 합이 제일 큰 행의 값을 출력해라

maxi = 0
value = 0
for r in range(len(arr)):
    for c in range(len(arr[0])):
        value += arr[r][c]

    if value > maxi:
        maxi = value

    value = 0
print(maxi)


# 각 열행의 합을 구해 합이 제일 큰 열의 값을 구해라.

maxi = 0
value = 0
for c in range(len(arr[0])):
    for r in range(len(arr)):
        value += arr[r][c]

    if value > maxi:
        maxi = value

    value = 0
print(maxi)