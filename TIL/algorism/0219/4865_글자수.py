import sys

sys.stdin = open("input_4865.txt","r")

T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    # str1 각 문자에 카운트를 세기 위함
    cnt = [0] *len(str1)

    #str1의 길이만큼 순회
    for i in range(len(str1)):
        # str1[i]가 str2에 몇개 있는지 확인
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt[i] += 1

    ans = 0
    # 가장 큰 값 찾기
    for i in range(len(cnt)):
        if ans < cnt[i]:
            ans = cnt[i]