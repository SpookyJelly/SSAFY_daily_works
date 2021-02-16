#4843번 특별한 정렬 (D3)
"""
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만,
이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 
가장 작은 수, 2번째 큰 수, 
2번째 작은 수 식으로 큰 수와 작은 수를 
번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
 

10 1 9 2 8 3 7 4 6 5

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다.
10<=N<=100, 1<=ai<=100

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 
특별히 정렬된 숫자를 10개까지 출력한다.

"""

# 접근방법
# 1. 우선 들어오는 숫자들을 오름차순 정렬부터 해준다.
# 2. 이후 순서에 맞게 재정렬한다.
# 2.1. 미지의 변수 N을 잡는다. new arr[len(n)-1] = arr[N]// newarr[N]=arr[len(arr)-(N+1)]
# 2.2 while문을 사용해서 저런식으로 전개하는데, N을 +1 한다. len(n) - 1 == N일때 종료
# ** 10까지 출력이니까,  알아서 잘 커트하자

# 해결방법
# 2.1 에서 새로운 정렬 리스트를 빈 리스트로 만든 후, 가장 큰값/ 가장 작은 값 페어로 이루어진
# (그러니까 정렬된 리스트에서는 가장 뒤에 있는 값/ 가장 앞에 있는 값)을 하나로 묶어서 집어넣어줬다.
# 집어 넣는 값은 while문의 순환에 따라 점점 바뀌며, len(arr) //2 번 반복된다

def selectsort(lst):
    
    for i in range(len(lst)-1):
        min_idx = i
        for j in range(i+1,len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        tem = lst[i]
        lst[i] = lst[min_idx]
        lst[min_idx] = tem
    return lst

# 셀렉션 정렬 작동 확인용
# print(selectsort([2,3,24,1,5,4]))


for tc in range(1,int(input())+1):
    len_N = int(input())
    lst_N = list(map(int,input().split()))
    # len_N = 10
    # lst_N = [1,2,3,4,5,6,7,8,9,10]
    # 순차정렬부터 해주고
    sorted_N = selectsort(lst_N)
    # 신기한 정렬이 될 빈 리스트 생성
    # 아니 그냥 어펜드로 더해버릴까?
    # new_arr = [ 0 for x in range(len(sorted_N))]
    new_arr = []
    idx = 0
    while (idx<len(sorted_N)//2):
        # new_arr[idx] = sorted_N[len_N-(1+idx)]
        # new_arr[idx+1] = sorted_N[idx]
        new_arr += [sorted_N[len_N-(1+idx)],sorted_N[idx]]
        idx += 1
    # print(new_arr[:10])
    new_arr = new_arr[:10]
    print('#{0} {1}'.format(tc,' '.join(list(map(str,new_arr)))))