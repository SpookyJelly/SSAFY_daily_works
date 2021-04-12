# 연습문제 2
# 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서 7bit 씩 묶어 십진수로 변환하여 출력


hex_dic ={
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}

# sample = list(input())
sample = ['0','F','9','7','A','3']
converted_hex = ''
for num in sample:
    converted_hex += hex_dic[num]

result = []
for i in range(0,len(converted_hex),7):
    result.append(converted_hex[i:i+7])

for num in result:
    print(int(num,2), end= ' ')
