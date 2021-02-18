# 4864번 문자열 비교

"""

두 개의 문자열 str1과 str2가 주어진다.
문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.
예를 들어 두 개의 문자열이 다음과 같이 주어질 때,
첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.

ABC

ZZZZZABCZZZZZ

두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.


ABC

ZZZZAZBCZZZZZ

문자열이 일치하지 않으므로 0을 출력.




[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  (1≤T≤50)
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인
str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)



[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

"""

# 접근법: 그냥 str2에 str1가 있는지 확인 하는 문제이므로, 브루트포스 및 각종 알고리즘으로 서치해준다.

def IamBrutal(key,sentence):
    N = len(key)
    M = len(sentence)
    i = 0 # key와 엮는 부분
    j = 0 # sentence와 엮는 부분

    while j<M:

        if key[i] != sentence[j]:
            j = j-i
            i = -1

        i += 1
        j += 1

        if i == N:
            return 1

    return 0



TC = int(input())
for tc in range(1,TC+1):
    N = input()
    M = input()
    ans = IamBrutal(N,M)
    print('#{0} {1}'.format(tc,ans))












