# 무한 사전
"""
영어 알파벳으로 만들 수 있는 모든 단어(그것이 뜻이 없어도)가 수록된 무한 사전이 있다.
두 단어 P, Q가 주어질 때, 사전 상에서 P와 Q사이에 다른 단어가 있는지 없는지 판별하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 알파벳 소문자로 이루어진 단어 P가 주어진다.

두 번째 줄에는 알파벳 소문자로 이루어진 단어 Q가 주어진다.
P와 Q의 길이는 1이상 10이하이며, P는 Q보다 사전 상에서 먼저 오는 단어다.
(단, 사전에는 10자보다 더 긴 단어가 존재 할 수 있다.)

[출력]
각 테스트 케이스마다 용사가 사전 상에서 P와 Q사이에 다른 단어가 있다면 “Y”를, 아니면 “N”를 출력한다.


"""
# 접근방법
# 1. 단어 두개를 리스트로 변환해서 받는다.
# 2. 1번 리스트를 순회. 문자열도 대소 비교가 되므로, 0번 인덱스간 비교. 만약에 2번 리스트
# 0번 인덱스가 1번 리스트의 0 인덱스보다 크면, T 반환
# 3. 같으면 1 인덱스로 넘어간다.
# 4. 만약에 2번 리스트가 1번보다 길다면... 같은 위치 비교가 안되니까까 애초에 거르면 되겠네.
# len(lst1) < len(lst2) --> true ?? --> 아 이것도 아니네, man / mana 케이스 생각하면 오류다.
# 아니면 lst1에 a를 붙여줄까???

# aa / aaa -> 둘 사이에 아무것도 없다... ae / af --> 아니 얘들 사이에도 없네... caa cab
# 아예 아스키로 바꿔서 합차 구하는건 어떨까? 차가 1 이하면 없는거지.
# 아스키 전환은 좋은 아이디어인데, 한자리씩 가야한다 안그러면 또...다시 원점이네
# 어찌되었던, lst 1의 마지막 인덱스에서 조건문을 달아서 승부봐야겠다.
# 잠깐만... P 가 Q 보다 먼저 온다고 했잖아. aae / aaaf 의 경우에는 aaaf가 더 먼저온다!!

# 키워드 : chr , if , idx , ord
def isit(lst1,lst2):
    for idx in range(len(lst1)):
        if ord(lst2[idx]) - ord(lst1[idx]) > 1:
            return True
        elif ord(lst1[idx]) == ord(lst2[idx]):
            if len(lst2) > len(lst1): # acd / acde
                return True
            continue

        else:   # ord(lst2[idx]) - ord(lst1[idx]) ==1 
            # 77개 이후로 에러나는게 여기 구문인듯
            # aa / aaaaaa 문항을 True로 걸러내지 못한다 --> 아니는데? False 맞는데?
            # aa/ aaaea도 True로 못 거름
            if len(lst2) > len(lst1) and lst2[-1] != 'a':
                return True
            else: # len(lst2) == len (lst1) / len(lst2) < len(lst1)
                try:
                    if abs(ord(lst2[idx+1]) - ord(lst1[idx+1])) <= 1:
                        return False
                    else:
                        return True
                except:
                    False
            return False

    # if lst2[-1]=='a': # lst2의 마지막 리터럴
    #거짓 반환 분리하자

    # 그냥 len차이로 처음부터 거를까?
    # 생각해보니 P와 Q는 10자리. 사전에는 10자리 이상이 있다 --> 둘다 10자리로 만들고 시작?
    # aaaaa (aaaaa) / aaaaa aaaa(a) 이 둘 사이에는 뭐가 있지? aaaaa a / aaaaa ab / aaaaa aa 등등 다 있다
    # 둘다 10자리로 만들어보자. 그리고 지금 이 코드에 반례가 있나?? (aef / afa)
for tc in range(1,int(input())+1):
    lst1 = list(input())
    lst2 = list(input())
    #lst1 = lst1 + ['a'] * (10 - len(lst1))
    #lst2 = lst2 + ['a'] * (10 - len(lst2))
    if isit(lst1,lst2):
        print(f'#{tc} Y')
    else:
        print(f'#{tc} N')


# 76개만 성공...나머지는 왜 실패?