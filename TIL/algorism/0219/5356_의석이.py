# 5356번 의석이의 세로로 말해요.

"""
칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다.
세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 
세로로 읽는다. 다음에 두 번째 글자들을 세로로 읽는다.
이런 식으로 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 
동일한 자리의 글자들을 세로로 읽어 나간다.

위의 그림 1의 다섯 번째 자리를 보면
두 번째 줄의 다섯 번째 자리의 글자는 없다. 
이런 경우처럼 세로로 읽을 때 해당 자리의 글자가 없으면, 
읽지 않고 그 다음 글자를 계속 읽는다.
그림 1의 다섯 번째 자리를 세로로 읽으면 D1gk로 읽는다.

칠판에 붙여진 단어들이 주어질 때, 
의석이가 세로로 읽은 순서대로 글자들을 
출력하는 프로그램을 작성하라.

"""
import sys
sys.stdin = open("input_5356.txt","r")


TC = int(input())
#TC = 1

for tc in range(1,TC+1):
    # 바로 5행의 문자열이 오니까. 아래와 같이 받는다.
    arr = [input() for _ in range(5)]
    #arr =['ABCDE','abcde','01234','FGHIJ','fghij']
    max_len = 0


    for element in arr:
        if len(element) > max_len:
            max_len = len(element)

# # try / except를 쓰면 매우 Cool 하긴 한데, 알고리즘 공부가 안된다.
#     for row in range(max_len):
#         for col in range(len(arr)):
#             try:
#                 print(arr[col][row], end='')
#             except:
#                 continue
#         print()
    print('#{0} '.format(tc), end='')
    for row in range(max_len):
        for col in range(len(arr)):
            # 이게 포인트가...[]일때는 리스트 그자체가 되고 [][]일때는 리스트의 요소가 되잖아
            # 엄청 아름답네...만약에 출력하려는 위치 인덱스가, 값을 가져와야할 list의 길이 보다 길다면,
            # 그 부분은 비어있으니까, 생략하게 된다.
            # 이거는 그림으로 그리는게 빠르다.
            if len(arr[col]) > row:
                print(arr[col][row], end= '')
    print()