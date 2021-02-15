#접근법
# 1. 일단 N*N 크기의 0으로 가득찬 행렬을 만든다
# 2. 1~N까지를 가진 리스트를 뽑아서, 그 안을 순서대로 채워넣는다.

# 아니다. 일단 요청된 행렬을 만드는거다. 1~N까지 제자리에 위치한..
# 그리고 그걸 순서에 맞게 출력?
# 아니 처음부터 달팽이 꼴로 넣을수 있나?
# 아니면 1~N 행렬을 서순 맞게 집어넣은 다음에, 출력 순서만 조절하는게 어떨까


# 최종 해결책 : row와 col의 변화를 제 3의 변수인 switch로 조절했다.
# 값의 입력은 for 문을 이용해 N 회 반복하도록 했는데, 행과 열의 인덱스에 독립적으로 각각 N번씩 돈다.
#

def snail(N): # N == 3으로 가정하자
    squ = [[0 for _ in range(N)] for __ in range(N)] # 이거 그냥 [0] *N 이런 식으로 하면 shallow copy 되서 꼬인다.
    row = 0
    col = -1
    cnt = 1 # 실제로 빈칸에 들어갈 값
    switch = 1 # row와 col을 조정해줄 값
    while(N>0):
        for i in range(N): # 0~2
            col += switch
            squ[row][col] = cnt
            cnt += 1
        N -= 1
        for j in range(N): # 0 ~ 2
            row += switch
            squ[row][col] = cnt
            cnt += 1
        switch *= -1 # switch는 1 , -1 을 왔다갔다 할 뿐이다.
    return squ

# a = snail(3)

# for idx in range(len(a)):
#     print(*a[idx]) # *는 컨테이너 타입의 데이터를 Unpacking 할 때도 이용할 수 있다.

for tc in range(1,int(input())+1):
    N = snail(int(input())) # 리스트
    print(f'#{tc}')
    for idx in range(len(N)):
        print(*N[idx])
    
