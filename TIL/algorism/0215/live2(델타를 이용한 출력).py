arr =[[1,2,3,4],
    [5,6,7,8],
    [10,11,12,13]
    ]

N = 3 # 행의 길이
M = 4 # 열의 길이

len (arr) # 전체 리스트의 행의 길이를 뽑아오는 방법
len (arr[0]) # 전체 리스트의 열의 길이를 뽑아오는 방법


# 행 우선 순회 방식

print('행 순회입니다.')
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j])


# 행 우선순회를 역으로 돌아보자.
print('행 역 순회입니다')
for i in range(len(arr)):
    for j in range(len(arr[0])-1,-1,-1):
        print(arr[i][j])



# 열 우선순회
print('열 순회입니다.')
for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j]) # 필요한 연산 수행


# 열 우선순회를 역으로 돌아보자
print('열 역순입니다.')
for j in range(len(arr[0])-1,-1,-1):
    for i in range(len(arr)):
        print(arr[i][j])


# 지그재그 순회
print('지그재그 순회입니다.')
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i%2:
            print(arr[i][j])
        else:
            print(arr[i][len(arr[0])-1-j]) # 맞나??

# #  지그재그 순회2
# print('지그재그 순회 2입니다.')
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         arr[i][j+(len(arr[0])-1-2*j+(i%2))] # i가 홀수인지, 짝수인지에 따라 뒤에 붙은 값들이 사라지거나 한다.


#델타를 이용한 행열 탐색
# 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

arr = [[1,2,3],
        [4,5,6],
        [7,8,9]]

r = 1
c = 1

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 혹은 바로 이걸 2차원 리스트로 바꿔도 좋다.
drc = [[-1,0],[1,0],[0,-1],[0,1]]

for i in range(4):
    nr = r+dr[i]
    nc = c+dc[i]

    # 만약 델타의 범위가 행렬을 벗어나게 되면, continue로 아무것도 못하게 만든다.
    if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
    
    print(arr[nr][nc])