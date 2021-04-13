# 1242번보다 간소한 버젼, 코드의 크기가 정해져 있다.
# 가로 길이도 56칸으로 고정되어있다.(7*8)

import sys
sys.stdin = open('1240_input.txt','r')

decipher = {
    0 : '211',
    1 : '221',
    2 : '122',
    3 : '411',
    4 : '132',
    5 : '231',
    6 : '114',
    7 : '312',
    8 : '213',
    9 : '112',
}

def proof_it(lst:list)->int:
    total = 0
    for idx in range(len(lst)):
        if idx%2:
            total += lst[idx]
        else:
            total += lst[idx]*3
    if total%10 == 0:
        return sum(lst)
    else:
        return 0


TC = int(input())

# 암호문은 전부 같은 꼴이므로, 한 줄만 뽑아서 분석하면 된다.
for tc in range(1,TC+1):
    N,M = map(int,input().split())
    for n in range(N):
        tem = input()
        am_i_null = '0'*M
        if tem == am_i_null:
            pass
        else:
            barcord = tem

    # barcord를 파싱하여, 1이 등장하는 시점부터 찾자.
    # 수 변환 3번이면 하나의 숫자가 된다 (1->0->1)
    flag,flag2,flag3 = False,False,False
    a,b,c = 0,0,0
    test =[]

    for idx in range(len(barcord)):
        # if문 작동 순서를 잘 고려해야한다.
        """
        if barcord[idx] == '1':
            a += 1
        로 하였더니, c가 올라가야하는 시점에도 a가 중복되서 카운팅 되었다.

        """
        if flag == True and flag2 == True and barcord[idx] == '1':
            c += 1
            flag3 = True
        if flag == True and flag3 == False and barcord[idx] == '0':
            b += 1
            flag2 = True
        if flag2 == False and flag3 == False and barcord[idx] == '1':
            a += 1
            flag = True
        
        # 종료된것
        if flag == True and flag2 == True and flag3 == True and barcord[idx] == '0':
            flag,flag2,flag3 = False,False,False
            test.append(str(a)+str(b)+str(c))
            a,b,c = 0,0,0

    deciphered_lst = []
    # 처음 사전형 구성을 잘못하였다.
    # "암호문 : 풀이문" 꼴로 구성해야했는데, 반대로 하는 바람에, value에서 key를 구하게 되었다.
    # 사전을 바꿔도 되지만, 학습을 위해 value에서 key를 구해보았다.
    for password in test:
        for item in decipher.items():
            if password == item[1]:
                deciphered_lst.append(item[0])
                break

    ans = proof_it(deciphered_lst)
    print('#{0} {1}'.format(tc,ans))


                
