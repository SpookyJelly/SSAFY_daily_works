# 카운팅 정렬 알고리즘 만들어보기

def counting (lst):
    # 최대값 몰라도 checklst (등장한 숫자의 빈도수를 세어주는 리스트)를 가변형으로 구성하면 된다.
    # max(lst)+1 하는 이유는 인덱스 크기 맞추기 위해서, 만약 lst에 5가 나오는데, max(lst)만 하면 크기가 5인 리스트가 만들어진다.
    # 우리는 checklst의 인덱스 값과 요소의 등장횟수를 일치시키기려기에, 
    # 최대값 N인 lst를 받아줄 checklst에는 0~N까지의 인덱스가 있어야한다.(크기 N+1)
    
    checklst = [0] * (max(lst)+1) 
    copy_lst = [0] * len(lst)
    for num in lst:
        checklst[num] += 1
    for idx in range(1,len(checklst)):
        checklst[idx] += checklst[idx-1]

    for element in lst:
        copy_lst[checklst[element]-1] = element
        checklst[element] -= 1
    return copy_lst
print(counting([1,3,4,2,2,3]))   