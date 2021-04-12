# 연습문제 1
# 0과 1로 이루어진 1차 배열에서 7개 바이트를 묶어서 10진수로 출력하기

def prt(s):
    t= 0
    for i in range(7):
        t = (t<<1)| int(s[i])
    print(t, end = ' ')


# byte_lst = list(input())
byte_lst = ['0','0','0','0','0','0','1','0','0','0','1','1','0','1']
converted = []
for i in range(0,len(byte_lst),7):
    tem = byte_lst[i:i+7]
    tem_num = ''
    for i in range(len(tem)):
        tem_num += tem[i]
    converted.append(tem_num)
# print(converted)
for word in converted:
    prt(word)
