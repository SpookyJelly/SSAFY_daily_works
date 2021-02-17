#1213번. String

'''

주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.

Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.

[제약 사항]

총 10개의 테스트 케이스가 주어진다.
문장의 길이는 1000자를 넘어가지 않는다.
한 문장에서 검색하는 문자열의 길이는 최대 10을 넘지 않는다.
한 문장에서는 하나의 문자열만 검색한다.

[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 찾을 문자열, 그 다음 줄에는 검색할 문장이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.


'''

import sys
sys.stdin = open("test_input.txt",'rt',encoding='UTF-8')

TC = 10

for tc in range(1, TC+1):
    N = int(input())
    Key = input()
    sentence = input()
    m = len(Key)
    n = len(sentence)
    cnt = 0
    i = 0
    j = 0
    while i<n:
        # 들어가는 조건 자체가 j와 i 가 서로 다를 때임.
        # 만약에 같다면 i와 j 모두 앞으로 쭉쭉 나간다.
        # 기본적으로 i과 j은 동시에 나가는데, 서로 다른 지점이 나오면 다른 영역을 바라본다.
        if Key[j] != sentence[i]:
            # i에서 그간 같았던 정도인 j 만큼 빼주고, Key의 처음부터 다시 조사하자는 뜻이다.
            # 만약에 i,j가 0부터 시작해 3 이였다. 그러면 i는 다시 0으로 가서 무한 루프에 빠질 것으로 보이나,
            # 아래의 무조건 거치는 2단계 덕분에 i는 1부터 시작할 수 있게 된다.
            # 한번 여기를 거치고 다시 들어올때는, 이미 i = i-0 이라, i는 아무런 변화 없이 앞으로 나갈 수 있게 된다.
            i = i-j
            j = -1

        # 무조건 거치는 두단계, 이 조건들 때문에, sentence는 다음으로 나아갈 수 있고,
        # j는 0~m 사이의 값을 가지게 된다.
        i+=1
        j+=1

        if j == m:
            cnt += 1
            j = 0

    print('#{0} {1}'.format(tc,cnt))

#
# def IamBrutal(key,sentence):
#     n = len(key)
#     m = len(sentence)
#     i = 0 # key와 연계
#     j = 0 # sentence와 연계
#     cnt = 0
#     while j<m:
#         if key[i] != sentence[j]:
#             j = j-i
#             i = -1
#
#
#         # 계속 더해지는 작자들
#         i+=1
#         j+=1
#
#         if i==n:
#             cnt+=1
#             i = 0
#     return cnt
#
# print(IamBrutal(Key,sentence))