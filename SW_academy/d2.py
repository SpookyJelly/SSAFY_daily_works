import sys
from pprint import pprint
sys.stdin = open("input.txt", "r")


def squ_sum(squ_row):
    for j in [0,1,2,9,10,11,18,19,20]:
        squ_sum=sum(squ_row[j])+sum(squ_row[j+3])+sum(squ_row[j+6])

        if squ_sum != 45:
            return False
    return True

T = int(input())

sutoku = []

for num in range(1,T+1):
    for row in range(9):
        array = list(map(int,input().split()))
        sutoku.append(array)
        squ_row=[]
        row_sum,col_sum=[0,0]
    # 각행의 합이 45인지 확인 
    for i in range(len(sutoku)):
        row_sum = sum(sutoku[i])
    # 순회 중에 하나라도 45가 아니면 break
        if row_sum != 45:
            print('0')
            break
    # sutoku[0][0:3] --> [7,3,6] // sutoku[0][3:6] --> [4,2,9]
        #print(f'@{num} {row_sum} {len(sutoku)}')
        for x in [0, 3, 6]:
            # squ_row = [[7,3,6],[4,2,9]....]
            squ_row.append(sutoku[i][x:x+3])
        #col_sum += sutoku[k][0]...
        for k in range(len(sutoku)):
            col_sum += sutoku[k][i]
            # 의도 : 만약에 한 열을 전부 다 더했는데, 45가 아니면 break
            if i==9 and col_sum != 45:
                break
            col_sum = 0 
        #print(f'@{num} {col_sum} {len(sutoku)}')

       
    print(row_sum,col_sum,squ_sum(squ_row))            
    if (row_sum == 45) and (col_sum==45) and squ_sum(squ_row):
        print(f'#{num} 1')
    else:
        print(f'#{num} 0')
    sutoku = []
