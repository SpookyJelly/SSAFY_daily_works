# d3 추가 문제. 정렬과 달팽이.

# 다음의 2차원 배열을 초기화 한 후 , 달팽이 모양으로 만드시오.
def snail(N, lst):
    #  0으로 찬 N * N 행렬 만들어짐
    squ = [ [0 for _ in range(N)] for __ in range(N)]
    row = 0
    col = -1
    switch = 1
    cnt = 0
    # 행/렬 순회인데, i /j는 행렬과 무관
    # 일단, 여기가 행 조절 부위이다.
    while N>0:
        for i in range(N):
            col += switch
            squ[row][col] = lst[cnt]
            cnt += 1

        N -= 1
        # 여기는 열 조절 부위이다.
        # row가 0부터 시작하는 이유는, 21번항에 의해 1이 된다. 이 for문이 적용되는 시점은 
        # row가 0인 시점이 아니라, 1부터 적용 되기에 row의 초기값을 0으로 한것이다. 위의 col은 0부터 적용되서 그렇다.
        # 0에서 1을 5번 더하면 5이라, 이게 인덱스로 들어가면 에러가 난다. 근데, 2번째 루프를 돌때 23번 라인에서 -1이 되어
        # row는 4가 된다. 그렇게 범위 밖을 나가지 않게 되는 것이다.
        for j in range(N):
            row += switch
            squ[row][col] = lst[cnt]
            cnt += 1
        switch *= -1
    return squ




arr = [[9,20,2,18,11],
    [19,1,25,3,21],
    [8,24,10,17,7],
    [15,4,16,5,6],
    [12,13,22,23,14]]

new_arr =[]
for idx in range(len(arr)):
    new_arr += arr[idx]
# print(new_arr)
# 이제 selecting sort를 이용해서 정렬합시다

# 먼저 최소값 인덱스를 설정하자.
# 리스트 전체를 순회해야므로, len -1 범위까지 조사
for i in range(len(new_arr)-1):
    minidx = i

    for j in range(i+1,len(new_arr)):
        if new_arr[j] < new_arr[minidx]:
            minidx = j
    
    tem = new_arr[i]
    new_arr[i] = new_arr[minidx]
    new_arr[minidx] = tem
    # new_arr[i],new_arr[minidx] = new_arr[minidx], new_arr[i]

# print(new_arr)

# 이제 달팽이 정렬을 해야한다. 함수로 완료하자.

print(snail(5,new_arr))