# 오후의 과제. str() 사용하지 않고 itoa()를 구현해보자
# 양의 정수를 입력받아 문자열로 변환하는 함수
# 입력 값: 변환할 정수 값, 변환된 문자열을 저장한 문자배열
# 반환값 : 없음
# * 음수를 변환할 때는 어떤 고려사항이 필요한가요?

def itoa(inti):
    # 인풋으로 오는 값들이 어짜피 숫자 값이므로, 따로 검증 과정은 필요는 없다.
    # 기본적인 아이디어는 들어온 숫자를 자리수 분해 한 다음, chr 함수로 문자화 하는 것이다.
    # 이 과정에서 아스키 코드를 참조하여 48을 더해줘야 문자형 숫자로 바꿀 수 있다.
    # 또한, str()를 사용할 수 없으니, 일의 자리수부터 반환이 된다.
    # 이를 역순으로 출력해야하므로, 빈 리스트에 다 집어넣은 다음, 역순으로 출력하도록 하자 

    N = inti # 입력으로 들어오는 값. 혹시 모를 원본 손상을 막기 위해 다른 변수에 할당함
    result =[] # 정수가 문자로 변환되어 채워질 리스트
    
    # 문제에서 추가로 언급한, 음수일때의 고려사항을 살피자.
    # 나는 문자열 이어붙이기를 통해 (immutable 하지만, sequental 한 문자열의 특징) 함수를 구현했기에,
    # 받아줄 문자열에 "-"만 미리 넣어주면 된다.
    
    
    if N >= 0:
        str =''
    else: # N < 0: // N이 음수일 경우에는 str에 미리 -을 넣어놓고, N에 절대값을 취해준다.
        str = '-'
        N *= -1
    
    #루프가 반복되며, N은 0이 될 것이고, 그때 마다 a는 N의 1의 자리를 토해낼 것이다.
    # result만이 꾸준히 문자로 변환된 정수들을 받아주고 있을 것이다.
    while N>0:
        a = N%10
        result += [chr(a + 48)]
        N=N//10
    # 루프가 종료되면 result에는 문자로 변환된 정수들이 역순으로 들어가 있을 것이다.
    # 이것을 다른 변수에 정방향으로 옮기고, 반환하자.
    for idx in range(len(result)-1,-1,-1):
        str += result[idx]
    
    return str



my_str = itoa(1234)
my_minus = itoa(-1234)
print(my_str,type(my_str))
print(my_minus,type(my_minus))



# ==, is 를 이용해서 값이 같은지를 확인한다..
# print(ord('0')==48)