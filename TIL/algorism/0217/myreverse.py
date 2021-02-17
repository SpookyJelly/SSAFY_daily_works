# reverse 함수 만들어보기 
# 1. 새로운 문자열로 만들어보기
# 2. list로 만들어서 교환하기
# 단, 리스트 슬라이싱 [::-1]은 쓰지말아라. (알고리즘 연습이 안됨)

# print(ord('0')==48)

# 일단 str은 인덱싱이 되니까 그걸 활용하면 될듯?
# 1번 새로운 문자열로 만들어보기 방법을 써보자. 빈 문자열 하나 만들고 거기에 역순 인덱싱 추출한 값들 넣으면 될듯
def myreverse(string):
    r_string = ''
    for idx in range(len(string)-1,-1,-1):
        r_string += string[idx]
    return r_string


print(myreverse("Iamaboy"))

# 2번 list로 만들어서 교환하기.
# 문자열을 리스트로 만든다음, 임시 변수 하나 만들어서 첫 값 집어넣고, 마지막 값을 첫값으로, 마지막 값을 임시값으로 바꾸길 N/2회 반복
# 대상이 자꾸 바뀌니까, 인덱스 위치를 잘 생각해보자


# 시작점과 끝점이 매 루프마다 바뀌는 문제에 조금 약한 모습을 보이는 나다.
# 매 루프마다 idx가 커지니까, 이 커지는 루프에 맞춰서 시작점, 끝점을 조절해야하는데, 그 감각에 익숙치 않은거 같다.
def myreverse2(string):
    lst_string = list(string)
    N = len(lst_string) // 2 
    for idx in range(N):
        tem = lst_string[idx]
        # idx가 커지면서, lst_string의 처음 값에서 점점 뒤의 값으로 간다. 마찬가지로, lst_string의 뒤의 값도 점점 앞으로 온다.
        lst_string[idx] = lst_string[len(lst_string)-idx-1]
        lst_string[len(lst_string)-idx-1] = tem
    for string in lst_string:
        print(string, end= '')
    print()

# 따로 빈 문자열 만들어서 정렬해도 되지만, 그냥 함수에서 출력까지 되도록 설정해보았다.
myreverse2('abcd') 
myreverse2('bvcsq')
