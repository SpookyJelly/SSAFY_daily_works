#1221번 GNS

"""
숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서
사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.

"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여
출력하는 프로그램을 작성하라.

예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우
정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

[입력]

입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.
그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.
그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며,
문자열의 길이 N은 100≤N≤10000이다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.


"""
# 접근법
# 일단 입력은 잘 받았으니까, 좀 손을 봐주자.
# 외계인의 문자체계에게 인덱스 값을 부여할까?
# 아니면 그냥 replace 사용해서 숫자로 만들어준다음에, 정렬하고 다시 원상복구?
# 이게 제일 빠른 해결책인거 같은데 딕셔너리 이용하는건 어떤가?
# replace 대신에 딕셔너리로 교체해보는게 괜찮아보이는데... 일단 해볼까요



import sys
sys.stdin = open("GNS_test_input.txt", "r")


def selectingsort(lst):

    for i in range(len(lst)-1):
        min_idx = i
        for j in range(1+i, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        tem = lst[i]
        lst[i] = lst[min_idx]
        lst[min_idx] = tem
    return lst



num_dic = {
    'ZRO' : 0,
    'ONE' : 1,
    'TWO' : 2,
    'THR' : 3,
    'FOR' : 4,
    'FIV' : 5,
    'SIX' : 6,
    'SVN' : 7,
    'EGT' : 8,
    'NIN' : 9,

}
#print(num_dic.keys())
TC = int(input())
#TC = 10
for tc in range(1,TC+1):
    t_num, N = list(input().split())
    N = int(N)
    str_lst = list(input().split())
    #str_lst = ['SVN', 'FOR', 'ZRO', 'NIN', 'FOR', 'EGT', 'EGT', 'TWO', 'FOR', 'FIV', 'FIV']
    #print(t_num, N, type(N))
    #print(str_lst)
    for idx in range(len(str_lst)):
        for key in list(num_dic.keys()):
            if str_lst[idx] == key:
                str_lst[idx] = num_dic[key]
    # 이제 외계인 문제를 예쁘게 정렬 해준다음에.. 다시 밸류로 바꿔주면 된다
    #print(str_lst)
    isortlst= selectingsort(str_lst)
    #print(isortlst)

    # 딕셔너리의 아이템 뽑은 다음에, 이번에는 밸류와 isortlst의 요소를 비교해서 같으면 key로 요소를 바꿔준다
    for k in range(len(isortlst)):
        for kv in list(num_dic.items()):
            if isortlst[k] == kv[1]:
                isortlst[k] = kv[0]
    print('#{0}'.format(tc))
    print(*isortlst)


# 다시 생각해볼 문제.
# 딕셔너리를 기껏 만들어놓고, 리스트 방식을 썼다. 그냥 순회를 돌면서 외계인 숫자들을 키 값 삼아 밸류를 하나씩 증가시켜주고
# 출력할때 키를 밸류 값 만큼 출력해주면 된다. 다시 한 번 해주자.