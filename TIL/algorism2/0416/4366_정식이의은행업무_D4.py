# 4366번 정식이의 은행업무

# 하지만 다행스럽게도 정식이는 평소 금액을 2진수와 3진수의 두 가지 형태로 기억하고 다니며, 
# 기억이 명확하지 않은 지금조차 2진수와 3진수 각각의 수에서 단 한 자리만을 잘못 기억하고 있다는 것만은 알고 있다. 
# 예를 들어 현재 기억이 2진수 1010과 3진수 212을 말해주고 있다면 
# 이는 14의 2진수인 1110와 14의 3진수인 112를 잘못 기억한 것이라고 추측할 수 있다.
# 정식이는 실수를 바로잡기 위해 당신에게 부탁을 하였다.
# 정식이가 송금액을 추측하는 프로그램을 만들어주자.
# ( 단, 2진수와 3진수의 값은 무조건 1자리씩 틀리다.  추측할 수 없는 경우는 주어지지 않는다. )

# 입력받은 이진수를 십진수로 바꾼다음, 그걸 XOR 연산을 통한 2진수 값 출력.
# 그걸 다시 십진수로 바꾼 리스트를 return 한다.



import sys
sys.stdin = open('4366_input.txt','r')

def bin_case(bin_num:int):
    # bin_num은 2진수 시절 4자리 였으니까, 4번 반복해야한다.
    # 그러기 위해 local scope에서 bin_num의 리즈시절 길이를 가져옴
    n = len(bin_money)
    result = []
    filt = 0b0001
    for i in range(n):
        tem = bin_num ^ filt
        result.append(tem)
        filt <<= 1
    return result



def bin_to_dec(lst)->int:
    dec = 0
    n = len(lst)
    i = 0
    for idx in range(n-1,-1,-1):
        dec += (2 ** idx) * int(lst[i])
        i += 1
    return dec

def tri_to_dec(lst)->int:
    dec = 0
    n = len(lst)
    i = 0
    for idx in range(n-1,-1,-1):
        dec += (3 ** idx) * int(lst[i])
        i += 1
    return dec

TC = int(input())
for tc in range(1,TC+1):
    bin_money = list(input())
    tri_money = list(input())
    convert = bin_to_dec(bin_money)
    bin_result = bin_case(convert)
    print(bin_result)
    ans = 0
    for bin_num in bin_result:
        # 삼진수 한자리 씩 바꾸기
        for idx in range(len(tri_money)):
            origin = tri_money[idx]
            # 아직 삼진수는 문자열 리스트 꼴로 저장되어있다.
            for k in ['0','1','2']:
                # 만약에 현재 삼진수의 자리수의 값이 현재 k 값과 같다면 스킵, 아니면 교환하고 원복
                if tri_money[idx] == k: continue
                else:
                    tri_money[idx] = k
                    # 10진수 변환해서 비교해서 맞으면 정답으로 인정하고 탈출
                    if bin_num == tri_to_dec(tri_money):
                        ans = tri_to_dec(tri_money)
                        break
                    tri_money[idx] = origin

    print('#{0} {1}'.format(tc,ans))

    

