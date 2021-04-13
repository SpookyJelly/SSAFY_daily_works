# 해설 보러 오신 분들께는 죄송한 말씀이지만, 이번 문제는 저도 어떻게 풀었는지 모르겠습니다.
# 기본 아이디어는 00000..이 아닌 한 라인에서 암호코드를 도출하는 것인데,
# 한 라인에 두개 이상의 암호코드가 있는 경우를 처리하는 알고리즘 설계에서 정신줄을 놔버렸습니다.
# 때문에 후반부는 직관적인 흐름으로 작성되었습니다. 그래서 저도 설명하기가 참 어렵습니다...유감입니다.

# 1240번 하드코어 버전.
# 단, 암호 코드 조합이 1과0의 갯수가 아닌 비율로 결정된다.
# 따라서, 해독한 코드가 몇대 몇의 비율로 이루어져 있는지 확인해야한다.
# -> 가장 적게 등장한 패턴이 최소비 -> 최소비로 전체 패턴을 나누면 1240번 패턴을 만들 수 있다.
import sys
sys.stdin = open('1242_input.txt','r')

# 16진법 -> 2진법 함수
def hex_to_bin(n:int)->str:
    filt = 0b1000
    result = ''
    for _ in range(4):
        t = filt&n
        if t == 0:
            result += '0'
        else:
            result += '1'
        filt >>= 1
    return result

# 해답지
decipher = {
    '211' : 0,
    '221' : 1,
    '122' : 2,
    '411' : 3,
    '132' : 4,
    '231' : 5,
    '114' : 6,
    '312' : 7,
    '213' : 8,
    '112' : 9,
}

# 암호코드를 1240번 처럼 정상적으로 줄여주는 함수
# 긴 암호코드에서는 abc가 decipher 키 값보다 더 커지는데, 
# abc를 비례관계에 맞게 변경해주어 decipher를 온전히 사용하게 해준다.
def neck_slice(a,b,c)->list:
    small = min(a,b,c)
    a = a//small
    b = b//small
    c = c//small
    return [str(a)+str(b)+str(c)]

# 암호문 -> 숫자
def get_num(key_lst:list)->list:
    result = []
    for key in key_lst:
        result.append(decipher[key])
    return result

# 올바른 암호인지 확인하는 함수
def proof_it(lst:list)->int:
    total = 0
    for idx in range(len(lst)):
        # 홀수 인덱스 == 짝수 자리 
        if idx%2:
            total += lst[idx]
        # 짝수 인덱스 == 홀수 자리
        else:
            total += lst[idx]*3
    if total%10 == 0:
        return sum(lst)
    else:
        return 0


TC = int(input())

for tc in range(1,TC+1):
    N,M = map(int,input().split()) # N : 배열의 세로 크기, M: 배열의 가로 크기
    code = [input() for _ in range(N)]

    bi_code = ''
    barcode = set()
    am_i_null = '0'*(M*4)
    for row in range(len(code)):
        for col in range(len(code[0])):
            if code[row][col].isdecimal():
                bi_code += hex_to_bin(int(code[row][col]))
            else:
                bi_code += hex_to_bin(ord(code[row][col]) - ord('A') + 10)
        if bi_code == am_i_null:
            bi_code = ''
        else:
            if bi_code not in barcode:
                barcode.add(bi_code)
            bi_code = ''

    # 비문을 꺼내는 과정을 정규표현식으로 접근해보려고 했는데, 숙련도 부족으로 실패.
    # 조금 더 숙련도를 쌓은 후 도전해봄직하다.

    # 암호 스캔한거 저장할 리스트
    result = []
    ans = []
    int_ans = 0

    for password in barcode:
        a,b,c = 0,0,0
        for idx in range(len(password)):
            if b==0 and c==0 and password[idx] == '1':
                a += 1
            elif a>0 and c==0 and password[idx] == '0':
                b+=1
            elif a>0 and b>0 and password[idx] == '1':
                c += 1
            
            if a>0 and b>0 and c>0 and password[idx] == '0':
                result.extend(get_num(neck_slice(a,b,c)))
                a,b,c =0,0,0

            if len(result) == 8:
                if result not in ans:
                    ans.append(result)
                    int_ans += proof_it(result)
                result = []

    print('#{0} {1}'.format(tc,int_ans))


