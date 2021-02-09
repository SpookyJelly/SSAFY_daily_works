lst = [2,3,5,2,2,1,7,7,2]


# for 반복을 사용하여 2가 몇개?
cnt = 0
for i in range(len(lst)):
    if lst[i] == 2:
        cnt+=1
print(cnt)


# while 반복을 이용해서 2가 몇개?

cnt = 0
i = 0
while(i<len(lst)):
    if lst[i] == 2:
        cnt +=1
    i+=1
print(cnt)



lst = [2,3,5,2,2,1,7,7,2]
#숫자가 커지다가 작아지는(같아지는) 경우에 위치와 값을 출력하라

case = 1
for i in range(len(lst)):
    if lst[i]<lst[i+1]:
        case = 1
    else:
        case=0
    if case==0:
        print(i, lst[i])
        break


# 반복이 몇번 될지 모를때는 while문이 더 낫다.
i=1
while lst[i-1]<lst[i]:
    i+=1
print(i,lst[i])


# 숫자가 두번째 커지다가 작아지는 경우에 위치와 값을 출력하라

lst=[2,3,5,2,2,1,7,7,2]

i=1
cnt =0
while(cnt<1):
    if lst[i-1]>lst[i]:
        cnt +=1
    i+=1
print(i,lst[i])
