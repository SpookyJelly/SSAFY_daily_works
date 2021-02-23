array = []


sample = input() #입력될 문자열

test= list(sample)

top = -1
i = 0
result = 1
while i<len(sample)-1:
    if sample[i] == '('or sample[i] =='{'or sample[i]=='[':
        array.append(sample[i])
        top += 1
    else:
        a = array[-1]
        if (a == '(' and sample[i] ==')') or( a == '{' and sample[i] =='}') or (a == '[' and sample[i] ==']') :
            a = array.pop(top)
            top -= 1
            continue
        result = 0
        break
    i+=1
print(f'sample :{test} array :{array} result : {result}')

# 으음...계속 실패하네...스택 구현하는 방법 좀 더 생각해보자.