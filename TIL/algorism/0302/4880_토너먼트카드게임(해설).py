#4880번 해설

# 이 문제처럼 인덱스에 대한 수식이 주어지는 경우 ( ex. 시작 인덱스가 1인 경우. 중간값을 구하는 식이 있는 경우 등...)
"""

문제에서 사용되는 인덱스와, 내가 사용하게 되는 인덱스가 동일한지 확인할 것.


"""
# 배열은 정해져 있다.
# 시작점 i랑 j를 받으려고 합니다.
def game(i,j):

    if i==j:
        return i # game(1,1) 이런 식으로 올테니까, i를 반납하든, j를 반납하든 상관 없다.

    else:

        aidx = game(i,(i+j)//2)
        bidx = game(((i+j)//2) + 1,j)

        # aidx,bidx는 인덱스이다. 누가 이겼는지를 알 수 있다.
        if arr[aidx] == '1':
            if arr[bidx] == '2':
                return bidx
            elif arr[bidx] == '3':
                return aidx
        elif arr[aidx] == '2':
            if arr[bidx] == '1':
                return aidx
            elif arr[bidx] =='3':
                return bidx

            #... 쭉 쭉 쭉


N = 5
arr = [0]+[2,1,1,2,3] # 인덱스 맞추기 위해서 앞에 0을 더한다.
print(game(1,N))

# 이 기본 아이디어로 한번 해보자.