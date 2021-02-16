# 4839번 이진탐색

"""

책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때,
이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.

"""
# 접근 방법
# 1. 일단 함수 설계 input(책의 전체 쪽 수 , 찾을 쪽 번호)
# 2. range(1,책 전체 쪽수+1) 한 후 이 범위 내에서 for문 돌림.
# 3. if 찾을 쪽 번호 > len(range())//2 --> 범위 수정 range = [len(range())//2 : 끝] cnt +=1
# 3.1 if 찾을 쪽 번호 < len(range())//2 --> 범위 수정 range= [시작 : len(range())//2] cnt += 1
# 3.2 if 찾을 쪽 번호 == len(range())//2 --> return cnt
# 4. 3번 시퀀스 반복..

def binary(lst:list,page):
    half_idx = 0
    cnt  = 0
    while True:
        half_idx = len(lst)//2 # 인덱스다. 처음에는 200이다
        a = lst[half_idx] # lst[200] --> 201
        if lst[half_idx] > page:
            lst = lst[:half_idx-1] # lst[:200] --> lst [ 0~ 199]
            cnt += 1
        elif lst[half_idx] == page: # lst[half_idx] ==> lst[200] --> 201이랑 비교해도 ㄱㅊ음
            cnt +=1
            break
        else: # lst[half_idx] < page # lst[200] ==> 200 <page?
            lst = lst[half_idx:]  # lst[20:] --> lst[200~400]
            cnt += 1
    print(lst[half_idx],cnt)

# 자꾸 에러나는 이유가 리스트를 변형해서 그런거 같다... 다른식으로 해보자.

# 추가 확인 사항 : 리스트 슬라이싱의 경우는 딥 카피가 되는 것이 맞다. 바이너리 함수 자체는 문제 없다. 다만 시간이 오래걸리는거 빼면
# 다만 함수 간 리스트가 넘어갈때는 쉘로우 카피가 되서 내부에서 바뀌었을때, 돌아왔을때도 바뀌어 있을 수 있다.

for tc in range(1,int(input())+1):
    P,Pa,Pb = list(map(int,input().split()))
    P = list(range(1,P+1))
    binary(P,Pa)
    print(P)
    binary(P,Pb)