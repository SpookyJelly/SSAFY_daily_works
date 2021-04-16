import sys
sys.stdin = open('1244_input.txt','r')

TC = int(input())

def bearclaw(numbers,swap):
    cnt = 0
    start = 0 # 시작 포인터
    while cnt < swap:
        # base case? 아무튼 더이상 교환할만한게 없을게
        if len(numbers)-1 == start:
            numbers = timekilling(numbers,cnt,swap)
            break
        maxi = selective_max(numbers,start)
        maxi_idx = finding(numbers,maxi)
        # 이제 교환하자
        if maxi > numbers[start]:
            numbers[start], numbers[maxi_idx] = numbers[maxi_idx], numbers[start]
            cnt += 1
        start +=1
    
    return numbers

def selective_max(numbers,start):
    new_lst = numbers[start:]
    return max(new_lst)

def finding(area,maxi):
    for idx in range(len(area)-1,-1,-1):
        if area[idx] == maxi:
            return idx

def timekilling(numbers,cnt,swap):
    while cnt <= swap:
        numbers[-1],numbers[-2] = numbers[-2],numbers[-1]
        cnt+=1
    return numbers

for tc in range(1,TC+1):
    numbers, swap = input().split()
    numbers = list(map(int,numbers))
    swap = int(swap)
    ans = bearclaw(numbers,swap)
    print(tc , ans)
    
# 테케 거의 다 맞았는데... 과감하게 버려야하나