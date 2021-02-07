import sys
from pprint import pprint
sys.stdin = open("input.txt", "r")

def cube(list1,list2,list3):
    # 리스트를 각 3개로 쪼개기
    # 1번 리스트
    list1_a=list1[0:3]
    list1_b=list1[3:6]
    list1_c=list1[6:9]
    # 2번 리스트
    list2_a=list2[0:3]
    list2_b=list2[3:6]
    list2_c=list2[6:9]
    #3번 리스트
    list3_a=list3[0:3]
    list3_b=list3[3:6]
    list3_c=list3[6:9]
    
    A=sum(list1_a+list2_a+list3_a)
    B=sum(list1_b+list2_b+list3_b)
    C=sum(list1_c+list2_c+list3_c)
    
    if A==45 and B ==45 and C==45:
        return True
    return False

def row(sutoku):
    for i in range(9):
        result=0
        for k in range(9):
            result+=sutoku[k][i]
        if result != 45:
            return False
    return True

def col(sutoku):
    for i in range(9):
        col = 0
        for k in range(9):
            col += sutoku[i][k]
            if k==8 and col != 45:
                return False
    return True

T = int(input())

for tc in range(1,T+1):
    sutoku=[]
    for N in range(9):
        array = list(map(int,input().split()))
        sutoku.append(array)
        cnt = 0
    for num in [0,3,6]:
        a=row(sutoku)
        b=col(sutoku)
        c=cube(sutoku[num],sutoku[num+1],sutoku[num+2])
        if a and b and c:
            cnt +=1
    if cnt == 3:
        print(f'{tc} 1')
    else:
        print(f'{tc} 0')
