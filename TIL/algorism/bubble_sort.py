def Bubble_sort(arr):
    # 제일 끝 인덱스부터 고른다.
    for i in range(len(arr)-1, 0, -1):
        # 2중 for문으로 처음 인덱스부터 끝 인덱스까지를 비교
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# 그러면 앞으로 이동하면서 자신보다 앞에 있는 애들 대상으로 비교하니까, 한번에 정렬되겠네.
# 나는 이걸 생각못해서 앞 뒤 순서 한번 바꾸는거만 해주고, while문으로 루프를 엄청 돌리는 불완전한 방식을 썼다.

for tc in range(1, int(input())+1):

    # N = int(input())

    #number = list(map(int,input().split()))
    number = [4,5,2,3,7,6,2,1]
    print(Bubble_sort(number))

    # print("#{0} {1}".format(tc,number[-1]-number[0]))

        