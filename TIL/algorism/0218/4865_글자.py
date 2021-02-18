# 4865번 글자수
# 이상하게 파일 이름을 4865_글자수.py 로 지정하면 파이참이 얘를 py파일로 인식하지를 못한다?

"""

두 개의 문자열 str1과 str2가 주어진다.
문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고,
그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.

예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우,
str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.

파이썬의 경우 딕셔너리를 이용할 수 있다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과
길이가 M인 str2가 각각 다른 줄에 주어진다. 5≤N≤100, 10≤M≤1000, N≤M

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

"""

# 접근법
# 일단 set으로 str1의 중복꼴을 없앤다음에
# str1의 요소들로 str2를 순회하면서 최대값 찾아서 반환하면 되겠다.
# 최대값 반환하는 것도 딕셔너리와 나만의 함수를 이용해서 반환하자

def mymax(lst):
    maxi = 0
    for idx in range(len(lst)):
        if lst[maxi] < lst[idx]:
            maxi = idx

    return lst[maxi]



TC = int(input())
for tc in range(1,TC+1):
    str1 = input()
    str2 = input()

    sstr1 = list(set(str1))

    str_dic ={}
    for i in sstr1:
        # 이거 간만에 쓰니까 까먹었었다. str_dic라는 빈 사전형에
        # 키값으로 쓸 애들의 집합인 sstr1의 밸류와 같이 넣어준다.
        #get은 딕셔너리 안의 키 값에 맞는 밸류를 가져오는데, get(x,디폴트값)을 사용해
        # 딕셔너리 안에 찾으려는 Key값이 없을 경우 미리 정해준 디폴트 값을 가져올 수 있다.
        # 자꾸 혈액형 문제가 머리에 맴돈다..아니 제목 문제였구나
        # 그 문제는 무작위로 주어진 문자열이 총 몇번 등장했는지를 나타내는 문제였는데,
        # for word in book_title:
        #   dic[word] = dic.get(word,0) + 1
        # 를 사용해서 주어진 문자열이 등장할때마다 1씩 증가시켰다. 처음에만 디폴트 값을 가져오지.
        # 이후로는 dic.get(word)에 값이 있으니까, word의 밸류를 가져온후 더해서 dic[word]의 밸류를 증대 시켰다. 아무튼 그럼
        str_dic[i] = str_dic.get(i,0)

    #print(str_dic)

    for element in str2:
        if element in sstr1:
            str_dic[element] += 1

    #print(str_dic)
    ans = list(str_dic.values())
    print('#{0} {1}'.format(tc, mymax(ans)))