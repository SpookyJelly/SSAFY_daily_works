# 연습문제 1번
# 5*5 2차 배열에 무작위로 25개의 숫자로 초기화 후
# 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오

# 25개의 요소에 대해서 모두 조사하여 총합을 구하시오.
# 벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의하시오.

# ARR[r][c]를 기준으로 네 방향의 값과의 절대값의 합을 구한다.
ARR = [[1,2,3],[4,5,6],[7,8,9]]
N = len(ARR)

# 순서 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 혹은 2차원 배열로는 이렇게 쓴다.
# dt =[[-1,0], [1,0],[0,-1],[0,1]]

# abs가 봉인되었으니, 나만의 abs 만들자
def myabs(vaule):
    if vaule > 0 :
        return vaule
    else:
        return vaule * -1

sumV = 0

for r in range(N):
    for c in range(N):
        for i in range(4):
            newR = r+dr[i]
            newC = c+dc[i]
            # 새로운 행/열 인덱스가 원래 범위의 안쪽에 있을때만, 더하기 수행. newR / newC 는 -1 혹은 4가 되고 있지만,
            # if 문에서 인덱스로 활용되지 않았기에, 인덱스 에러 없이 스무스하게 넘어간다.
            # 이 for문은 if문이 없다면 그저 newR과 newC라는 변수를 할당하는 구문임.
            if newR >= 0 and newR < N and newC >=0 and newC < N:
                sumV += myabs(ARR[r][c] - ARR[newR][newC])
print(sumV)

